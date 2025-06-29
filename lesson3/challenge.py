import requests
import pandas as pd

def get_job_for(lat=None, lng=None, results=20):
    if lat is None or lng is None:
        raise ValueError("Latitude and longitude must be provided")
    url = f"https://api.higherme.com/classic/jobs?page=1&includes=location,location.company,location.externalServiceReferences&limit=24&filters[brand.id]=58bd9e7f472bd&filters[lat]={lat}&filters[lng]={lng}&filters[distance]={results}&sort[distance]=asc"

    headers = {
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36 Edg/137.0.0.0",
        "accept": "application/json, text/plain */*",
        "accept-language": "ja,en-US;q=0.7,en-GB;q=0.8,en;q=0.3",
        "accept-encoding": "gzip, deflate, br",
        "Higherme-Client-Version": "2023.0.2.0a",
        "origin": "https://app.higherme.com",
        "DNT": "1",
        "connection": "keep-alive",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "TE": "trailers"
    }

    response = requests.get(url, headers=headers)

    response_data = response.json()

    df = pd.DataFrame(data = [r.get("attributes") for r in response_data.get("data")],
                   columns=["title", "full_time", "part_time", "requirements", "distance"])

    return df

response_data = get_job_for(43.6532, -79.3832, results=20)
# print(response_data.get("data"))
# for r in response_data.get("data"):
#     data = r.get("attributes")
#     df = pd.DataFrame(data)

#     print(df)

df = pd.DataFrame(data = [r.get("attributes") for r in response_data.get("data")],
                   columns=["title", "full_time", "part_time", "requirements", "distance"])

print(df)
df.to_csv("jobs.csv", index=False)