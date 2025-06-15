import requests
from bs4 import BeautifulSoup

url = "https://books.toscrape.com"

def extract_book_data(book_tag):
    # title = book_tag.find("h3").find("a")["title"]
    title = book_tag.find("h3").find("h3").find("a")

resp = requests.get(url)
if resp.status_code == 200:
    soup = BeautifulSoup(resp.content, "html.parser")
    books_tags = soup.find_all("article", attrs={"class": "product_pod"})
    print(books_tags[0].prettify())