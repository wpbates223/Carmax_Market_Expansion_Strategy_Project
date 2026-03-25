# Market Opportunity Model: Estimate relative demand potential
from sklearn.preprocessing import MinMaxScaler
import pandas as pd


def calculate_opportunity_score(df):

    cols = ["population", "median_income", "online_adoption", "store_count"]

    scaler = MinMaxScaler()
    scaled = scaler.fit_transform(df[cols])
    scaled_df = pd.DataFrame(scaled, columns=cols)

    df["opportunity_score"] = (
        0.4 * scaled_df["population"] +
        0.3 * scaled_df["median_income"] +
        0.3 * scaled_df["online_adoption"]
        - 0.5 * scaled_df["store_count"]  
    )

    return df

def add_store_saturation(df, store_df):

    store_counts = (
        store_df.groupby(["city", "state"])
        .size()
        .reset_index(name="store_count")
    )

    df = df.merge(store_counts, on=["city", "state"], how="left")
    df["store_count"] = df["store_count"].fillna(0)

    return df