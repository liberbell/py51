import requests
from bs4 import BeautifulSoup

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
    print(list(soup.ul.children))
