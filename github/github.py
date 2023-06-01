import sys
from bs4 import BeautifulSoup
import requests

if len(sys.argv) < 2:
    print("Please provide a username as a command-line argument.")
    sys.exit(1)

username = sys.argv[1]
print('\n')
url = f"https://github.com/{username}"
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
maincontainer = soup.find_all("div", class_="js-profile-editable-replace")

for container in maincontainer:
    display_name = container.find("span", class_="p-name vcard-fullname d-block overflow-hidden")
    username = container.find("span", class_="p-nickname vcard-username d-block")
    quote = container.find("div", class_="css-truncate css-truncate-target width-fit color-fg-default text-left")
    bio = container.find("div", class_="p-note user-profile-bio mb-3 js-user-profile-bio f4")
    email = container.find("a", class_="Link--primary")

    if display_name is not None:
        print(f"Display Name: {display_name.text.strip()}")
    if username is not None:
        print(f"Username: {username.text.strip()}")
    if quote is not None:
        print(f"Quote: {quote.text.strip()}")
    if bio is not None:
        print(f"Bio: {bio.text.strip()}")
    if email is not None:
        print(f"Email: {email.text.strip()}")

    print('\n')
