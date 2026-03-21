import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

def run_clustering(df, k=3):

    features = df[[
        "population",
        "median_income",
        "car_ownership_rate",
        "online_adoption",
        "opportunity_score"
    ]]

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

        if row["population"] > 1_000_000:
            labels[cluster] = "High Growth Urban"

        elif row["online_adoption"] > 0.55:
            labels[cluster] = "Digital-First Market"

        else:
            labels[cluster] = "Emerging / Low Density"

    df["cluster_label"] = df["cluster"].map(labels)

    return df