"""
Project Queue — 52 GeoAI, GIS, ML & API projects (1 per week, full year)
Rotates automatically. Never runs out.
"""

import json
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent

PROJECTS = [
    # ── GeoAI / GIS ──────────────────────────────────────────────
    {
        "name": "OpenStreetMap Road Network Analyzer",
        "slug": "osm_road_analyzer",
        "category": "GeoAI",
        "description": "Analyze road networks from OpenStreetMap using graph algorithms to find optimal routes, detect bottlenecks, and compute connectivity metrics for any city.",
        "tech_stack": ["osmnx", "networkx", "geopandas", "folium", "matplotlib"],
        "datasets": ["OpenStreetMap"],
        "difficulty": "intermediate",
        "outputs": ["interactive_map.html", "network_stats.json", "route_analysis.png"]
    },
    {
        "name": "Urban Heat Island Detector",
        "slug": "urban_heat_island",
        "category": "GeoAI",
        "description": "Detect and visualize urban heat islands using satellite LST data and land cover classification. Compare urban vs rural temperature differentials.",
        "tech_stack": ["rasterio", "numpy", "matplotlib", "scikit-learn", "geopandas"],
        "datasets": ["NASA MODIS", "USGS Landsat"],
        "difficulty": "intermediate",
        "outputs": ["heat_map.png", "land_cover_classification.tif", "statistics.csv"]
    },
    {
        "name": "Flood Risk Zone Mapper",
        "slug": "flood_risk_mapper",
        "category": "GeoAI",
        "description": "Map flood risk zones using DEM elevation data, river proximity, and historical flood records. Output interactive risk maps with severity levels.",
        "tech_stack": ["geopandas", "rasterio", "folium", "pandas", "shapely"],
        "datasets": ["USGS DEM", "FEMA Flood Maps", "OpenStreetMap"],
        "difficulty": "intermediate",
        "outputs": ["flood_risk_map.html", "risk_zones.geojson", "report.md"]
    },
    {
        "name": "Wildfire Spread Predictor",
        "slug": "wildfire_predictor",
        "category": "GeoAI",
        "description": "Predict wildfire spread patterns using wind data, terrain slope, aspect, and vegetation type. Simulate fire progression over time.",
        "tech_stack": ["numpy", "rasterio", "scikit-learn", "matplotlib", "geopandas"],
        "datasets": ["NASA FIRMS", "USGS DEM", "NLCD Vegetation"],
        "difficulty": "advanced",
        "outputs": ["spread_simulation.gif", "risk_areas.geojson", "prediction_model.pkl"]
    },
    {
        "name": "Deforestation Rate Calculator",
        "slug": "deforestation_calculator",
        "category": "GeoAI",
        "description": "Calculate deforestation rates from multi-temporal forest cover data. Identify hotspots and compute annual loss rates by region.",
        "tech_stack": ["rasterio", "numpy", "geopandas", "matplotlib", "pandas"],
        "datasets": ["Global Forest Watch", "Hansen Forest Cover"],
        "difficulty": "intermediate",
        "outputs": ["deforestation_map.png", "annual_rates.csv", "hotspots.geojson"]
    },
    {
        "name": "Species Distribution Modeler",
        "slug": "species_distribution",
        "category": "GeoAI",
        "description": "Model species distribution using environmental variables (climate, elevation, land cover) and species occurrence records with MaxEnt-style ML.",
        "tech_stack": ["geopandas", "scikit-learn", "rasterio", "folium", "pandas"],
        "datasets": ["GBIF", "WorldClim", "USGS Elevation"],
        "difficulty": "advanced",
        "outputs": ["distribution_map.html", "habitat_suitability.tif", "model_accuracy.json"]
    },
    {
        "name": "Coastal Erosion Monitor",
        "slug": "coastal_erosion",
        "category": "GeoAI",
        "description": "Monitor coastal erosion patterns by detecting shoreline changes over time using multi-temporal satellite imagery and shapefile analysis.",
        "tech_stack": ["geopandas", "shapely", "rasterio", "folium", "matplotlib"],
        "datasets": ["Landsat Archive", "Sentinel-2", "NOAA Shoreline"],
        "difficulty": "intermediate",
        "outputs": ["shoreline_change_map.html", "erosion_rates.csv", "time_series.png"]
    },
    {
        "name": "Air Quality Spatial Interpolator",
        "slug": "air_quality_interpolation",
        "category": "GeoAI",
        "description": "Interpolate sparse air quality sensor readings across geographic areas using kriging and IDW. Generate continuous pollution surface maps.",
        "tech_stack": ["geopandas", "scipy", "matplotlib", "pandas", "folium"],
        "datasets": ["EPA AQS", "OpenAQ", "PurpleAir"],
        "difficulty": "intermediate",
        "outputs": ["pollution_surface.png", "interpolated.geojson", "validation_report.md"]
    },
    {
        "name": "Earthquake Risk Assessor",
        "slug": "earthquake_risk",
        "category": "GeoAI",
        "description": "Assess seismic risk by analyzing historical earthquake catalogs, fault line proximity, and soil type to generate risk index maps.",
        "tech_stack": ["geopandas", "folium", "pandas", "scikit-learn", "shapely"],
        "datasets": ["USGS Earthquake Catalog", "GEM Fault Database"],
        "difficulty": "intermediate",
        "outputs": ["seismic_risk_map.html", "risk_scores.csv", "fault_buffer_zones.geojson"]
    },
    {
        "name": "Urban Green Space Analyzer",
        "slug": "green_space_analyzer",
        "category": "GeoAI",
        "description": "Analyze urban green space coverage, accessibility per capita, and equity gaps across neighborhoods using parks data and population density.",
        "tech_stack": ["geopandas", "osmnx", "folium", "pandas", "matplotlib"],
        "datasets": ["OpenStreetMap", "Census TIGER", "USGS NLCD"],
        "difficulty": "beginner",
        "outputs": ["green_space_map.html", "equity_report.csv", "coverage_stats.json"]
    },
    {
        "name": "Land Use Change Detector",
        "slug": "land_use_change",
        "category": "GeoAI",
        "description": "Detect land use changes over time using multi-temporal satellite imagery classification. Identify urban expansion, agricultural conversion, and vegetation loss.",
        "tech_stack": ["rasterio", "scikit-learn", "numpy", "matplotlib", "geopandas"],
        "datasets": ["Landsat Time Series", "NLCD"],
        "difficulty": "advanced",
        "outputs": ["change_map.png", "transition_matrix.csv", "classified_images/"]
    },
    {
        "name": "Population Gravity Model",
        "slug": "population_gravity",
        "category": "GeoAI",
        "description": "Model population movement and interaction between cities using gravity models. Predict migration flows and market catchment areas.",
        "tech_stack": ["geopandas", "pandas", "numpy", "folium", "matplotlib"],
        "datasets": ["WorldPop", "Census Data", "OSM Cities"],
        "difficulty": "intermediate",
        "outputs": ["gravity_flows_map.html", "interaction_matrix.csv", "catchment_areas.geojson"]
    },
    {
        "name": "Crop Yield Predictor",
        "slug": "crop_yield_predictor",
        "category": "GeoAI",
        "description": "Predict crop yields using satellite NDVI time series, weather data, and historical harvest records. Train regression models by crop type and region.",
        "tech_stack": ["rasterio", "pandas", "scikit-learn", "matplotlib", "numpy"],
        "datasets": ["MODIS NDVI", "NOAA PRISM", "USDA NASS"],
        "difficulty": "advanced",
        "outputs": ["yield_prediction_map.png", "model_performance.json", "feature_importance.png"]
    },
    {
        "name": "Nighttime Lights Poverty Mapper",
        "slug": "nighttime_poverty_mapper",
        "category": "GeoAI",
        "description": "Map economic development and poverty proxies using NASA nighttime light intensity. Correlate with socioeconomic indicators.",
        "tech_stack": ["rasterio", "geopandas", "folium", "scikit-learn", "pandas"],
        "datasets": ["NASA Black Marble", "World Bank", "UNDP HDI"],
        "difficulty": "intermediate",
        "outputs": ["poverty_proxy_map.html", "development_index.csv", "correlation_analysis.png"]
    },
    {
        "name": "Traffic Accident Hotspot Finder",
        "slug": "accident_hotspot_finder",
        "category": "GeoAI",
        "description": "Identify and visualize traffic accident hotspots using kernel density estimation and spatial clustering of accident records.",
        "tech_stack": ["geopandas", "scipy", "folium", "pandas", "matplotlib"],
        "datasets": ["NHTSA FARS", "UK STATS19", "OpenStreetMap"],
        "difficulty": "beginner",
        "outputs": ["hotspot_map.html", "kde_surface.png", "top_locations.csv"]
    },

    # ── General ML / Data Science ─────────────────────────────────
    {
        "name": "Time Series Anomaly Detector",
        "slug": "timeseries_anomaly",
        "category": "ML",
        "description": "Detect anomalies in multivariate time series using Isolation Forest, LSTM autoencoders, and statistical methods. Compare approaches.",
        "tech_stack": ["pandas", "scikit-learn", "numpy", "matplotlib", "scipy"],
        "datasets": ["UCI Machine Learning", "Synthetic sensor data"],
        "difficulty": "intermediate",
        "outputs": ["anomaly_plot.png", "detected_anomalies.csv", "model_comparison.json"]
    },
    {
        "name": "Customer Churn Predictor",
        "slug": "churn_predictor",
        "category": "ML",
        "description": "Predict customer churn with XGBoost + SHAP explainability. Full pipeline: preprocessing, training, evaluation, feature importance dashboard.",
        "tech_stack": ["scikit-learn", "xgboost", "pandas", "matplotlib", "numpy"],
        "datasets": ["Telco Customer Churn (Kaggle)"],
        "difficulty": "beginner",
        "outputs": ["model.pkl", "shap_summary.png", "evaluation_report.md", "predictions.csv"]
    },
    {
        "name": "Climate Trend Dashboard",
        "slug": "climate_dashboard",
        "category": "ML",
        "description": "Interactive dashboard visualizing global climate trends, anomalies, and projections. Long-term temperature, precipitation, and CO2 analysis.",
        "tech_stack": ["plotly", "dash", "pandas", "requests", "numpy"],
        "datasets": ["NOAA Climate Data", "NASA GISS", "Our World in Data"],
        "difficulty": "intermediate",
        "outputs": ["app.py", "dashboard (localhost:8050)", "trend_analysis.csv"]
    },
    {
        "name": "NLP News Topic Classifier",
        "slug": "news_topic_classifier",
        "category": "ML",
        "description": "Classify news articles into topics using TF-IDF + ML and transformer embeddings. Train on multi-class news dataset with evaluation metrics.",
        "tech_stack": ["scikit-learn", "pandas", "numpy", "matplotlib", "requests"],
        "datasets": ["BBC News Dataset", "AG News"],
        "difficulty": "beginner",
        "outputs": ["classifier.pkl", "confusion_matrix.png", "classification_report.txt"]
    },
    {
        "name": "Geospatial Clustering Engine",
        "slug": "geo_clustering",
        "category": "ML",
        "description": "Cluster geographic points using DBSCAN, K-Means, and HDBSCAN. Compare algorithms on real-world POI and event datasets.",
        "tech_stack": ["scikit-learn", "geopandas", "folium", "pandas", "matplotlib"],
        "datasets": ["OpenStreetMap POIs", "GDELT Events"],
        "difficulty": "beginner",
        "outputs": ["cluster_map.html", "algorithm_comparison.png", "cluster_stats.json"]
    },
    {
        "name": "Satellite Image Classifier",
        "slug": "satellite_classifier",
        "category": "ML",
        "description": "Classify satellite imagery patches into land cover types using CNN with transfer learning. Full training pipeline with data augmentation.",
        "tech_stack": ["numpy", "scikit-learn", "matplotlib", "rasterio", "pillow"],
        "datasets": ["EuroSAT", "UC Merced Land Use"],
        "difficulty": "advanced",
        "outputs": ["model_weights.pkl", "test_accuracy.json", "confusion_matrix.png", "sample_predictions.png"]
    },
    {
        "name": "Housing Price Predictor",
        "slug": "housing_price",
        "category": "ML",
        "description": "Predict housing prices using spatial features + ML regression. Incorporate neighborhood geospatial variables alongside standard features.",
        "tech_stack": ["pandas", "scikit-learn", "geopandas", "matplotlib", "numpy"],
        "datasets": ["Zillow Research", "American Community Survey"],
        "difficulty": "beginner",
        "outputs": ["model.pkl", "spatial_price_map.html", "feature_importance.png"]
    },
    {
        "name": "Renewable Energy Site Selector",
        "slug": "renewable_site_selector",
        "category": "GeoAI",
        "description": "Identify optimal sites for solar and wind energy installation using multi-criteria GIS analysis: irradiance, wind speed, land use, grid proximity.",
        "tech_stack": ["geopandas", "rasterio", "numpy", "folium", "pandas"],
        "datasets": ["NASA POWER", "Global Wind Atlas", "USGS NLCD"],
        "difficulty": "intermediate",
        "outputs": ["optimal_sites_map.html", "site_scores.csv", "criteria_analysis.png"]
    },
    {
        "name": "Supply Chain Network Optimizer",
        "slug": "supply_chain_optimizer",
        "category": "ML",
        "description": "Optimize supply chain networks using graph algorithms and linear programming. Minimize transport costs while meeting demand constraints.",
        "tech_stack": ["networkx", "scipy", "pandas", "matplotlib", "numpy"],
        "datasets": ["Synthetic + real logistics data"],
        "difficulty": "advanced",
        "outputs": ["optimal_routes.json", "cost_analysis.csv", "network_visualization.png"]
    },
    {
        "name": "Pandemic Spread Simulator",
        "slug": "pandemic_simulator",
        "category": "GeoAI",
        "description": "Simulate disease spread using SIR/SEIR models on geographic networks. Visualize epidemic curves and spatial transmission patterns.",
        "tech_stack": ["numpy", "scipy", "geopandas", "matplotlib", "networkx"],
        "datasets": ["Census Population", "OpenStreetMap Mobility"],
        "difficulty": "intermediate",
        "outputs": ["epidemic_curves.png", "spatial_spread.gif", "simulation_results.csv"]
    },

    # ── Web API / Backend ──────────────────────────────────────────
    {
        "name": "GeoJSON REST API",
        "slug": "geojson_rest_api",
        "category": "API",
        "description": "FastAPI-based REST API for storing, querying, and serving GeoJSON features with spatial filtering, bounding box queries, and PostGIS-ready schema.",
        "tech_stack": ["fastapi", "geopandas", "uvicorn", "shapely", "pydantic"],
        "datasets": ["User-provided GeoJSON"],
        "difficulty": "intermediate",
        "outputs": ["api server", "openapi_docs.json", "tests/", "docker-compose.yml"]
    },
    {
        "name": "Geocoding Microservice",
        "slug": "geocoding_microservice",
        "category": "API",
        "description": "Fast geocoding and reverse geocoding microservice using Nominatim with Redis caching, rate limiting, and batch processing endpoints.",
        "tech_stack": ["fastapi", "requests", "pandas", "uvicorn", "pydantic"],
        "datasets": ["OpenStreetMap Nominatim"],
        "difficulty": "intermediate",
        "outputs": ["api server", "batch_geocoder.py", "cache_layer.py", "tests/"]
    },
    {
        "name": "Routing & Distance API",
        "slug": "routing_api",
        "category": "API",
        "description": "REST API for computing optimal routes, distances, and travel times using OSRM or Valhalla. Supports multi-waypoint and isochrone queries.",
        "tech_stack": ["fastapi", "requests", "geopandas", "shapely", "uvicorn"],
        "datasets": ["OpenStreetMap", "OSRM API"],
        "difficulty": "intermediate",
        "outputs": ["api server", "route_engine.py", "isochrone_generator.py"]
    },
    {
        "name": "Real-Time Weather Dashboard",
        "slug": "weather_dashboard",
        "category": "API",
        "description": "Real-time weather monitoring dashboard with maps, forecasts, and historical comparisons. Fetches from open weather APIs and renders interactive visualizations.",
        "tech_stack": ["plotly", "dash", "requests", "pandas", "folium"],
        "datasets": ["Open-Meteo API", "NOAA", "OpenWeatherMap"],
        "difficulty": "beginner",
        "outputs": ["dashboard app", "weather_fetcher.py", "map_layers.py"]
    },
    {
        "name": "GitHub Activity Analyzer",
        "slug": "github_analyzer",
        "category": "API",
        "description": "Analyze GitHub repository and user activity patterns. Compute contribution metrics, language trends, and commit heatmaps using the GitHub API.",
        "tech_stack": ["requests", "pandas", "matplotlib", "numpy", "plotly"],
        "datasets": ["GitHub REST API"],
        "difficulty": "beginner",
        "outputs": ["activity_report.html", "language_chart.png", "commit_heatmap.png"]
    },

    # ── Advanced GeoAI ────────────────────────────────────────────
    {
        "name": "3D Terrain Visualizer",
        "slug": "terrain_visualizer",
        "category": "GeoAI",
        "description": "Generate interactive 3D terrain visualizations from DEM data with hillshading, contour lines, and overlay layers using Plotly and rasterio.",
        "tech_stack": ["rasterio", "numpy", "plotly", "matplotlib", "geopandas"],
        "datasets": ["USGS 3DEP", "SRTM DEM"],
        "difficulty": "intermediate",
        "outputs": ["3d_terrain.html", "hillshade.png", "contours.geojson"]
    },
    {
        "name": "Water Quality Index Mapper",
        "slug": "water_quality_mapper",
        "category": "GeoAI",
        "description": "Map surface water quality indices using satellite reflectance data and in-situ measurements. Detect algal blooms and turbidity patterns.",
        "tech_stack": ["rasterio", "geopandas", "folium", "numpy", "matplotlib"],
        "datasets": ["Sentinel-2", "EPA Water Quality", "USGS Water Data"],
        "difficulty": "intermediate",
        "outputs": ["water_quality_map.html", "wqi_scores.csv", "temporal_analysis.png"]
    },
    {
        "name": "Solar Irradiance Calculator",
        "slug": "solar_irradiance",
        "category": "GeoAI",
        "description": "Calculate solar irradiance and optimal panel angles for any location using astronomical formulas, terrain shading, and NASA POWER data.",
        "tech_stack": ["numpy", "pandas", "matplotlib", "rasterio", "requests"],
        "datasets": ["NASA POWER", "USGS DEM"],
        "difficulty": "intermediate",
        "outputs": ["irradiance_map.png", "monthly_analysis.csv", "optimal_angles.json"]
    },
    {
        "name": "Noise Pollution Mapper",
        "slug": "noise_pollution_mapper",
        "category": "GeoAI",
        "description": "Model and map urban noise pollution from road traffic, airports, and industry using spatial propagation models and OSM infrastructure data.",
        "tech_stack": ["geopandas", "shapely", "numpy", "folium", "pandas"],
        "datasets": ["OpenStreetMap", "EEA Noise Maps", "Airports"],
        "difficulty": "intermediate",
        "outputs": ["noise_map.html", "exposure_stats.csv", "buffer_analysis.geojson"]
    },
    {
        "name": "Groundwater Level Predictor",
        "slug": "groundwater_predictor",
        "category": "GeoAI",
        "description": "Predict groundwater levels using historical well data, precipitation, and land use variables with spatiotemporal regression models.",
        "tech_stack": ["pandas", "scikit-learn", "geopandas", "matplotlib", "numpy"],
        "datasets": ["USGS NWIS", "NOAA Precipitation", "NLCD"],
        "difficulty": "advanced",
        "outputs": ["prediction_map.html", "model_accuracy.json", "feature_analysis.png"]
    },
    {
        "name": "Public Transit Accessibility Scorer",
        "slug": "transit_accessibility",
        "category": "GeoAI",
        "description": "Score neighborhoods by public transit accessibility using GTFS feed analysis, stop coverage, frequency, and walking distance calculations.",
        "tech_stack": ["geopandas", "pandas", "folium", "shapely", "numpy"],
        "datasets": ["GTFS Feeds", "OpenStreetMap", "Census"],
        "difficulty": "intermediate",
        "outputs": ["accessibility_map.html", "neighborhood_scores.csv", "gap_analysis.png"]
    },
    {
        "name": "Landslide Susceptibility Mapper",
        "slug": "landslide_susceptibility",
        "category": "GeoAI",
        "description": "Map landslide susceptibility using slope, aspect, lithology, land cover, and rainfall data with machine learning classification.",
        "tech_stack": ["rasterio", "geopandas", "scikit-learn", "numpy", "matplotlib"],
        "datasets": ["USGS DEM", "NASA GPM", "ESA CCI Land Cover"],
        "difficulty": "advanced",
        "outputs": ["susceptibility_map.tif", "risk_zones.geojson", "model_roc.png"]
    },
    {
        "name": "Ocean Current Visualizer",
        "slug": "ocean_current_viz",
        "category": "GeoAI",
        "description": "Visualize ocean current patterns, sea surface temperature anomalies, and circulation systems using NOAA and Copernicus Marine data.",
        "tech_stack": ["numpy", "matplotlib", "rasterio", "requests", "pandas"],
        "datasets": ["NOAA OSCAR", "Copernicus Marine", "NASA GHRSST"],
        "difficulty": "intermediate",
        "outputs": ["current_animation.gif", "sst_anomaly_map.png", "circulation_stats.json"]
    },
    {
        "name": "Demographic Change Analyzer",
        "slug": "demographic_analyzer",
        "category": "GeoAI",
        "description": "Analyze demographic changes over census periods. Map population growth, diversity shifts, and income changes at tract level with choropleth maps.",
        "tech_stack": ["geopandas", "pandas", "folium", "matplotlib", "requests"],
        "datasets": ["US Census ACS", "Census TIGER", "World Bank"],
        "difficulty": "beginner",
        "outputs": ["demographic_map.html", "change_analysis.csv", "trend_charts.png"]
    },
    {
        "name": "Crime Pattern Analyzer",
        "slug": "crime_pattern_analyzer",
        "category": "GeoAI",
        "description": "Analyze and predict crime patterns using spatial statistics, temporal analysis, and hotspot detection. Identify high-risk times and locations.",
        "tech_stack": ["geopandas", "scipy", "folium", "pandas", "matplotlib"],
        "datasets": ["Chicago Data Portal", "LAPD Open Data", "UK Police API"],
        "difficulty": "intermediate",
        "outputs": ["crime_hotspot_map.html", "temporal_patterns.png", "prediction_zones.geojson"]
    },
    {
        "name": "Food Desert Identifier",
        "slug": "food_desert_identifier",
        "category": "GeoAI",
        "description": "Identify food deserts by analyzing grocery store accessibility, population density, income levels, and vehicle availability across census tracts.",
        "tech_stack": ["geopandas", "osmnx", "folium", "pandas", "shapely"],
        "datasets": ["USDA Food Access Atlas", "OpenStreetMap", "Census ACS"],
        "difficulty": "beginner",
        "outputs": ["food_desert_map.html", "access_scores.csv", "vulnerability_report.md"]
    },
    {
        "name": "Wind Farm Yield Simulator",
        "slug": "wind_farm_simulator",
        "category": "GeoAI",
        "description": "Simulate wind farm energy yield using turbine specs, wind rose data, wake effect models, and terrain roughness calculations.",
        "tech_stack": ["numpy", "pandas", "matplotlib", "scipy", "rasterio"],
        "datasets": ["Global Wind Atlas", "ERA5 Reanalysis", "USGS DEM"],
        "difficulty": "advanced",
        "outputs": ["yield_estimate.json", "wind_rose.png", "layout_optimizer.py"]
    },
    {
        "name": "Glacier Retreat Monitor",
        "slug": "glacier_retreat_monitor",
        "category": "GeoAI",
        "description": "Monitor glacier retreat rates using multi-temporal satellite imagery. Calculate area loss, volume estimates, and project future retreat timelines.",
        "tech_stack": ["rasterio", "geopandas", "numpy", "matplotlib", "shapely"],
        "datasets": ["Landsat", "Sentinel-2", "RGI Glacier Inventory"],
        "difficulty": "intermediate",
        "outputs": ["retreat_timeline.png", "area_loss_stats.csv", "glacier_polygons.geojson"]
    },
    {
        "name": "Hospital Catchment Area Analyzer",
        "slug": "hospital_catchment",
        "category": "GeoAI",
        "description": "Analyze hospital service catchment areas using drive-time isochrones, population coverage, and healthcare access equity analysis.",
        "tech_stack": ["geopandas", "osmnx", "folium", "pandas", "shapely"],
        "datasets": ["CMS Hospital Data", "OpenStreetMap", "Census Population"],
        "difficulty": "intermediate",
        "outputs": ["catchment_map.html", "coverage_stats.csv", "equity_gaps.geojson"]
    },
    {
        "name": "Air Traffic Pattern Visualizer",
        "slug": "air_traffic_viz",
        "category": "GeoAI",
        "description": "Visualize air traffic patterns, route density, altitude profiles, and delay hotspots using ADS-B and FAA flight data.",
        "tech_stack": ["pandas", "folium", "matplotlib", "numpy", "requests"],
        "datasets": ["OpenSky Network", "FAA ASDI", "FlightAware"],
        "difficulty": "intermediate",
        "outputs": ["traffic_density_map.html", "route_analysis.png", "delay_heatmap.html"]
    },
    {
        "name": "Soil Carbon Stock Estimator",
        "slug": "soil_carbon_estimator",
        "category": "GeoAI",
        "description": "Estimate soil organic carbon stocks using remote sensing indices, climate data, and pedotransfer functions for carbon sequestration accounting.",
        "tech_stack": ["rasterio", "numpy", "geopandas", "matplotlib", "scikit-learn"],
        "datasets": ["SoilGrids", "MODIS", "FAO Soil Data"],
        "difficulty": "advanced",
        "outputs": ["carbon_stock_map.tif", "estimates_by_region.csv", "uncertainty_analysis.png"]
    },
    {
        "name": "Real Estate Market Analyzer",
        "slug": "real_estate_analyzer",
        "category": "GeoAI",
        "description": "Analyze real estate market trends spatially — price per sqft gradients, walkability correlations, school district effects, and investment opportunity zones.",
        "tech_stack": ["geopandas", "pandas", "folium", "scikit-learn", "matplotlib"],
        "datasets": ["Zillow", "Walk Score", "Census", "OpenStreetMap"],
        "difficulty": "intermediate",
        "outputs": ["market_map.html", "price_gradient.png", "opportunity_zones.geojson"]
    },
    {
        "name": "Migration Flow Mapper",
        "slug": "migration_flow_mapper",
        "category": "GeoAI",
        "description": "Map internal and international migration flows using census and IOM data. Visualize directional flows with arc maps and Sankey diagrams.",
        "tech_stack": ["geopandas", "pandas", "folium", "matplotlib", "numpy"],
        "datasets": ["IOM Migration Data", "UN DESA", "US Census Migration"],
        "difficulty": "intermediate",
        "outputs": ["flow_map.html", "sankey_diagram.html", "migration_stats.csv"]
    },
    {
        "name": "Industrial Emissions Tracker",
        "slug": "emissions_tracker",
        "category": "GeoAI",
        "description": "Track and visualize industrial GHG emissions by facility, sector, and region. Compute dispersion models and identify regulatory compliance gaps.",
        "tech_stack": ["geopandas", "pandas", "folium", "matplotlib", "numpy"],
        "datasets": ["EPA GHGRP", "EU ETS", "EDGAR"],
        "difficulty": "intermediate",
        "outputs": ["emissions_map.html", "sector_analysis.csv", "compliance_report.md"]
    },
    {
        "name": "Port & Shipping Lane Analyzer",
        "slug": "shipping_lane_analyzer",
        "category": "GeoAI",
        "description": "Analyze global shipping lanes, port throughput, vessel density, and bottleneck choke points using AIS vessel tracking data.",
        "tech_stack": ["geopandas", "pandas", "folium", "matplotlib", "shapely"],
        "datasets": ["MarineTraffic AIS", "UNCTAD Maritime", "OpenStreetMap Ports"],
        "difficulty": "intermediate",
        "outputs": ["shipping_density_map.html", "port_rankings.csv", "lane_analysis.geojson"]
    },
    {
        "name": "Smart City Sensor Dashboard",
        "slug": "smart_city_dashboard",
        "category": "API",
        "description": "Real-time IoT sensor data dashboard for smart city monitoring — traffic, parking, air quality, noise, and energy consumption on a live map.",
        "tech_stack": ["dash", "plotly", "pandas", "folium", "requests"],
        "datasets": ["Chicago Array of Things", "NYC Open Data", "Synthetic IoT"],
        "difficulty": "intermediate",
        "outputs": ["dashboard app", "sensor_aggregator.py", "alert_system.py"]
    },
    {
        "name": "Terrain Classification Pipeline",
        "slug": "terrain_classification",
        "category": "GeoAI",
        "description": "Classify terrain types (mountains, valleys, plains, ridges) from DEM derivatives using ML feature engineering and spatial cross-validation.",
        "tech_stack": ["rasterio", "numpy", "scikit-learn", "matplotlib", "geopandas"],
        "datasets": ["SRTM DEM", "USGS 3DEP", "MERIT DEM"],
        "difficulty": "advanced",
        "outputs": ["terrain_classes.tif", "classification_report.txt", "feature_maps.png"]
    },
    {
        "name": "Election Results Mapper",
        "slug": "election_mapper",
        "category": "GeoAI",
        "description": "Map and analyze election results at precinct and county level. Swing analysis, turnout patterns, demographic correlations, and cartogram generation.",
        "tech_stack": ["geopandas", "pandas", "folium", "matplotlib", "numpy"],
        "datasets": ["MIT Election Lab", "Harvard Dataverse", "Census"],
        "difficulty": "beginner",
        "outputs": ["election_map.html", "swing_analysis.csv", "demographic_correlation.png"]
    },
    {
        "name": "Biodiversity Hotspot Identifier",
        "slug": "biodiversity_hotspots",
        "category": "GeoAI",
        "description": "Identify global biodiversity hotspots using species richness, endemism rates, and threat indices. Prioritize conservation areas.",
        "tech_stack": ["geopandas", "pandas", "folium", "matplotlib", "rasterio"],
        "datasets": ["GBIF", "IUCN Red List", "Global Forest Watch"],
        "difficulty": "intermediate",
        "outputs": ["hotspot_map.html", "priority_areas.geojson", "richness_analysis.csv"]
    },
]


class ProjectQueue:
    def __init__(self):
        self.queue_file = BASE_DIR / "projects_queue.json"
        self.projects = PROJECTS
        self.load_state()

    def load_state(self):
        if self.queue_file.exists():
            with open(self.queue_file) as f:
                data = json.load(f)
                self.completed = data.get("completed", [])
                self.current_index = data.get("current_index", 0)
        else:
            self.completed = []
            self.current_index = 0
            self.save_state()

    def save_state(self):
        with open(self.queue_file, "w") as f:
            json.dump({
                "completed": self.completed,
                "current_index": self.current_index,
                "total_available": len(self.projects),
                "last_updated": __import__("datetime").datetime.now().isoformat()
            }, f, indent=2)

    def get_next_project(self):
        # Rotate through all projects, then repeat
        idx = self.current_index % len(self.projects)
        project = self.projects[idx]

        self.completed.append({
            "index": idx,
            "name": project["name"],
            "slug": project["slug"],
            "category": project["category"]
        })
        self.current_index += 1
        self.save_state()

        return project

    def peek_upcoming(self, n=5):
        """Preview next N projects"""
        upcoming = []
        for i in range(n):
            idx = (self.current_index + i) % len(self.projects)
            upcoming.append(self.projects[idx])
        return upcoming
