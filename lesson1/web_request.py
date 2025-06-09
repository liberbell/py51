from urllib.request import urlopen

url = "https://quotes.toscrape.com/"
# response = urlopen(url)
# print(response.status, response.read().decode("utf-8"))

with urlopen(url=url) as resp:
    content = resp.read()
    print(content.decode("utf-8"))