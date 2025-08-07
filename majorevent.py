import pandas as pd
import zipfile
import requests
import os
from datetime import datetime, timedelta

# Config
start_date = datetime(2019, 1, 1)
end_date = datetime(2023, 12, 31)
event_codes = {'03', '04', '05', '07', '08', '14'}

output = []  # to collect daily features

os.makedirs("gdelt_tmp", exist_ok=True)

current_date = start_date
while current_date <= end_date:
    yyyymmdd = current_date.strftime("%Y%m%d")
    url = f"http://data.gdeltproject.org/events/{yyyymmdd}.export.CSV.zip"
    zip_path = f"gdelt_tmp/{yyyymmdd}.zip"

    print(f"Processing {yyyymmdd}...")

    try:
        r = requests.get(url, timeout=10)
        if r.status_code != 200:
            print(f"❌ Failed: {url} ({r.status_code})")
            current_date += timedelta(days=1)
            continue

        with open(zip_path, "wb") as f:
            f.write(r.content)

        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            csv_name = zip_ref.namelist()[0]
            zip_ref.extract(csv_name, path="gdelt_tmp")

        df = pd.read_csv(f"gdelt_tmp/{csv_name}", sep="\t", header=None, low_memory=False)

        # Add column names
        df.columns = [f"col{i}" for i in range(len(df.columns))]
        df = df.rename(columns={
            "col1": "SQLDATE",
            "col26": "EventRootCode",
            "col31": "GoldsteinScale",
            "col34": "AvgTone"
        })

        # Filter major events
        major_events = df[df["EventRootCode"].astype(str).isin(event_codes)]

        # Aggregate per day
        if not major_events.empty:
            avg_tone = major_events["AvgTone"].astype(float).mean()
            goldstein = major_events["GoldsteinScale"].astype(float).mean()
            count = len(major_events)
        else:
            avg_tone = 0.0
            goldstein = 0.0
            count = 0

        output.append({
            "Date": current_date.date(),
            "AvgTone": avg_tone,
            "GoldsteinScale": goldstein,
            "NumEvents": count
        })

        # Clean up
        os.remove(zip_path)
        os.remove(f"gdelt_tmp/{csv_name}")

    except Exception as e:
        print(f"❌ Error on {yyyymmdd}: {e}")

    current_date += timedelta(days=1)

# Save final result
final_df = pd.DataFrame(output)
final_df.to_csv("gdelt_features.csv", index=False)
print("✅ Saved all daily features to gdelt_features.csv")
