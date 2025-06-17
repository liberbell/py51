import requests
from bs4 import BeautifulSoup
import re
from random import choice
import pandas as pd

url = "https://books.toscrape.com"


def clean_price2(price):
    return float(re.sub("[^0-9.]", "", price))

def convert_rating(rating):
    ratings = {
        "One": 1,
        "Two": 2,
        "Three": 3,
        "Four": 4,
        "Five": 5
    }
    return ratings.get(rating, 0)


def extract_book_data(book_tag):
    title = book_tag.find("h3").find("a")["title"]
    price = book_tag.find("p", attrs={"class": "price_color"}).get_text()
    rating = book_tag.find("p", attrs={"class": "star-rating"})["class"][-1]

    return {
        "title": title,
        "price": clean_price2(price),
        "rating": convert_rating(rating)
    }
    # return title, price, rating

def clean_price(price):
    # return "".join([char for char in price if char.isdigit() or char == '.'])
    return float("".join([char for char in price if char.isdigit() or char == '.']))

def fiction_category_anchor(tag):
    return tag.name == "a" and "category" in tag["href"]

resp = requests.get(url)
# if resp.status_code == 200:
#     soup = BeautifulSoup(resp.content, "html.parser")
#     books_tags = soup.find_all("article", attrs={"class": "product_pod"})
#     # book_title, book_price, book_rating = extract_book_data(books_tags[3])
#     # book_price = clean_price2(book_price)
#     # print(book_title, book_price, book_rating)
#     # print(type(book_price))
#     books_data = [extract_book_data(book_tag) for book_tag in books_tags]
    # print(books_data)

# books_tags = soup.find_all("article", attlrs={"class": "product_pod"})


# print(extract_book_data(choice(books_tags)))
# for book in books_data:
#     print(book["price"])

# print(extract_book_data(choice(books_tags)))
# for book in books_data:
#     if book["price"] < 20:
#         print(book["title"])

# df = pd.DataFrame(books_data)
# print(df)
# print(df.price.mean())
# print(df[df.price < 20])
# df.to_csv("book.csv", index=False)
# df.to_json("book.json", orient="records")

if resp.status_code == 200:
    soup = BeautifulSoup(resp.content, "html.parser")
    soup_id = soup.find_all(attrs={"id": "messages"})
    soup_id = soup.find_all(attrs={"id": lambda x: x is not None})
    soup_id = soup.find_all(lambda x: x is not None)
    soup_id = soup.find_all(lambda x: x.has_attr("id"))
    print(soup_id)