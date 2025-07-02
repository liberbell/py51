import requests
from httpx import get
from selectolax.parser import HTMLParser

def get_img_tags_for(term):
    url = f"https://unsplash.com/s/phtoss/{term}"
    resp = get(url)
    print(resp.text)
    
    if resp.status_code != 200:
        raise Exception("Error getting response")
    
    tree = HTMLParser(resp.text)
    imgs = tree.css("figure a img + div img")
    return imgs


data = get_img_tags_for("galaxy")
print(data)
# if __name__ == "__main__":
#     print(get_img_tags_for("galaxy"))