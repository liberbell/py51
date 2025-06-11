import requests
from bs4 import BeautifulSoup

url1 = "https://www.toscrape.com"
resp = requests.get(url1)

print(resp.content)