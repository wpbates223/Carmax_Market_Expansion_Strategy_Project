import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

def plot_elbow_method(df):

    features = df[[
        "population",
        "median_income",
        "car_ownership_rate",
        "online_adoption",
        "opportunity_score"
    ]]

    df = df.dropna(subset=features.columns)
    features = df[features.columns]

    scaler = StandardScaler()
    scaled_features = scaler.fit_transform(features)

    inertia = []

    k_range = range(1, min(10, len(df)))

    for k in k_range:
        kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
        kmeans.fit(scaled_features)
        inertia.append(kmeans.inertia_)

    plt.figure(figsize=(8, 5))
    plt.plot(k_range, inertia, marker='o')
    plt.axvline(x=3, linestyle='--')

    plt.title("Elbow Method for Optimal Clusters")
    plt.xlabel("Number of Clusters (k)")
    plt.ylabel("Inertia (Within-Cluster Sum of Squares)")

    plt.show()

def plot_pca_clusters(df):

    features = df[[
        "population",
        "median_income",
        "car_ownership_rate",
        "online_adoption",
        "opportunity_score"
    ]]

    df = df.dropna(subset=features.columns)
    features = df[features.columns]

    scaler = StandardScaler()
    scaled_features = scaler.fit_transform(features)

    pca = PCA(n_components=2)
    components = pca.fit_transform(scaled_features)

    df["pca1"] = components[:, 0]
    df["pca2"] = components[:, 1]

    plt.figure(figsize=(10, 7))

    for label in df["cluster_label"].unique():
        subset = df[df["cluster_label"] == label]

        plt.scatter(
            subset["pca1"],
            subset["pca2"],
            label=label,
            alpha=0.7
        )

    top_cities = df.sort_values("opportunity_score", ascending=False).head(10)

    # Add city labels for better interpretability
    for _, row in df.iterrows():
        plt.text(row["pca1"], row["pca2"], row["city"], fontsize=9)

    print("Explained variance ratio:", pca.explained_variance_ratio_)

    plt.xlabel(f"PC1 ({pca.explained_variance_ratio_[0]:.2%})")
    plt.ylabel(f"PC2 ({pca.explained_variance_ratio_[1]:.2%})")
    plt.title("PCA of Market Clusters (Strategy Segmentation)")

    plt.legend()
    plt.show()