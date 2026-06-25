import pandas as pd

df = pd.read_csv("data/weather_raw.csv")

df.rename(columns={
    "temperature": "temperature_celsius",
    "humidity": "humidity_percent",
    "wind_speed": "wind_speed_kmh"
}, inplace=True)

df.to_csv("data/weather_clean.csv", index=False)

print("Weather data transformed successfully!")