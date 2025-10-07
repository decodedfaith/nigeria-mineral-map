from src.data_loader import list_layers, load_geodataframe
from src.data_processor import prepare_data, merge_and_process
from src.map_builder import build_map
from src.ui_enhancer import enhance_ui

def main():
    filepath = 'data/gadm41_NGA.gpkg'
    print("Available layers:", list_layers(filepath))
    
    gdf = load_geodataframe(filepath)
    data_df = prepare_data(source='sample')  # Or 'api' in prod
    gdf = merge_and_process(gdf, data_df)
    
    m = build_map(gdf)
    m = enhance_ui(m)
    
    print("Saving map to index.html...")
    m.save('index.html')
    print("Map saved! Open in browser and check Console (F12) for errors.")

if __name__ == "__main__":
    main()