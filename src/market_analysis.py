# Market Opportunity Model: Estimate relative demand potential

import pandas as pd

def calculate_opportunity_score(df):
    
    df["income_factor"] = df["median_income"] / df["median_income"].max()
    
    df["demand_estimate"] = (
        df["population"]
        * df["car_ownership_rate"]
        * df["income_factor"]
        * df["online_adoption"]
    )

    df["opportunity_score"] = df["demand_estimate"] / df["demand_estimate"].max()

    return df.sort_values("opportunity_score", ascending=False)