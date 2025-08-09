import yfinance as yf
import pandas as pd

sp500 = yf.download('^GSPC', start='2015-01-01', end='2024-12-31')
sp500.to_csv('sp500_data.csv')
print(sp500.head())

