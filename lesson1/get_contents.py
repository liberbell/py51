import requests

resp = requests.delete("https://www.httpbin.org/delete")
print(resp.status_code)