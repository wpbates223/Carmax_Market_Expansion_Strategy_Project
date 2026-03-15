# Return of Interest Model: Expected revenue, gross profit, ROI

def calculate_roi(df):

    avg_car_price = 25000
    gross_margin = 0.12
    investment_cost = 40000000

    annual_units = (
        df["population"] * 0.002
    )  # Assuming 2% of the population have cars

    revenue = annual_units * avg_car_price

    gross_profit = revenue * gross_margin

    roi = (gross_profit - investment_cost) / investment_cost

    df["annual_units"] = annual_units
    df["revenue"] = revenue
    df["gross_profit"] = gross_profit
    df["roi"] = roi

    return df