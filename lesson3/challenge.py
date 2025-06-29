import requests
import pandas as pd
from pgeocode import Nominatim

def get_job_for(lat=None, lng=None, postal_code=None, results=20):
    if (lat is None or lng is None) and postal_code is None:
        raise ValueError("Latitude and longitude must be provided")
    
    if postal_code is not None:
        nomi = Nominatim("ca")

        geo = nomi.query_postal_code(postal_code)
        lat = geo.latitude
        lng = geo.longitude
    
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

    response = requests.get(url, headers=headers).json()

    df = pd.DataFrame(data = [r.get("attributes") for r in response.get("data")],
                   columns=["title", "full_time", "part_time", "requirements", "distance"])

    return df

response_data = get_job_for(43.6532, -79.3832, results=20)

print(response_data)


response_data = get_job_for(postal_code="m5e", results=20)

print(response_data)

# nomi = .Nominatim("ca")
# print(nomi.query_location("union station"))
# print(nomi.query_location("m5e"))
