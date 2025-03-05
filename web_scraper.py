# Import library
import os
import requests
from bs4 import BeautifulSoup

# Set data directory
data_dir = "data"
if not os.path.exists(data_dir):
    os.makedirs(data_dir)

# List of URLs to scrape
URLS = [
    "http://myaastha.in/",
    "http://myaastha.in/about-us/",
    "http://myaastha.in/how-to-become-a-member/",
    "http://myaastha.in/scheme/savings-account/",
    "http://myaastha.in/scheme/recurring-deposits/",
    "http://myaastha.in/scheme/fixed-deposit/",
    "http://myaastha.in/scheme/monthly-income/",
    "http://myaastha.in/loan/#",
    "http://myaastha.in/personal-loan/",
    "http://myaastha.in/advance-against-deposits/",
    "http://myaastha.in/loan-against-property/",
    "http://myaastha.in/contact-us/"
]

def clean_filename(url):
    """Converts a URL to a safe filename."""
    return url.replace("http://", "").replace("https://", "").replace("/", "_") + ".txt"

def scrape_website(url):
    """Scrapes content from a given URL and saves it in a separate file."""
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        content = []
        for tag in soup.find_all(['h1', 'h2', 'h3', 'p', 'table', 'li', 'div']):
            if tag.parent.name != "header" and tag.parent.name != "footer":
                content.append(tag.get_text(" ", strip=True))
        
        filename = os.path.join(data_dir, clean_filename(url))
        with open(filename, "w", encoding="utf-8") as f:
            f.write("\n".join(content))
        print(f"Scraped and saved: {filename}")
    else:
        print(f"Failed to fetch {url}")

for url in URLS:
    scrape_website(url)