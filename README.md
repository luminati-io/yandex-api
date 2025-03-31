# Yandex Search Scraper

[![Promo](https://github.com/luminati-io/LinkedIn-Scraper/blob/main/Proxies%20and%20scrapers%20GitHub%20bonus%20banner.png)](https://brightdata.com/products/serp-api/yandex-search)

This repository offers two reliable solutions for extracting data from Yandex Search Engine Results Pages (SERPs):

- **Free Yandex Scraper:** A basic tool for scraping Yandex Search Results at small scale
- **Enterprise-grade Yandex SERP API:** A scalable, production-ready solution for high-volume, real-time data extraction (part of [Bright Data's SERP Scraper API](https://brightdata.com/products/serp-api))

## Table of Contents
- [Free Yandex SERP Scraper](#free-yandex-serp-scraper)
  - [Setup Requirements](#setup-requirements)
  - [Quick Start Guide](#quick-start-guide)
  - [Sample Output](#sample-output)
  - [Limitations](#limitations)
- [Yandex SERP Scraper API](#yandex-serp-scraper-api)
  - [Key Benefits](#key-benefits)
  - [Getting Started](#getting-started)
- [Implementation Methods](#implementation-methods)
  - [Direct API Access](#direct-api-access)
  - [Native Proxy-Based Access](#native-proxy-based-access)
- [Yandex Search Query Parameters](#yandex-search-query-parameters)
  - [Localization](#localization)
  - [Pagination](#pagination)
  - [Time Range](#time-range)
  - [Device Targeting](#device-targeting)
- [Practical Example](#practical-example)
- [Support & Resources](#support--resources)

## Free Yandex SERP Scraper

The free scraper provides a straightforward way to collect Yandex SERP data at a small scale. It's perfect for developers needing limited data for personal projects, research, or testing purposes.

<img width="800" alt="free-yandex-serp-scraper" src="https://github.com/luminati-io/yandex-api/blob/main/images/428371413-775c71f6-10cf-4a2d-91b8-6f137db5b171.png" />

### Setup Requirements

- [Python 3.9+](https://www.python.org/downloads/)
- Required packages:
    - `playwright` for browser automation
    - `BeautifulSoup` for HTML parsing

```bash
pip install playwright beautifulsoup4
playwright install
```

> **New to web scraping?** Explore our [Beginner's Guide to Web Scraping with Python](https://brightdata.com/blog/how-tos/web-scraping-with-python)
>

### Quick Start Guide

1. Open [yandex-search-results-scraper.py](https://github.com/luminati-io/yandex-api/blob/main/yandex-serp-scraper/yandex-serp-scraper.py)
2. Customize the search terms and page count variables:

```python
PAGES_PER_TERM = {
    "ergonomic office chair": 2,
}
```

3. Run the script

### Sample Output
<img width="800" alt="yandex-scraper-output" src="https://github.com/luminati-io/yandex-api/blob/main/images/428371812-dbd6f456-af64-4a4a-8735-f26876ae5fa8.png" />


### Limitations
One of the biggest challenges when scraping Yandex is its aggressive CAPTCHA protection:

<img width="800" alt="yandex-captcha-challenge" src="https://github.com/luminati-io/yandex-api/blob/main/images/428371880-309e645f-c043-4231-aeb2-c3417e91b15e.png" />


Yandex uses a strict and constantly evolving anti-bot system to prevent automated data extraction. Frequent CAPTCHA triggers can quickly lead to IP blocks, making it tough to maintain stable, long-running scrapers.

While the free scraper handles basic tasks, it has several important limitations:

- High risk of IP blocking
- Limited request volume
- Constant CAPTCHA interruptions
- Not suitable for production environments

For a scalable and stable solution, consider Bright Data's dedicated API detailed below. 👇


## Yandex SERP Scraper API

The [Yandex Search API](https://brightdata.com/products/serp-api/yandex-search) is part of Bright Data’s [SERP Scraping API](https://brightdata.com/products/serp-api) suite. It leverages our industry-leading [proxy infrastructure](https://brightdata.com/proxy-types) to deliver real-time Yandex search results with a single API call.

### Key Benefits

- **Global Accuracy**: Get tailored results for specific locations worldwide
- **Pay-Per-Success**: Only pay for successful requests
- **Real-Time Data**: Access up-to-date search results in seconds
- **Unlimited Scalability**: Handle high-volume scraping effortlessly
- **Cost-Efficient**: Eliminates the need for costly infrastructure
- **Reliable Performance**: Built-in anti-blocking technology
- **24/7 Expert Support**: Access to technical assistance whenever needed

 📌 Try Before You Buy: Test it for free in our SERP API Live Demo
 
 <img width="800" alt="bright-data-serp-api-playground" src="https://github.com/luminati-io/yandex-api/blob/main/images/428391143-c089343e-50a8-4961-8d11-d312982480df.png" />


### Getting Started

1. [Create a Bright Data account](https://brightdata.com/) (new users receive a $5 credit)
2. Generate your [API key](https://docs.brightdata.com/general/account/api-token)
3. Follow our [step-by-step guide](https://github.com/luminati-io/yandex-api/blob/main/setup-serp-api-guide.md) to configure the SERP API


## Implementation Methods

### Direct API Access

The simplest way to use the API is by making a direct request to Bright Data's API endpoint.

**cURL Example:**

```bash
curl https://api.brightdata.com/request \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer API_TOKEN" \
  -d '{
        "zone": "ZONE_NAME",
        "url": "https://www.yandex.com/search/?text=apple+watch+series+10+review&lr=95&lang=en",
        "format": "raw"
      }'
```

**Python Example:**

```python
import requests
import json

url = "https://api.brightdata.com/request"

headers = {"Content-Type": "application/json", "Authorization": "Bearer API_TOKEN"}

payload = {
    "zone": "ZONE_NAME",
    "url": "https://www.yandex.com/search/?text=apple+watch+series+10+review&lr=95&lang=en",
    "format": "raw",
}

response = requests.post(url, headers=headers, json=payload)

with open("yandex-scraper-api-result.html", "w", encoding="utf-8") as file:
    file.write(response.text)

print("Response saved!")
```

### Native Proxy-Based Access

This alternative method uses proxy routing for direct access to search results.

**cURL Example:**

```bash
curl -i \
  --proxy brd.superproxy.io:33335 \
  --proxy-user brd-customer-<CUSTOMER_ID>-zone-<ZONE_NAME>:<ZONE_PASSWORD> \
  -k \
  "https://www.yandex.com/search/?text=apple+watch+series+10+review&lr=95&lang=en"
```

**Python Example:**

```python
import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

host = "brd.superproxy.io"
port = 33335
username = "brd-customer-<customer_id>-zone-<zone_name>"
password = "<zone_password>"
proxy_url = f"http://{username}:{password}@{host}:{port}"

proxies = {"http": proxy_url, "https": proxy_url}

url = "https://www.yandex.com/search/?text=apple+watch+series+10+review&lr=95&lang=en"
response = requests.get(url, proxies=proxies, verify=False)

with open("yandex-scraper-api-result.html", "w", encoding="utf-8") as file:
    file.write(response.text)

print("Response saved!")
```

> **Note:** When using the native proxy approach, it's recommended to install Bright Data's SSL certificate for production use. Learn more in the [SSL Certificate Guide](https://docs.brightdata.com/general/account/ssl-certificate).
> 

👉 See the [full HTML output](https://github.com/luminati-io/yandex-api/blob/main/yandex-scraper-api-output/yandex-scraper-api-result.html)

*The query parameters like `lr` and `lang` are explained in the next section.*


## Yandex Search Query Parameters

### Localization

#### Region (`lr`)

This parameter defines which geographic region or country to target for search results.

| Region | Code |
| --- | --- |
| Moscow | 1 |
| Saint-Petersburg | 2 |
| USA | 84 |
| Canada | 95 |
| China | 134 |

Example - Check how "best wireless earbuds" ranks in the USA:

```bash
curl --proxy brd.superproxy.io:33335 \
     --proxy-user brd-customer-<id>-zone-<zone>:<password> \
     "https://www.yandex.com/search/?text=best+wireless+earbuds&lr=84"
```

#### Language (`lang`)

Sets the language preference using two-letter language codes:

- `lang=en` - English
- `lang=es` - Spanish
- `lang=fr` - French

Example - Get sports news in Spanish:

```bash
https://www.yandex.com/search/?text=local+sports+news&lang=es
```

### Pagination

#### Page Number (`p`)

Controls which page of results to display:

- `p=0` - First page (default)
- `p=1` - Second page
- `p=4` - Fifth page

Each Yandex SERP page typically returns 10 results.

Example - Scrape page 3 (results 21-30) for "nike running shoes":

```bash
https://www.yandex.com/search/?text=nike+running+shoes&p=2
```

### Time Range

#### Time Period (`within`)

Limits results to a specific time period:

- `within=77` - Results from the past 24 hours
- `within=1` - Results from the past 2 weeks
- `within=[%pm]` - Results from the past month

Example - Get "iPhone 15 review" results from the past 24 hours:

```bash
https://www.yandex.com/search/?text=iphone+15+review&within=77
```

### Device Targeting

#### Device Type (`brd_mobile`)

Specifies which device type to simulate:

- `brd_mobile=0` or omitted - Random desktop user-agent
- `brd_mobile=1` - Random mobile user-agent
- `brd_mobile=ios` or `brd_mobile=iphone` - iPhone user-agent
- `brd_mobile=ipad` or `brd_mobile=ios_tablet` - iPad user-agent
- `brd_mobile=android` - Android phone user-agent
- `brd_mobile=android_tablet` - Android tablet user-agent

Example - Simulate an iPhone searching for responsive website testing:

```bash
https://www.yandex.com/search/?text=responsive+website+testing&brd_mobile=ios
```

#### Browser Type (`brd_browser`)

Defines which browser to simulate:

- Default (omitted) - Random browser
- `brd_browser=chrome` - Google Chrome
- `brd_browser=safari` - Safari
- `brd_browser=firefox` - Mozilla Firefox

Example - Simulate Safari browser searching for Python tutorials:

```bash
https://www.yandex.com/search/?text=how+to+learn+python&brd_browser=safari
```

> **Note:** Don't combine `brd_browser=firefox` with `brd_mobile=1` as they're incompatible.
> 

## **Practical Example**

For comprehensive targeting, you can combine multiple parameters:

```bash
https://www.yandex.com/search/?text=organic+skincare+products
&lr=95
&lang=en
&p=2
&within=1
&brd_mobile=ios
&brd_browser=safari
```

This search:

- Targets Canadian users (`lr=95`)
- Shows English results (`lang=en`)
- Displays the second page (`p=2`)
- Limits to the past 2 weeks (`within=1`)
- Simulates an iPhone user (`brd_mobile=ios`)
- Uses Safari browser (`brd_browser=safari`)

Perfect for a skincare company researching recent organic product trends in the Canadian market as viewed by iOS mobile users.


## Support & Resources

- **Documentation:** [SERP API Documentation](https://docs.brightdata.com/scraping-automation/serp-api/)
- **Related APIs:**
    - [SERP API](https://github.com/luminati-io/serp-api)
    - [Google Search API](https://github.com/luminati-io/google-search-api)
    - [Google News Scraper](https://github.com/luminati-io/Google-News-Scraper)
    - [Google Trends API](https://github.com/luminati-io/google-trends-api)
    - [Google Reviews API](https://github.com/luminati-io/google-reviews-api)
    - [Google Hotels API](https://github.com/luminati-io/google-hotels-api)
    - [Google Flights API](https://github.com/luminati-io/google-flights-api)
    - [Web Unlocker API](https://github.com/luminati-io/web-unlocker-api)
- **Use Cases:**
    - [SEO & SERP Tracking](https://brightdata.com/use-cases/serp-tracking)
    - [Travel Industry Data](https://brightdata.com/use-cases/travel)
- **Additional Reading:** [Best SERP APIs](https://brightdata.com/blog/web-data/best-serp-apis)
- **Contact Support:** [support@brightdata.com](mailto:support@brightdata.com)
