import requests

resp = requests.delete("https://www.httpbin.org/delete")
print(resp.json())

resp = requests.patch("https://www.httpbin.org/patch")
print(resp.json())