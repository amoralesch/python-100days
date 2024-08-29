# Web Scrapper

# Create a program that reads an HTML page, and extract information,
# i.e. a web scrapper.
#
# Use new library (beatifulsoup) and practice HTML DOM structure.

import bs4 as bs
import requests

URL = 'https://www.timeout.com/film/best-movies-of-all-time'

response = requests.get(URL)
response.raise_for_status()

html = response.text

soup = bs.BeautifulSoup(html, 'html.parser')
headers = soup.select('h3[data-testid="tile-title_testID"]')

titles = []
for header in headers:
    rank = header.find('span')

    if rank is None:
        continue

    info = header.text.replace('\xa0', ' ')

    titles.append(info)

with open('movies.txt', 'w') as file:
    file.write('Movies you must watch!\n\n')
    file.write('\n'.join(titles))
