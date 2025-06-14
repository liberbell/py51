import requests
from bs4 import BeautifulSoup
from bs4.element import NavigableString

url1 = "https://books.toscrape.com"
resp = requests.get(url1)

def no_navigable_strings(iterable):
    return list(filter(lambda x: type(x) != NavigableString, iterable))

# print(resp.content)
if resp.status_code == 200:
    soup = BeautifulSoup(resp.content, "html.parser")
    # print(soup.title)
    # print(soup.h1)
    # print(soup.div)
    first_div = soup.div
    # print(first_div.div.div.attrs)
    # print(list(soup.ul.children))
    # print(list(filter(lambda x: type(x) != NavigableString, soup.ul.children)))
    li_child = no_navigable_strings(soup.ul.children)
    # print(li_child)
    # print(list(soup.ul.descendants))
    # desc = no_navigable_strings(soup.ul.descendants)
    # print(desc[0])
    # print(soup.ul.li)
    # print(soup.ul.li.next_sibling.next_sibling)
    # print(soup.a.get_text())
    # print(soup.a.text, soup.a.string)
    # print(soup.ul.text)
    # print(soup.ul.string)
    # print(soup.a.text, " of type ", type(soup.a.text))
    # print(soup.a.get_text(), " of type ", type(soup.a.get_text()))
    # print(soup.a.string, " of type ", type(soup.a.string))

    # print(soup.stripped_strings)
    # all_strings = list(soup.stripped_strings)
    # print(len(all_strings))

    # print(len(soup.find_all()))
    # print(len(soup.find_all(["a", "p"])))
    price_tags = soup.find_all("p", attrs={"class": "price_color"})

    for price in price_tags:
        print(price.get_text())

    # add_buttons = soup.find_all("button", attrs={"data-loding-text": "Adding..."})
    add_buttons = soup.find_all("button", attrs={"data-loading-text": "Adding..."})
    add_buttons = soup.find_all("button", attrs={"data-loading-text": lambda x: "add" in x.lower() or "remove" in x.lower()})
    # add_buttons = soup.find_all("button")
    print(add_buttons)


