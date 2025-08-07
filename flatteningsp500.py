import pandas as pd

# Load the S&P500 CSV with multi-index headers
sp500 = pd.read_csv("sp500_data.csv", header=[0, 1], index_col=0)

# Flatten multi-level columns
sp500.columns = [col[1] for col in sp500.columns]  # Extract just 'Close', 'Open', etc.

# Reset index so Date becomes a column
sp500.reset_index(inplace=True)
sp500 = sp500.rename(columns={'index': 'Date'})  # In case index is unnamed

# Standardize Date format
sp500['Date'] = pd.to_datetime(sp500['Date']).dt.date
sp500.to_csv("sp500_data_cleaned.csv", index=False)
