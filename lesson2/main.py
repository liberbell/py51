import pandas as pd
from bs4 import BeautifulSoup
import requests

def get_price_information(ticker, exchange):
    url = "https://www.google.com/finance/quote/HPE:NYSE?authuser=0"
    # url = "https://www.google.com/finance/quote/{ticker}:{exchange}?authuser=0"