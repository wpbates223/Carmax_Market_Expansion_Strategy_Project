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

    colors = {
        0: "red",
        1: "blue",
        2: "green",
        3: "purple"
    }

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
        folium.CircleMarker(
            location=[row["lat"], row["lon"]],
            radius=8,
            color=colors.get(row["cluster"], "black"),
            fill=True,
            fill_opacity=0.7,
            popup=(
                f"{row['city']}<br>"
                f"Cluster: {row['cluster_label']}<br>"
                f"Opportunity: {row['opportunity_score']:.2f}<br>"
                f"ROI: {row['roi']:.2f}<br>"
                f"Store Type: {row['recommended_store_type']}"
            )
        ).add_to(m)


    legend_html = """
    <div style="
    position: fixed; 
    bottom: 50px; left: 50px; width: 200px; height: 120px; 
    background-color: white;
    border:2px solid grey; z-index:9999; font-size:14px;
    ">
    &nbsp;<b>Cluster Legend</b><br>
    &nbsp;<i style="color:red;">●</i> High Growth Urban<br>
    &nbsp;<i style="color:blue;">●</i> Digital-First<br>
    &nbsp;<i style="color:green;">●</i> Emerging Markets<br>
    </div>
    """
    m.get_root().html.add_child(folium.Element(legend_html))                            
    

    # Save map
    m.save("outputs/market_heatmap.html")

    print("Heatmap saved to 'outputs/market_heatmap.html'")