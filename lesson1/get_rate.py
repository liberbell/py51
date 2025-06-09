import requests

url = "https://api.coinbase.com/v2/exchange-rates?currency=BTC"
resp = requests.get(url)
# print(resp.json()['data']['rates']['USD'])

params = {
    "currency": "BTC",
    "base": "USD"
}

resp = requests.get(url, params=params)
print(resp.json()['data']['rates']['USD'])

url2 = "https://api.sunrisesunset.io/json"
params2 = {
    "lat": 43.6532,
    "lng": -79.3832,
    "timezone": "EST",
    "data": "today"
}

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36"
}

resp2 = requests.get(url2, params=params2, headers=headers)
print(resp2.json())