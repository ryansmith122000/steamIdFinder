from pprint import pprint
import requests
from bs4 import BeautifulSoup

valid_steamidio_url = 'https://steamid.io/lookup/76561198258233294'
steam_profile_url = 'https://steamcommunity.com/id/bumbelheadlmao/'

form_website_url = 'https://steamid.io/lookup'
response = requests.post(form_website_url, data={'input': steam_profile_url})
soup = BeautifulSoup(response.text, features='html.parser')
values = [item.text.strip() for item in soup.select('.value')]
keys = [key.text.strip() for key in soup.select('.key')]

data = {
    key: value for key, value in zip(keys, values)
}

pprint(data)
