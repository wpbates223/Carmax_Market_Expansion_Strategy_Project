import pandas as pd

from src.census_api import get_median_income, clean_city_data


def load_city_data():

    df = pd.read_csv("data/cities.csv")

    # Normalize city/state for matching
    df["city"] = df["city"].str.lower().str.strip()
    df["state"] = df["state"].str.strip()

    # --- Pull Census Data ---
    api_key = "0080e39e4b80153ea66061cdf33693873660d673"

    income_df = get_median_income(api_key)
    income_df = clean_city_data(income_df)

    # --- Merge ---
    df = df.merge(
        income_df[["city", "state", "median_income"]],
        on=["city", "state"],
        how="left"
    )

    print(df[["city", "state", "median_income"]].head())

    # --- Feature Engineering ---
    df["car_ownership_rate"] = 0.7 + (
        df["population"] / df["population"].max()
    ) * 0.2

    df["online_adoption"] = (
        df["median_income"] / df["median_income"].max()
    )

    return df

def load_store_data():
    return pd.read_csv("data/carmax_locations.csv")