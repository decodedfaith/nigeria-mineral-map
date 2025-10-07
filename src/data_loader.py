import geopandas as gpd
import fiona
import sys

def list_layers(filepath: str) -> list:
    """Debug: List available layers in GeoPackage."""
    return fiona.listlayers(filepath)

def load_geodataframe(filepath: str, layer_name: str = 'ADM_ADM_1') -> gpd.GeoDataFrame:
    """Load and standardize GeoDataFrame."""
    try:
        print("Loading GeoPackage...")
        gdf = gpd.read_file(filepath, layer=layer_name)
        if gdf.crs != 'EPSG:4326':
            gdf = gdf.to_crs('EPSG:4326')
        print("GeoPackage loaded successfully!")
        print("State names:", gdf['NAME_1'].tolist())
        return gdf
    except Exception as e:
        print(f"Error loading GeoPackage: {e}")
        sys.exit(1)