# Amazon Price Tracker

# Create a script that will check the price of products on Amazon, and
# if the price drops lower than some pre-defined value, send an email
# alerting us.
#
# Again, no new toppics, just more practices for projects starting from
# scratch

import os
import bs4
import requests
import pandas
from etc.helpers import send_email

ALERT_EMAIL = os.environ.get('MY_EMAIL')


class Product:
    def __init__(self, name: str, url: str, price: int):
        self.name = name
        self.url = url
        self.price = price


def get_list_of_products() -> list[Product]:
    info = pandas.read_csv('products.csv')

    return [
        Product(row['PRODUCT'], row['URL'], row['MAX_PRICE'])
        for _, row in info.iterrows()
    ]


def get_price(url: str) -> int:
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:125.0) Gecko/20100101 Firefox/125.0',
        'Accept-Language': 'en-US,en;q=0.5'
    }

    response = requests.get(url, headers=headers)
    response.raise_for_status()
    html = response.text

    soup = bs4.BeautifulSoup(html, 'html.parser')
    price = soup.select(
        'div#buyBoxAccordion '
        'span.a-price '
        'span.a-price-whole')[0]

    return int(price.text[:-1])


def alert(product: Product, price: int):
    subject = f'Buy now! - {product.name}'
    message = f"""
        Alert! The product {product.name} is right now at only ${price},
        that's less than your limit of {product.price}.

        Take advantage of this offer now!

        Direct URL: {product.url}"""

    send_email(ALERT_EMAIL, subject, message)


products = get_list_of_products()

for current_product in products:
    current_price = get_price(current_product.url)

    if get_price(current_product.url) <= current_product.price:
        alert(current_product, current_price)
