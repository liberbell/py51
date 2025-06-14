import requests
from bs4 import BeautifulSoup

url = "https://books.toscrape.com"

resp = requests.get(url)
if resp.status_code == 200:
    soup = BeautifulSoup(resp.content, "html.parser")
    books_tags = soup.find_all("article", attrs={"class": "product_pod"})