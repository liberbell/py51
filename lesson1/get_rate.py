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

url2 = "https://api.sunrisesunset.com/json"
params2 = {
    "lat": 43.6532,
    "lng": -79.3832,
    "timezone": "EST",
    "data": "today"
}