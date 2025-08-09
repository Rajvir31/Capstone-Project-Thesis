import pandas as pd
import matplotlib.pyplot as plt

# Load your merged dataset
df = pd.read_csv("merged_data.csv", index_col=0, parse_dates=True)

# Sort by NumEvents and select top N high-event days
top_n = 10  # You can adjust this number
top_event_days = df.sort_values('NumEvents', ascending=False).head(top_n).index

# Plot S&P 500 Close Price
plt.figure(figsize=(14, 6))
plt.plot(df.index, df['Close'], label='S&P 500 Close Price', color='blue')

# Add vertical lines for top high-event days
for date in top_event_days:
    plt.axvline(x=date, color='orange', linestyle='--', alpha=0.7)

# Labels and legend
plt.title('S&P 500 Close Price with Top High-Event Days (from GDELT NumEvents)')
plt.xlabel('Date')
plt.ylabel('S&P 500 Close Price')
plt.legend(['S&P 500 Close Price', 'Top Event Day (NumEvents)'])
plt.grid(True)
plt.tight_layout()
plt.savefig("top_event_days_visual.png")  # Optional: save the figure
plt.show()
