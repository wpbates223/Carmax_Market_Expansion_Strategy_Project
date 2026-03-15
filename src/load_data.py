import pandas as pd

def load_city_data():
    return pd.read_csv("data/cities.csv")

def load_store_data():
    return pd.read_csv("data/carmax_locations.csv")