import requests

url = "https://en.wikipedia.org/wiki/Rare-earth_element"

resp = requests.get(url)
print(resp.status_code)