import matplotlib.pyplot as plt

def plot_opportunities(df):

    df_sorted = df.sort_values("opportunity_score", ascending=False).head(15)
    df["city_label"] = df["city"] + ", " + df["state"]

    plt.figure(figsize=(10, 8))
    plt.barh(df_sorted["city"], df_sorted["opportunity_score"])

    plt.title("Top 15 Market Opportunity Scores")
    plt.xlabel("Opportunity Score")
    plt.ylabel("City")

    plt.gca().invert_yaxis()  # Highest score on top
    plt.tight_layout()

    plt.show()


def plot_clusters(df):

    df = df.sort_values("opportunity_score", ascending=False).head(100)
    
    plt.figure(figsize=(10, 6))

    for cluster in df["cluster"].unique():
        subset = df[df["cluster"] == cluster]

        plt.scatter(
            subset["population"],
            subset["opportunity_score"],
            label=subset["cluster_label"].iloc[0],
            alpha=0.7
        )

    plt.xlabel("Population")
    plt.ylabel("Opportunity Score")
    plt.title("Market Clusters (Strategy Segmentation)")

    plt.legend()
    plt.tight_layout()
    plt.show()