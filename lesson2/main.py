import pandas as pd
from bs4 import BeautifulSoup
import requests
from dataclasses import dataclass
from tabulate import tabulate

@dataclass
class Stock:
    ticker: str
    exchange: str
    price: float = 0
    currency: str = "USD"
    jpn_price: float = 0

    def __post_init__(self):
        price_info = get_price_information(self.ticker, self.exchange)

        self.price = price_info["price"]
        self.currency = price_info["currency"]
        self.jpn_price = price_info["jpn_price"]

@dataclass
class Position:
    stock: Stock
    quantity: int = 0

@dataclass
class Portfolio:
    positions: list[Position] = None

    def get_total_value(self):
        total_value =0

        for position in self.positions:
            total_value += position.quantity * position.stock.jpn_price

            return total_value

def get_fx_to_jpn(currency):
    url = f"https://www.google.com/finance/quote/{currency}-JPY"
    resp = requests.get(url)
    if resp.status_code == 200:
        soup = BeautifulSoup(resp.content, "html.parser")
        fx_rate = soup.find("div", {"data-last-price": True})
        fx = float(fx_rate["data-last-price"])
        return fx
    else:
        print("Request failed.")

def get_price_information(ticker, exchange):
    url = f"https://www.google.com/finance/quote/{ticker}:{exchange}?authuser=0"

    resp = requests.get(url)
    if resp.status_code == 200:
        soup = BeautifulSoup(resp.content, "html.parser")
        price_div = soup.find("div", attrs={'data-last-price': True})
        price = float(price_div["data-last-price"])
        currency = price_div["data-currency-code"]

        price_jpn = price
        if currency != "JPY":
            price_jpn = round(price * get_fx_to_jpn(currency), 2)

        return {
            "ticker": ticker,
            "exchange": exchange,
            "price": price,
            "currency": currency,
            "jpn_price": price_jpn
        }
    else:
        print("Request failed.")
    
def display_portfolio_summary(portfolio):
    data = []
    if not isinstance(portfolio, Portfolio):
        raise TypeError("Please provide a instance of the Portfolio type.")
    
    portfolio_value = portfolio.get_total_value()

if __name__ == "__main__":
    # print(get_price_information("HPE", "NYSE"))
    # print(get_price_information("MSFT", "NASDAQ"))
    # print(get_price_information("SHOP", "TSE"))
    # print(get_price_information("SHOP", "NASDAQ"))
    # print(get_price_information("NTT", "TYO"))
    # print(get_fx_to_usd("CAD"))
    # print(Stock("HPE", "NYSE"))
    # print(Stock("SHOP", "TSE"))
    shop = Stock("SHOP", "TSE")
    msft = Stock("MSFT", "NASDAQ")
    csco = Stock("CSCO", "NASDAQ")
    portfolio = Portfolio([Position(shop, 10), Position(msft, 10), Position(csco, 10)])
    # print(portfolio.get_total_value())
    display_portfolio_summary(portfolio)