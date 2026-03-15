import matplotlib.pyplot as plt

def plot_opportunities(df):

    df_sorted = df.sort_values("opportunity_score", ascending=False)

    plt.figure(figsize=(10, 6))
    plt.bar(df_sorted["city"], df_sorted["opportunity_score"])

    plt.title("Market Opportunity Scores")
    plt.xlabel("City")
    plt.ylabel("Opportunity Score")

    plt.show()