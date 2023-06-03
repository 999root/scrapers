from bs4 import BeautifulSoup
import requests

user_input = input("\nInput the game's name: ")
print('\n')
url = f"https://rpcs3.net/compatibility?g={user_input}#jump"
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
main_containers = soup.find_all("label", class_="compat-table-row")

for container in main_containers:
    country = container.find("div", class_="compat-table-cell compat-table-cell-gameid").text.strip()
    game_title = container.find("div", class_="compat-table-cell").text.strip()
    status = container.find("div", class_="txt-compat-status background-status-1").text.strip()
    updated = container.find("div", class_="compat-table-cell compat-table-cell-updated").text.strip()

    output = f"""
--------------------------------------------------

Game IDs:
{country}

Game Title:
{game_title}

Status:
{status}

Last Updated:
{updated}

"""

    print(output)
