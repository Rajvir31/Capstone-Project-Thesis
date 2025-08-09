import pandas as pd

# Load cleaned S&P 500 data (from your cleaned step)
sp500 = pd.read_csv("sp500_data_cleaned.csv")
sp500['Date'] = pd.to_datetime(sp500['Date']).dt.date

# Load GDELT daily event features
gdelt_df = pd.read_csv("gdelt_features.csv")
gdelt_df['Date'] = pd.to_datetime(gdelt_df['Date']).dt.date

# Merge both datasets on Date
merged = pd.merge(sp500, gdelt_df, how='left', on='Date').fillna(0)

# Create label: 1 if market goes up next day, else 0
merged['Return'] = merged['Close'].pct_change().shift(-1)
merged['Target'] = (merged['Return'] > 0).astype(int)

# Save merged dataset
merged.to_csv("gdelt_sp500.csv", index=False)
print("✅ Merged dataset saved as merged_gdelt_sp500.csv")
