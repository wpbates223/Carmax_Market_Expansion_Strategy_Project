import folium
from folium.plugins import HeatMap

def add_store_markers(m, stores_df):

    for _, row in stores_df.iterrows():
        folium.CircleMarker(
            location=[row["lat"], row["lon"]],
            radius=6,
            popup=f"Existing Store: {row['city']}",
            color="blue",
            fill=True
        ).add_to(m)

def create_heatmap(df, stores_df=None):

    # Base map centered in US
    m = folium.Map(location=[37.5, -96], zoom_start=4)

    # Prepare data for heatmap
    heat_data = [
        [row["lat"], row["lon"], row["opportunity_score"]]
        for _, row in df.iterrows()
    ]

    # Add heatmap layer
    HeatMap(heat_data, radius=25).add_to(m)

    # Add stores if provided
    if stores_df is not None:
        add_store_markers(m, stores_df)

    # Add markers with details
    for _, row in df.iterrows():
        folium.Marker(
            location=[row["lat"], row["lon"]],
            popup=(
                f"{row['city']}<br>"
                f"Opportunity Score: {row['opportunity_score']:.2f}<br>"
                f"ROI: {row['roi']:.2f}<br>"
                f"Store Type: {row['recommended_store_type']}"
            )
        ).add_to(m)

    

    # Save map
    m.save("outputs/market_heatmap.html")

    print("Heatmap saved to 'outputs/market_heatmap.html'")