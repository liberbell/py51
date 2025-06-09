import requests

url = "https://quotes.toscrape.com/"
resp = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
print(resp.status_code)
print(resp.content.decode("utf-8"))
print(resp.headers)

url2 = "https://httpbin.org/headers"
print(resp.json())