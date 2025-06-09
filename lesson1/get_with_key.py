import configparser

config = configparser.ConfigParser()

config.read("api_key.ini")
key1 = config["Key-Values"]["Key1"]
print(key1)

url = "https://api.exchange.coinbase.com/files"
headers = {
    "Authorization": f"Bearer {key1}",
    "Content-Type": "application/json"
}
