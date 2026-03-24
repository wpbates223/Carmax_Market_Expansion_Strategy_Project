import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

def run_clustering(df, k=3):

    feature_cols = [
        "population",
        "median_income",
        "car_ownership_rate",
        "online_adoption",
        "opportunity_score"
    ]

    # Drop NaNs 
    df = df.dropna(subset=feature_cols)

    # Select features
    features = df[feature_cols]

    # Normalize data 
    scaler = StandardScaler()
    scaled_features = scaler.fit_transform(features)

    # Train KMeans model
    kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
    df["cluster"] = kmeans.fit_predict(scaled_features)

    return df


# Add cluster labels
def label_clusters(df):

    cluster_summary = df.groupby("cluster")[[
        "population",
        "median_income",
        "car_ownership_rate",
        "online_adoption",
        "opportunity_score"
    ]].mean()

    labels = {}

    for cluster, row in cluster_summary.iterrows():

        if row["opportunity_score"] == cluster_summary["opportunity_score"].max():
            labels[cluster] = "High Opportunity Market / Urban Core"

        elif row["online_adoption"] == cluster_summary["online_adoption"].max():
            labels[cluster] = "Digital-First Market"

        else:
            labels[cluster] = "Emerging / Low Density"

    df["cluster_label"] = df["cluster"].map(labels)

    return df