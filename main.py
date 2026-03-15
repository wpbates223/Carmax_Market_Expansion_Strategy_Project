from src.load_data import load_city_data
from src.market_analysis import calculate_opportunity_score
from src.facility_planning import estimate_reconditioning_need
from src.roi_model import calculate_roi
from src.store_strategy import assign_store_type
from src.visualization import plot_opportunities

def run_pipeline():

    df = load_city_data()

    df = calculate_opportunity_score(df)

    df = assign_store_type(df)

    df = calculate_roi(df)

    df = estimate_reconditioning_need(df)

    df.to_csv("outputs/opportunity_analysis.csv", index=False)

    plot_opportunities(df)

    print(df)

if __name__ == "__main__":

    run_pipeline()