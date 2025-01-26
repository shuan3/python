from prophet import Prophet
import pandas as pd

# Example data
date_range = pd.date_range(start="2023-01-01", periods=10, freq="D")
data = [10, 12, 11, 13, 150, 10, 9, 8, 10, 12]

df = pd.DataFrame({"ds": date_range, "y": data})

# Fit Prophet
model = Prophet()
model.fit(df)

# Predict
forecast = model.predict(df)

# Flag outliers
df["outlier"] = (df["y"] < forecast["yhat_lower"]) | (df["y"] > forecast["yhat_upper"])
print(df[df["outlier"]])
print(df.head(100))


# c:\users\shanh\appdata\local\programs\python\python312\lib\site-packages
# python -u "d:\Github\test\generator\outlier detection.py"
