"""
Nigeria Mineral Map Visualization Tool.

This is the main entry point for the application. It orchestrates the data loading,
processing, and map generation to create an interactive HTML map of Nigeria's
mineral resources distribution.

Usage:
    python main.py
"""

from src.data_loader import list_layers, load_geodataframe
from src.data_processor import prepare_data, merge_and_process
from src.map_builder import build_map
from src.ui_enhancer import enhance_ui

def main():
    """Execute the map generation pipeline."""
    # 1. Load Geospatial Data
    filepath = 'data/gadm41_NGA.gpkg'
    # Optional: print("Available layers:", list_layers(filepath))
    
    gdf = load_geodataframe(filepath)
    
    # 2. Prepare & Merge Data
    # 'sample' uses hardcoded data for MVP. Implement 'api' for real-time data.
    data_df = prepare_data(source='sample')  
    gdf = merge_and_process(gdf, data_df)
    
    # 3. Build & Enhance Map
    m = build_map(gdf)
    m = enhance_ui(m)
    
    # 4. Save Output
    output_file = 'index.html'
    print(f"Saving interactive map to {output_file}...")
    m.save(output_file)
    print("Success! Map saved.")
    print("Open 'index.html' in your browser to view the heatmap.")

if __name__ == "__main__":
    main()