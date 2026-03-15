# Store Type Recommendation Model: Large Metros -> full stores
#                                  Digital demand -> omni hub 
#                                  Smaller Population -> Pickup Center

def recommend_store_type(row):

    if row["population"] > 1200000:
        return "Full Retail Store"
    
    elif row["online_adoption"] > 0.55:
        return "Omnichannel Hub"
    
    else:
        return "Pickup / Delivery Center"
    
def assign_store_type(df):
    
    df["recommended_store_type"] = df.apply(recommend_store_type, axis=1)

    return df