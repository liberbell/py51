import requests

url = "https://api.coinbase.com/v3/exchange-rates?currency=BTC"
resp = requests.get(url)
print(resp.text)