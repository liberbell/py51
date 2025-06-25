import requests

url = "https://use1-prod-th.rbictg.com/graphql"

payload = {
    "operationName": "GetRestaurants",
    "variables": {"input": {
        "filter": "NEARBY",
        "cordinates": {
            "userLat": 43.447788,
            "userLng": -79.3733,
            "searchRadius": 8000
        }
    }
    }
}