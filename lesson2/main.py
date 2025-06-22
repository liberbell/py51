import pandas as pd
from bs4 import BeautifulSoup
import requests

def get_fx_to_usd(currency):
    url = f"https://www.google.com/finance/quote/{currency}-USD"
    
def get_price_information(ticker, exchange):
    # url = "https://www.google.com/finance/quote/HPE:NYSE?authuser=0"
    url = f"https://www.google.com/finance/quote/{ticker}:{exchange}?authuser=0"

    resp = requests.get(url)
    if resp.status_code == 200:
        soup = BeautifulSoup(resp.content, "html.parser")
        price_div = soup.find("div", attrs={'data-last-price': True})
        price = float(price_div["data-last-price"])
        currency = price_div["data-currency-code"]

        return {
            "ticker": ticker,
            "exchange": exchange,
            "price": price,
            "currency": currency
        }
    else:
        print("Request failed.")
    

if __name__ == "__main__":
    print(get_price_information("HPE", "NYSE"))
    print(get_price_information("MSFT", "NASDAQ"))
    print(get_price_information("SHOP", "TSE"))
    print(get_price_information("NTT", "TYO"))