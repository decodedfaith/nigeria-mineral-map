import pandas as pd
import geopandas as gpd
import sys

SAMPLE_DATA = {
    'NAME_1': [
        'Abia', 'Adamawa', 'Akwa Ibom', 'Anambra', 'Bauchi', 'Bayelsa', 'Benue', 'Borno', 'Cross River',
        'Delta', 'Ebonyi', 'Edo', 'Ekiti', 'Enugu', 'Federal Capital Territory', 'Gombe', 'Imo', 'Jigawa',
        'Kaduna', 'Kano', 'Katsina', 'Kebbi', 'Kogi', 'Kwara', 'Lagos', 'Nasarawa', 'Niger', 'Ogun',
        'Ondo', 'Osun', 'Oyo', 'Plateau', 'Rivers', 'Sokoto', 'Taraba', 'Yobe', 'Zamfara'
    ],
    'total': [1, 60, 0, 3, 50, 0, 8, 20, 150, 0, 4, 0, 80, 5, 120, 10, 2, 30, 450, 25, 30, 40, 320, 100, 0, 380, 200, 250, 90, 280, 0, 220, 0, 35, 70, 20, 180],
    'ssml': [1, 50, 0, 2, 40, 0, 6, 15, 120, 0, 3, 0, 60, 4, 90, 8, 1, 25, 350, 20, 25, 30, 250, 80, 0, 300, 150, 200, 70, 220, 0, 180, 0, 30, 50, 15, 140],
    'ml': [0, 5, 0, 1, 5, 0, 1, 3, 20, 0, 1, 0, 15, 1, 20, 1, 1, 3, 80, 3, 3, 5, 50, 15, 0, 60, 30, 40, 15, 50, 0, 30, 0, 3, 15, 3, 30],
    'ql': [0, 5, 0, 0, 5, 0, 1, 2, 10, 0, 0, 0, 5, 0, 10, 1, 0, 2, 20, 2, 2, 5, 20, 5, 0, 20, 20, 10, 5, 10, 0, 10, 0, 2, 5, 2, 10]
}

def prepare_data(source='sample') -> pd.DataFrame:
    """Prepare data (sample or API). Returns DataFrame."""
    if source == 'sample':
        return pd.DataFrame(SAMPLE_DATA)
    # TODO: For 'api', fetch from real endpoint, e.g., requests.get(...)
    raise ValueError("Unsupported data source. Use 'sample' or implement 'api'.")

def merge_and_process(gdf: gpd.GeoDataFrame, data_df: pd.DataFrame) -> gpd.GeoDataFrame:
    """Merge data and compute popup HTML."""
    try:
        print("Merging data...")
        gdf = gdf.merge(data_df, on='NAME_1', how='left').fillna(0)
        print("Data merged successfully!")
        
        # Compute optimized popup HTML
        gdf['popup_html'] = gdf.apply(lambda row: f"""
        <div style="
            min-width: 260px; 
            font-family: 'Inter', sans-serif; 
            color: #eee;
        ">
            <div style="
                border-bottom: 1px solid rgba(255,255,255,0.1); 
                padding-bottom: 10px; 
                margin-bottom: 10px;
                display: flex;
                justify-content: space-between;
                align-items: center;
            ">
                <h4 style="margin: 0; font-size: 18px; font-weight: 600; letter-spacing: 0.5px;">{row['NAME_1']}</h4>
                <span style="
                    background: rgba(255,255,255,0.1); 
                    padding: 2px 8px; 
                    border-radius: 10px; 
                    font-size: 11px; 
                    color: #aaa;
                ">State</span>
            </div>
            
            <div style="margin-bottom: 15px;">
                <p style="margin: 0; font-size: 12px; color: #aaa; text-transform: uppercase; letter-spacing: 1px;">Total Valid Licenses</p>
                <p style="margin: 2px 0 0 0; font-size: 24px; font-weight: 700; color: #fff;">{int(row['total'])}</p>
            </div>
            
            <div style="background: rgba(255,255,255,0.05); border-radius: 8px; padding: 10px; border: 1px solid rgba(255,255,255,0.05);">
                <div style="display: flex; justify-content: space-between; margin-bottom: 8px; font-size: 13px;">
                    <span style="color: #ccc;">Small Scale Mining</span>
                    <span style="font-weight: 600; color: #fff;">{int(row['ssml'])}</span>
                </div>
                <div style="display: flex; justify-content: space-between; margin-bottom: 8px; font-size: 13px;">
                    <span style="color: #ccc;">Mining Lease</span>
                    <span style="font-weight: 600; color: #fff;">{int(row['ml'])}</span>
                </div>
                <div style="display: flex; justify-content: space-between; font-size: 13px;">
                    <span style="color: #ccc;">Quarry License</span>
                    <span style="font-weight: 600; color: #fff;">{int(row['ql'])}</span>
                </div>
            </div>
            <p style="margin: 15px 0 0; font-size: 10px; color: #666; text-align: right;">Data: NMCO (Q1 2022)</p>
        </div>
        """, axis=1)
        return gdf
    except Exception as e:
        print(f"Error merging data: {e}")
        sys.exit(1)
