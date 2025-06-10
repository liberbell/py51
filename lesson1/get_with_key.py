import configparser
import requests

config = configparser.ConfigParser()

config.read("api_key.ini")
key1 = config["Key-Values"]["Key1"]
print(key1)

url = "https://api.exchange.coinbase.com/fills"
headers = {
    "Authorization": f"Bearer {key1}",
    "Content-Type": "application/json"
}
resp = requests.get(url, headers=headers)
print(resp.status_code)

auth = ("user1", "pass1")
url = "https://httpbin.org/basic-auth/user1/pass1"
resp = requests.get(url)
print(resp.status_code)