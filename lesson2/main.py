import pandas as pd
from bs4 import BeautifulSoup
import requests

def get_price_information(ticker, exchange):
    # url = "https://www.google.com/finance/quote/HPE:NYSE?authuser=0"
    url = f"https://www.google.com/finance/quote/{ticker}:{exchange}?authuser=0"

    resp = requests.get(url)
    if resp.status_code == 200:
        soup = BeautifulSoup(resp.content, "html.parser")
        price_div = soup.find("div", attrs={'data-last-price': True})
        price = float(price_div["data-last-price"])
        currency = price_div["data-currency-code"]

        return price, currency
    else:
        print("Request failed.")
    

hpe_share_price = get_price_information("HPE", "NYSE")
print(hpe_share_price)

if __name__ == "__main__":
    print(get_price_information("MSFT", "NASDAQ"))