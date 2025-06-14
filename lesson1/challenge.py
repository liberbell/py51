import requests
from bs4 import BeautifulSoup

url = "https://books.toscrape.com"

resp = requests.get(url)