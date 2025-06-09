import requests

url = "https://quotes.toscrape.com/"
resp = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
print(resp.status_code)
print(resp.content.decode("utf-8"))
print(resp.headers)

url2 = "https://httpbin.org/headers"
resp = requests.get(url2, headers={"User-Agent": "Mozilla/5.0"})
print(resp.json())
print(resp.request, resp.request.headers)