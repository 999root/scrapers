import requests
from bs4 import BeautifulSoup

search_keyword = input("\nEnter the search keyword: ")
print('\n')

url = f"https://www.npmjs.com/search?q={search_keyword}&page=1"
response = requests.get(url)
response.raise_for_status()
soup = BeautifulSoup(response.text, 'html.parser')

results = soup.find_all('div', class_='_0d2164ff')
print("Search results:")
for result in results:
    package_name = result.find('h3', class_='db7ee1ac fw6 f4 black-90 dib lh-solid ma0 no-underline hover-black')
    package_description = result.find('p', class_='_8fbbd57d f5 black-60 mt1 mb0 pv1 no-underline lh-copy')
    print('\n')
    if package_name is not None:
        print(f"Package Name: {package_name.text.strip()}")
    if package_description is not None:
        print(f"Description: {package_description.text.strip()}")
    print('\n')
