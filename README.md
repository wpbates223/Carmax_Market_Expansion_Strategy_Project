# CarMax Market Expansion Strategy Analysis

This project builds a data-driven framework to identify high-opportunity markets for CarMax expansion using demographic, behavorial, and economic data.
<br>
Using clustering and market scoring techniques, the model segments U.S. cities into strategic market categories and identifies where CarMax should prioritize growth.

## Business Questions
- Where are the largest opportunity areas to reach new customers?
- What store format best serves each market?
- What is the expected return on investment (ROI)?
- How will online sales shift infrastructure needs?
- Which regions require additional reconditioning centers?

## Methodology

### 1. Data Integration
- U.S. Census API (median income)
- City-level demographic and behavorial data
- Market features:
    - Population
    - Median income
    - Car Ownership Rate
    - Online Adoption
    - Opportunity Score

### 2. Feature Engineering
- Standardized key variables
- Cleaned and aligned city/state data
- Built composite opportunity score

### 3. Clustering (KMeans)
- Segmented markets into 3 clusters
- Validated using:
    - Elbow Method
    - PCA visualization

### 4. Market Segmentation
![Market Clusters](Visualizations/Market%20Clusters.png)

Markets were grouped into:
- High Opportunity / Urban Core
    - Large population, high income, strong demand
- Growth Markets
    - Mid-size cities with expansion potential
- Emerging / Low-Density
    - Smaller markets with lower short-term ROI

## Key Results
### **Top Opportunity Markets**
![Top 15 Market Opportunity Scores](Visualizations/Top%2015%20Market%20Opportunity%20Scores.png)

![Heatmap](Visualizations/Market%20Strategy%20Heatmap.png)

- San Francisco, CA
- New York, New York
- Seattle, Washingtion

### **Insights**
- Growing mid-size cities offer the best expansion ROI
- Major metros are saturated but remain critical for presence
- Smaller markets show limited short-term return
- Currently, my model favors high-income, digital-first markets
    - These areas are great for CarMax stability, but for expansion, mid-size cities should have a higher ROI.

- TODO: Factor store saturation into analysis in order to weigh major metros vs mid-size cities.

## Model Evaluation
- Elbow Method: Optimal cluster: k=3
![Elbow Method](Visualizations/Elbow%20Method%20for%20Optimal%20Clusters.png)

- PCA Analysis: Clear cluster separation
![PCA Clusters](Visualizations/PCA%20of%20Market%20Clusters.png)


## Tools & Technologies
- Python
- Pandas / NumPy
- Scikit-learn (KMeans, PCA)
- Matplotlib
- Folium (Heatmap)

