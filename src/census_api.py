import requests
import pandas as pd

def get_median_income(api_key):

    url = "https://api.census.gov/data/2022/acs/acs5"

    params = {
        "get": "NAME,B19013_001E",
        "for": f"place:*",
        "key": api_key   
    }

    response = requests.get(url, params=params)
    data = response.json()

    data = response.json()

    df = pd.DataFrame(data[1:], columns=data[0])

    # 🔍 DEBUG: Inspect raw API output
    print("\nRAW DATA SAMPLE:")
    print(df.head(10))

    print("\nUNIQUE median_income VALUES:")
    print(df["B19013_001E"].unique()[:20])

    df = pd.DataFrame(data[1:], columns=data[0])

    df.rename(columns={
        "NAME": "city_full",
        "B19013_001E": "median_income"
    }, inplace=True)

    # Convert to numeric
    df["median_income"] = pd.to_numeric(df["median_income"], errors="coerce")

    # REmove Census invalid values
    df.loc[df["median_income"] < 0, "median_income"] = None

    return df

def clean_city_data(df):

    state_map = {
    "Alabama": "AL", "Alaska": "AK", "Arizona": "AZ", "Arkansas": "AR",
    "California": "CA", "Colorado": "CO", "Connecticut": "CT",
    "Delaware": "DE", "Florida": "FL", "Georgia": "GA",
    "Hawaii": "HI", "Idaho": "ID", "Illinois": "IL",
    "Indiana": "IN", "Iowa": "IA", "Kansas": "KS",
    "Kentucky": "KY", "Louisiana": "LA", "Maine": "ME",
    "Maryland": "MD", "Massachusetts": "MA", "Michigan": "MI",
    "Minnesota": "MN", "Mississippi": "MS", "Missouri": "MO",
    "Montana": "MT", "Nebraska": "NE", "Nevada": "NV",
    "New Hampshire": "NH", "New Jersey": "NJ", "New Mexico": "NM",
    "New York": "NY", "North Carolina": "NC", "North Dakota": "ND",
    "Ohio": "OH", "Oklahoma": "OK", "Oregon": "OR",
    "Pennsylvania": "PA", "Rhode Island": "RI",
    "South Carolina": "SC", "South Dakota": "SD",
    "Tennessee": "TN", "Texas": "TX", "Utah": "UT",
    "Vermont": "VT", "Virginia": "VA", "Washington": "WA",
    "West Virginia": "WV", "Wisconsin": "WI", "Wyoming": "WY"
    }

    # Split "city" and "state" safely
    split_cols = df["city_full"].str.split(", ", n=1, expand=True)
    df["city"] = split_cols[0]
    df["state"] = split_cols[1]
    

    # Clear city names
    df["city"] = df["city"].str.replace(r"\s+(city|town|cdp|municipality)$", "", regex=True)
    df["city"] = df["city"].str.strip().str.lower()

    df["state"] = df["state"].map(state_map)

    df = df.dropna(subset=["state"])

    return df


