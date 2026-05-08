from langsmith import traceable
from dotenv import load_dotenv
import os 
import pandas as pd
import yfinance as yf

load_dotenv()

@traceable(name = "connection-test")
def sample_function(a : int, b : int) -> int:
    return a + b 


@traceable(name = "yfinance")
def get_price_history(ticker : str, start : str = "2026-01-01") -> pd.DataFrame:
    stock = yf.Ticker(ticker)
    prices = stock.history(start = start)
    return prices


print(sample_function(10, 11))
print(get_price_history(ticker = "AAPL"))