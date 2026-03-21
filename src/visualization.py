import matplotlib.pyplot as plt

def plot_opportunities(df):

    df_sorted = df.sort_values("opportunity_score", ascending=False)

    plt.figure(figsize=(10, 6))
    plt.bar(df_sorted["city"], df_sorted["opportunity_score"])

    plt.title("Market Opportunity Scores")
    plt.xlabel("City")
    plt.ylabel("Opportunity Score")

    plt.show()


def plot_clusters(df):

    plt.figure(figsize=(8, 6))

    for cluster in df["cluster"].unique():
        subset = df[df["cluster"] == cluster]

        plt.scatter(
            subset["population"],
            subset["opportunity_score"],
            label=subset["cluster_label"].iloc[0]
        )

    plt.xlabel("Population")
    plt.ylabel("Opportunity Score")
    plt.title("Market Clusters (Strategy Segmentation)")

    plt.legend()
    plt.show()