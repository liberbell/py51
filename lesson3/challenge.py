import requests

def get_job_for(lat=None, lng=None, results=20):
    if lat is None or lng is None:
        raise ValueError("Latitude and longitude must be provided")
    url = "https://api.higherme.com/classic/jobs?page=1&includes=location,location.company,location.externalServiceReferences&limit=24&filters[brand.id]=58bd9e7f472bd&filters[lat]={lat}&filters[lng]={lng}&filters[distance]={20}&sort[distance]=asc"



    headers = {
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36 Edg/137.0.0.0",
        "accept": "*/*",
        "accept-language": "ja,en;q=0.9,en-GB;q=0.8,en-US;q=0.7",
        "accept-encoding": "gzip, deflate, br, zstd",
        "x-session-id": "d8c8dcb0-df44-41d9-a19a-aa865d8f1462",
        "x-forter-token": "5764664add3e44a1a631d8257379ed63_1750980536710_51_UDF43-m4_13ck__tt",
        "x-user-datetime": "2025-06-26T07:45:26+09:00",
        "x-ui-language": "en",
        "x-ui-region": "CA",
        "x-ui-platform": "web",
        "origin": "https://www.timhortons.ca",
        "DNT": "1",
        "connection": "keep-alive",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "content-type": "application/json",
        "TE": "trailers"
    }

    response = requests.get(url, headers=headers)

    print(response.text)

get_job_for(43.6532, -793832, 20)