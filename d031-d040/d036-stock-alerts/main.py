# Stock Trading News Alert

# Track the price of a stock, and when the price varies a lot, check
# the news for any reason, then alert a user about it.
#
# Originally planned to use SMS for the alerts, but because it is not
# possible to create a free account on Twilio without providing a real
# phone number, it was modified to use email instead.
#
# More practice with the existing concepts, nothing new on this day.

import requests
import smtplib
import os

DEBUG = True

STOCK = "TSLA"
COMPANY_NAME = "Tesla"

AV_API_KEY = os.environ.get('AV_API_KEY')
AV_API_ROOT = 'https://www.alphavantage.co/query'
AV_PARAMS = {
    'function': 'GLOBAL_QUOTE',
    'symbol': STOCK,
    'apikey': AV_API_KEY
}
ALERT_THRESHOLD = 0.001

NEWS_COUNT = 3
NEWS_API_KEY = os.environ.get('NEWS_API_KEY')
NEWS_API_ROOT = 'https://newsapi.org/v2/top-headlines'
NEWS_PARAMS = {
    'apiKey': NEWS_API_KEY,
    'q': STOCK,
    'pageSize': NEWS_COUNT,
    'country': 'us',
    'category': 'business',
    'page': 1
}

SOURCE_EMAIL = os.environ.get('MY_EMAIL')
SOURCE_PASS = os.environ.get('MY_EMAIL_PASSWORD')
SMTP_SERVER = 'smtp-mail.outlook.com'
SMTP_PORT = 587


def stock_change() -> float:
    response = requests.get(url=AV_API_ROOT, params=AV_PARAMS)
    response.raise_for_status()
    data = response.json()

    price = float(data['Global Quote']['05. price'])
    prev_price = float(data['Global Quote']['08. previous close'])

    diff = price / prev_price * 100
    percentage_change = 100 - diff

    if DEBUG:
        print(f'Price: {price}. Previous close: {prev_price}')
        print(f'Percentage change: {percentage_change}')

    return percentage_change


def get_news() -> (str, str):
    response = requests.get(url=NEWS_API_ROOT, params=NEWS_PARAMS)
    response.raise_for_status()
    data = response.json()

    articles = [
        (article['title'], article['description'])
        for article in data['articles']]

    print(articles)
    return articles


def send_email(to_email: str, subject: str, message: str) -> None:
    with smtplib.SMTP(
            host=SMTP_SERVER,
            port=SMTP_PORT,
            timeout=30) as connection:
        connection.starttls()
        connection.login(user=SOURCE_EMAIL, password=SOURCE_PASS)
        connection.sendmail(
            from_addr=SOURCE_EMAIL,
            to_addrs=to_email,
            msg=f'Subject: {subject}!\n\n{message}')


# taken from https://stackoverflow.com/a/2743163
def strip_non_ascii(string: str) -> str:
    """Returns the string without non ASCII characters"""
    stripped = (c for c in string if 0 < ord(c) < 127)
    return ''.join(stripped)


change_percent = stock_change()

if abs(change_percent) > ALERT_THRESHOLD:
    change = '^' if change_percent > ALERT_THRESHOLD else 'v'
    title = f'{STOCK} {change} {change_percent:.2f}%'

    news_tuples = get_news()
    news = ''

    for (headline, brief) in news_tuples:
        news += f'Headline: {headline}\nBrief: {brief}\n\n'

    if len(news) == 0:
        news = 'No headlines found, no idea why the stock is moving!'

    send_email(SOURCE_EMAIL, title, strip_non_ascii(news))
