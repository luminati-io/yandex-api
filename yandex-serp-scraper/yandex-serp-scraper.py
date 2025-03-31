"""
Yandex SERP Scraper using Playwright
Extracts organic search results with accurate ranking for multiple search terms.
Outputs CSV with fields: search_term, rank, title, url, description
"""

import csv
import re
import time
import random
import asyncio
from urllib.parse import quote_plus
from bs4 import BeautifulSoup
from playwright.async_api import async_playwright

# Configuration
CONFIG = {
    "max_retries": 2,
    "request_delay": (1, 3),
    "max_concurrent": 3,
    "csv_fields": ["search_term", "rank", "title", "url", "description"],
    "search_terms": {"ergonomic office chair": 2},
    "user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36",
}


class YandexScraper:
    """Main scraper class encapsulating all functionality"""

    @staticmethod
    async def fetch_page(browser, search_term: str, page_num: int) -> str:
        """Fetch Yandex search page with retry logic"""
        url = f"https://yandex.com/search/?text={quote_plus(search_term)}&p={page_num}"

        for attempt in range(CONFIG["max_retries"]):
            try:
                context = await browser.new_context(
                    user_agent=CONFIG["user_agent"], locale="en-US"
                )
                page = await context.new_page()

                await page.set_extra_http_headers({"Accept-Language": "en-US,en;q=0.9"})
                await asyncio.sleep(random.uniform(*CONFIG["request_delay"]))

                response = await page.goto(url, wait_until="networkidle")
                if not response.ok:
                    continue

                await page.wait_for_selector("li.serp-item", timeout=10000)
                html = await page.content()

                if "serp-item" in html:
                    return html

            except Exception as e:
                if attempt == CONFIG["max_retries"] - 1:
                    print(f"Failed to fetch '{search_term}' page {page_num + 1}: {e}")
                await asyncio.sleep(2**attempt)
            finally:
                if "context" in locals():
                    await context.close()

        return None

    @staticmethod
    def parse_results(html: str, search_term: str, page_num: int) -> list[dict]:
        """Parse Yandex results page and extract structured data"""
        if not html:
            return []

        soup = BeautifulSoup(html, "html.parser")
        results = []

        for local_rank, result in enumerate(soup.select("li.serp-item"), 1):
            try:
                if result.get("data-type") == "ads" or "captcha" in result.get(
                    "class", []
                ):
                    continue

                link = result.select_one("a.OrganicTitle-Link")
                title_elem = result.select_one(
                    "span.OrganicTitle-LinkText, h2.OrganicTitle-LinkText"
                )
                desc_elem = result.select_one(
                    "div.Organic-ContentWrapper span.OrganicTextContentSpan"
                )

                url = link["href"] if link and link.has_attr("href") else ""
                if url.startswith("/r?"):
                    if match := re.search(r"&u=([^&]+)", url):
                        url = match.group(1)

                results.append(
                    {
                        "search_term": search_term,
                        "rank": (page_num * 10) + local_rank,
                        "title": title_elem.get_text(strip=True) if title_elem else "",
                        "url": url,
                        "description": (
                            desc_elem.get_text(strip=True) if desc_elem else ""
                        ),
                    }
                )

            except Exception:
                continue

        return results

    @staticmethod
    async def scrape_term(playwright, search_term: str, pages: int) -> list[dict]:
        """Scrape all pages for a single search term"""
        browser = await playwright.chromium.launch(headless=True)

        try:
            tasks = [
                YandexScraper.fetch_page(browser, search_term, page_num)
                for page_num in range(pages)
            ]
            html_results = await asyncio.gather(*tasks)

            results = []
            for page_num, html in enumerate(html_results):
                if html:
                    results.extend(
                        YandexScraper.parse_results(html, search_term, page_num)
                    )

            return sorted(results, key=lambda x: x["rank"])
        finally:
            await browser.close()


async def main():
    """Main execution function"""
    start_time = time.time()
    total_results = 0

    async with async_playwright() as playwright:
        semaphore = asyncio.Semaphore(CONFIG["max_concurrent"])

        async def controlled_scrape(term, pages):
            async with semaphore:
                return term, await YandexScraper.scrape_term(playwright, term, pages)

        tasks = [
            controlled_scrape(term, pages)
            for term, pages in CONFIG["search_terms"].items()
        ]
        scraped_results = await asyncio.gather(*tasks)

        with open("yandex_results.csv", "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=CONFIG["csv_fields"])
            writer.writeheader()

            for term, results in scraped_results:
                if results:
                    writer.writerows(results)
                    total_results += len(results)
                    print(f"→ Captured {len(results)} results for '{term}'")

    print(
        f"\n✔ Success! Saved {total_results} results in {time.time() - start_time:.2f}s"
    )
    print("Results saved to: yandex_results.csv")


if __name__ == "__main__":
    asyncio.run(main())
