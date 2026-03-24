from src.load_data import load_city_data, load_store_data
from src.market_analysis import calculate_opportunity_score
from src.facility_planning import estimate_reconditioning_need
from src.roi_model import calculate_roi
from src.store_strategy import assign_store_type
from src.visualization import plot_opportunities, plot_clusters
from src.geo_analysis import create_heatmap
from src.clustering import run_clustering, label_clusters
from src.model_evaluation import plot_elbow_method, plot_pca_clusters

def run_pipeline():

    df = load_city_data()

    df = calculate_opportunity_score(df)

    df = run_clustering(df, k=3)

    df = label_clusters(df)

    df = assign_store_type(df)

    df = calculate_roi(df)

    df = estimate_reconditioning_need(df)

    df.to_csv("outputs/opportunity_analysis.csv", index=False)

    plot_opportunities(df)
    plot_clusters(df)

    stores_df = load_store_data()

    create_heatmap(df, stores_df)

    plot_elbow_method(df)
    plot_pca_clusters(df)

    print(df)

if __name__ == "__main__":

    run_pipeline()