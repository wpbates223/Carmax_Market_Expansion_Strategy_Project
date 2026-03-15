# Identify where new reconditioning center may be needed

def estimate_reconditioning_need(df):
    
    recon_capacity_per_center = 120000

    df["vehicles_processed"] = df["annual_units"]

    df["centers_needed"] = df["vehicles_processed"] / recon_capacity_per_center

    return df