import pandas as pd
from bs4 import BeautifulSoup
import requests
from dataclasses import dataclass

@dataclass
class Stock:
    ticker: str

def get_fx_to_usd(currency):
    url = f"https://www.google.com/finance/quote/{currency}-USD"
    resp = requests.get(url)
    if resp.status_code == 200:
        soup = BeautifulSoup(resp.content, "html.parser")
        fx_rate = soup.find("div", {"data-last-price": True})
        fx = float(fx_rate["data-last-price"])
        return fx
    else:
        print("Request failed.")

def get_price_information(ticker, exchange):
    # url = "https://www.google.com/finance/quote/HPE:NYSE?authuser=0"
    url = f"https://www.google.com/finance/quote/{ticker}:{exchange}?authuser=0"

    resp = requests.get(url)
    if resp.status_code == 200:
        soup = BeautifulSoup(resp.content, "html.parser")
        price_div = soup.find("div", attrs={'data-last-price': True})
        price = float(price_div["data-last-price"])
        currency = price_div["data-currency-code"]

        price_usd = price
        if currency != "USD":
            price_usd = round(price * get_fx_to_usd(currency), 2)

        return {
            "ticker": ticker,
            "exchange": exchange,
            "price": price,
            "currency": currency,
            "usd_price": price_usd
        }
    else:
        print("Request failed.")
    

if __name__ == "__main__":
    # print(get_price_information("HPE", "NYSE"))
    # print(get_price_information("MSFT", "NASDAQ"))
    print(get_price_information("SHOP", "TSE"))
    print(get_price_information("SHOP", "NASDAQ"))
    # print(get_price_information("NTT", "TYO"))
    # print(get_fx_to_usd("CAD"))