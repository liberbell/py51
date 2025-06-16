import requests
from bs4 import BeautifulSoup

url = "https://books.toscrape.com"

def extract_book_data(book_tag):
    title = book_tag.find("h3").find("a")["title"]
    price = book_tag.find("p", attrs={"class": "price_color"}).get_text()
    rating = book_tag.find("p", attrs={"class": "star-rating"})["class"][-1]
    return title, price, rating

resp = requests.get(url)
if resp.status_code == 200:
    soup = BeautifulSoup(resp.content, "html.parser")
    books_tags = soup.find_all("article", attrs={"class": "product_pod"})
    book_title, book_price, book_rating = extract_book_data(books_tags[0])
    print(book_title, book_price, book_rating)