import requests
import pandas as pd

cities = [
    {"city": "Munich", "lat": 48.1351, "lon": 11.5820},
    {"city": "Berlin", "lat": 52.5200, "lon": 13.4050},
    {"city": "Hamburg", "lat": 53.5511, "lon": 9.9937},
    {"city": "Frankfurt", "lat": 50.1109, "lon": 8.6821},
    {"city": "Cologne", "lat": 50.9375, "lon": 6.9603},
    {"city": "Stuttgart", "lat": 48.7758, "lon": 9.1829},
    {"city": "Dusseldorf", "lat": 51.2277, "lon": 6.7735},
    {"city": "Leipzig", "lat": 51.3397, "lon": 12.3731},
    {"city": "Dresden", "lat": 51.0504, "lon": 13.7373},
    {"city": "Nuremberg", "lat": 49.4521, "lon": 11.0767}
]

weather_data = []

for city in cities:

    url = "https://api.open-meteo.com/v1/forecast"

    params = {
        "latitude": city["lat"],
        "longitude": city["lon"],
        "current": "temperature_2m,relative_humidity_2m,wind_speed_10m,weather_code"
    }

    response = requests.get(url, params=params)
    data = response.json()

    weather_code = data["current"]["weather_code"]

    if weather_code == 0:
        condition = "Clear"
    elif weather_code <= 3:
        condition = "Partly Cloudy"
    elif weather_code <= 48:
        condition = "Cloudy"
    elif weather_code <= 67:
        condition = "Rainy"
    else:
        condition = "Stormy"

    weather_data.append({
        "city": city["city"],
        "temperature": data["current"]["temperature_2m"],
        "humidity": data["current"]["relative_humidity_2m"],
        "wind_speed": data["current"]["wind_speed_10m"],
        "weather_condition": condition
    })

df = pd.DataFrame(weather_data)

df.to_csv("data/weather_raw.csv", index=False)

print("Weather data extracted successfully!")