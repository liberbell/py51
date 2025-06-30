import requests
from selectolax.parser import HTMLParser

url = "https://en.wikipedia.org/wiki/Rare-earth_element"

resp = requests.get(url)

tree = HTMLParser(resp.text)
print(type(tree))
print(tree.css("p"))