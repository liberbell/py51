from urllib.request import urlopen

url = "https://quotes.toscrape.com/"
response = urlopen(url)
print(response.status, response.read().decode("utf-8"))