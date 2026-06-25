import pandas as pd
from sqlalchemy import create_engine

# Load cleaned data
df = pd.read_csv("data/weather_clean.csv")

# PostgreSQL connection
engine = create_engine(
    "postgresql+psycopg2://postgres:Manikanta123@localhost:5433/weather.db"
)

# Load into database
df.to_sql(
    "weather_data",
    engine,
    if_exists="replace",
    index=False
)

print("Weather data loaded into PostgreSQL successfully!")