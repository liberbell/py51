import configparser

config = configparser.ConfigParser()

config.read("api_key.ini")
key1 = config["Key-Values"]["Key1"]
print(key1)