import requests
from selectolax.parser import HTMLParser
from random import choice

url = "https://en.wikipedia.org/wiki/Rare-earth_element"

resp = requests.get(url)

tree = HTMLParser(resp.text)
# print(type(tree))
# print(tree.css("p"))

random_node = choice(tree.css("img"))
print(random_node.attributes)
# print(random_node.html)
print(random_node.text())
# print(tree.css("p")[0].text())