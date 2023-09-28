import requests
from bs4 import BeautifulSoup
import re

BASE_URL = 'https://999.md/ru/list/real-estate/apartments-and-rooms'
PREFIX = 'https://999.md'


def fetch_links(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        pattern = r'^/ro/\d{8}$'
        links = [PREFIX + link.get('href') for link in soup.find_all('a', href=re.compile(pattern))]
        return links


def scrape_all_links(base_url, max_pages):
    all_links = set()
    for page in range(1, max_pages + 1):
        page_url = f"{base_url}?page={page}"
        page_links = fetch_links(page_url)
        all_links.update(page_links)
    return all_links


MAX_PAGES = 10
links = scrape_all_links(BASE_URL, MAX_PAGES)

for link in links:
    print(link)