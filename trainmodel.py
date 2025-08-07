import pandas as pd
from xgboost import XGBClassifier, plot_importance
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import matplotlib.pyplot as plt

# Load merged data
df = pd.read_csv("merged_data.csv")

# Convert date column
df['Date'] = pd.to_datetime(df['Date'])
df.sort_values('Date', inplace=True)

# Create label: 1 if next day's return is positive, else 0
df['Target'] = (df['Return'] > 0).astype(int)

# Show distribution of targets
print("Target distribution:\n", df['Target'].value_counts())

# Add lag features and rolling averages
df['Lag1'] = df['Return'].shift(1)
df['Lag2'] = df['Return'].shift(2)
df['RollingMean_3'] = df['Return'].rolling(window=3).mean()

# Drop rows with NaNs created by shifting
df.dropna(inplace=True)

# Define feature columns
features = ['GoldsteinScale', 'AvgTone', 'NumEvents', 'Lag1', 'Lag2', 'RollingMean_3']
X = df[features]
y = df['Target']

# Split into train/test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)

# Train model
model = XGBClassifier(use_label_encoder=False, eval_metric='logloss')
model.fit(X_train, y_train)

# Predict and evaluate
y_pred = model.predict(X_test)

print(f"\n✅ Model Accuracy: {accuracy_score(y_test, y_pred)}\n")
print("Classification Report:\n", classification_report(y_test, y_pred))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))

# Plot feature importance
plot_importance(model)
plt.tight_layout()
plt.show()
