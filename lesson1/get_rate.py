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