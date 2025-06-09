import requests

url = "https://api.coinbase.com/v2/exchange-rates?currency=BTC"
resp = requests.get(url)
print(resp.json()['data']['rates']['USD'])