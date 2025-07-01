import requests
from httpx import get
from selectolax.parser import HTMLParser

def get_img_tags_for(term="galaxy"):
    url = f"https://unsplash.com/s/phtoss/{term}"
    pass

if __name__ == "__main__":
    print(get_img_tags_for("python"))