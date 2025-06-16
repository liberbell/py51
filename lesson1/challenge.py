import requests
from bs4 import BeautifulSoup
import re
from random import choice

url = "https://books.toscrape.com"


def clean_price2(price):
    return float(re.sub("[^0-9.]", "", price))

def extract_book_data(book_tag):
    title = book_tag.find("h3").find("a")["title"]
    price = book_tag.find("p", attrs={"class": "price_color"}).get_text()
    rating = book_tag.find("p", attrs={"class": "star-rating"})["class"][-1]

    return {
        "title": title,
        "price": clean_price2(price),
        "rating": rating
    }
    # return title, price, rating

def clean_price(price):
    # return "".join([char for char in price if char.isdigit() or char == '.'])
    return float("".join([char for char in price if char.isdigit() or char == '.']))


resp = requests.get(url)
if resp.status_code == 200:
    soup = BeautifulSoup(resp.content, "html.parser")
    books_tags = soup.find_all("article", attrs={"class": "product_pod"})
    book_title, book_price, book_rating = extract_book_data(books_tags[3])
    # book_price = clean_price2(book_price)
    print(book_title, book_price, book_rating)
    print(type(book_price))

print(extract_book_data(choice(books_tags)))