import requests
from bs4 import BeautifulSoup

def get_products(URL):
    products = []
    i = 0

    while True:
        resp = requests.get(f"{URL}{i}")
        if resp.status_code != 200:
            break

        soup = BeautifulSoup(resp.text, 'html.parser')
        divs = soup.find_all('div')

        for div in divs:
            h1s = div.find_all("h1")
            product = {
                "name": h1s[0].text,
                "author": h1s[1].text,
                "price": h1s[2].text,
                "description": h1s[3].text,
            }
            products.append(product)

        i += 1

    return products

if __name__ == "__main__":
    URL = "http://127.0.0.1:8081/product/"
    print(get_products(URL))
