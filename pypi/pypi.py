
import sys
import requests
from bs4 import BeautifulSoup

ui = sys.argv[1]
url = f"https://pypi.org/search/?q={ui}&o="
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
cards = soup.find_all("li")

for card in cards:

    title = card.find("span", class_="package-snippet__name")
    version = card.find("span", class_="package-snippet__version")
    date = card.find("span", class_="package-snippet__created")
    desc = card.find("p", class_="package-snippet__description")
    
    if title is not None and version is not None:
        print(f"\nTitle: {title.text.strip()}   -   Version: {version.text.strip()}   -   Created: {date.text.strip()}   -   Description: {desc.text.strip()}")

print('\n')
