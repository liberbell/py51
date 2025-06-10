import requests
import json

# resp = requests.delete("https://www.httpbin.org/delete")
# print(resp.json())

# resp = requests.patch("https://www.httpbin.org/patch")
# print(resp.json())

# resp = requests.put("https://www.httpbin.org/put")
# print(resp.json())

resp = requests.post("https://www.httpbin.org/post", data={"key1": "value1"})
json_string = json.dumps(resp.json(), indent=2)
print(json_string)
print(resp.request.body)