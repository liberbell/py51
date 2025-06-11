import requests
from bs4 import BeautifulSoup
from bs4.element import NavigableString

url1 = "https://books.toscrape.com"
resp = requests.get(url1)

# print(resp.content)
if resp.status_code == 200:
    soup = BeautifulSoup(resp.content, "html.parser")
    # print(soup.title)
    # print(soup.h1)
    # print(soup.div)
    first_div = soup.div
    # print(first_div.div.div.attrs)
    # print(list(soup.ul.children))
    print(list(filter(lambda x: type(x) != NavigableString, soup.ul.children)))

def no_navigable_strings(iterable):
    return list(filter(lambda x: type(x) != NavigableString, iterable))