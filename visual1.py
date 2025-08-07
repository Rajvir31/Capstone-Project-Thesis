
import pandas as pd
import matplotlib.pyplot as plt

# Load your merged data (this should include Date, Close, EventCount, AvgTone)
df = pd.read_csv("merged_data.csv")
df['Date'] = pd.to_datetime(df['Date'])

# List of known high-impact event dates (Fed meetings, elections, etc.)
important_dates = [
    "2015-12-16",  # Fed raises rates for first time in a decade
    "2016-06-23",  # Brexit vote
    "2016-11-08",  # Trump elected
    "2020-03-11",  # WHO declares COVID-19 pandemic
    "2022-02-24",  # Russia invades Ukraine
    "2023-03-10",  # SVB collapse
    "2023-06-14",  # Fed interest rate decision
    "2023-09-20",
    "2023-12-13"
]

important_dates = pd.to_datetime(important_dates)

# Start plotting
fig, ax1 = plt.subplots(figsize=(14, 6))

# Plot S&P 500 Close prices
ax1.plot(df['Date'], df['Close'], label='S&P 500 Close Price', color='blue')
ax1.set_ylabel('S&P 500 Close Price', color='blue')
ax1.tick_params(axis='y', labelcolor='blue')
ax1.set_title('S&P 500 Movement with Major Global Events')

# Add vertical lines for important dates
for event_date in important_dates:
    ax1.axvline(event_date, color='red', linestyle='--', alpha=0.7, label='High-Impact Event' if event_date == important_dates[0] else "")

# Optional: Overlay event counts or AvgTone
# Uncomment below for a second y-axis
# ax2 = ax1.twinx()
# ax2.plot(df['Date'], df['EventCount'], label='Event Count', color='green', alpha=0.4)
# ax2.set_ylabel('Event Count', color='green')
# ax2.tick_params(axis='y', labelcolor='green')

# Add legend and grid
fig.legend(loc='upper left', bbox_to_anchor=(0.1, 0.9))
ax1.grid(True)
plt.tight_layout()
plt.show()
