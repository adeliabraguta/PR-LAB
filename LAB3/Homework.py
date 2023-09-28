import requests
from bs4 import BeautifulSoup


def scrape_product_details(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')

    product_details = []

    title = soup.find('h1').text
    product_details.append(f"Title: {title}")

    for li in soup.find_all('li', class_='m-value'):
        key = li.find('span', class_='adPage__content__features__key').text
        value = li.find('span', class_='adPage__content__features__value').text
        product_details.append(f"{key}:{value}")

    return product_details


url = "https://999.md/ro/16998771"
product_details = scrape_product_details(url)
print(*product_details, sep='\n')