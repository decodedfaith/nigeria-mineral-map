import geopandas as gpd
import pandas as pd
import folium
import fiona

# Step 1: Debugging - List available layers
print("Available layers in gadm41_NGA.gpkg:")
print(fiona.listlayers('gadm41_NGA.gpkg'))

# Step 2: Load GeoPackage
try:
    print("Loading GeoPackage...")
    gdf = gpd.read_file('gadm41_NGA.gpkg', layer='ADM_ADM_1')
    if gdf.crs != 'EPSG:4326':
        gdf = gdf.to_crs('EPSG:4326')
    print("GeoPackage loaded successfully!")
    print("State names:", gdf['NAME_1'].tolist())
except Exception as e:
    print(f"Error loading GeoPackage: {e}")
    exit(1)

# Step 3: Prepare sample data (replace with real feed for production)
data = {
    'NAME_1': [
        'Abia', 'Adamawa', 'Akwa Ibom', 'Anambra', 'Bauchi', 'Bayelsa', 'Benue', 'Borno', 'Cross River',
        'Delta', 'Ebonyi', 'Edo', 'Ekiti', 'Enugu', 'Federal Capital Territory', 'Gombe', 'Imo', 'Jigawa',
        'Kaduna', 'Kano', 'Katsina', 'Kebbi', 'Kogi', 'Kwara', 'Lagos', 'Nasarawa', 'Niger', 'Ogun',
        'Ondo', 'Osun', 'Oyo', 'Plateau', 'Rivers', 'Sokoto', 'Taraba', 'Yobe', 'Zamfara'
    ],
    'total': [
        1, 60, 0, 3, 50, 0, 8, 20, 150, 0, 4, 0, 80, 5, 120, 10, 2, 30,
        450, 25, 30, 40, 320, 100, 0, 380, 200, 250, 90, 280, 0, 220, 0, 35, 70, 20, 180
    ],
    'ssml': [
        1, 50, 0, 2, 40, 0, 6, 15, 120, 0, 3, 0, 60, 4, 90, 8, 1, 25,
        350, 20, 25, 30, 250, 80, 0, 300, 150, 200, 70, 220, 0, 180, 0, 30, 50, 15, 140
    ],
    'ml': [
        0, 5, 0, 1, 5, 0, 1, 3, 20, 0, 1, 0, 15, 1, 20, 1, 1, 3,
        80, 3, 3, 5, 50, 15, 0, 60, 30, 40, 15, 50, 0, 30, 0, 3, 15, 3, 30
    ],
    'ql': [
        0, 5, 0, 0, 5, 0, 1, 2, 10, 0, 0, 0, 5, 0, 10, 1, 0, 2,
        20, 2, 2, 5, 20, 5, 0, 20, 20, 10, 5, 10, 0, 10, 0, 2, 5, 2, 10
    ]
}

# Step 4: Merge data with GeoDataFrame
print("Merging data...")
try:
    titles_df = pd.DataFrame(data)
    gdf = gdf.merge(titles_df, on='NAME_1', how='left').fillna(0)
    print("Data merged successfully!")
except Exception as e:
    print(f"Error merging data: {e}")
    exit(1)

# Step 5: Precompute popup HTML with optimized styling
gdf['popup_html'] = gdf.apply(lambda row: f"""
<div style="width: 250px; padding: 10px; font-family: Arial, sans-serif; line-height: 1.5; background: #fff; border-radius: 5px; box-shadow: 0 2px 5px rgba(0,0,0,0.2);">
    <h4 style="margin: 0 0 10px; font-size: 16px; color: #333;"><b>{row['NAME_1']}</b></h4>
    <p style="margin: 5px 0; font-size: 14px;"><strong>Total Valid Licenses:</strong> {int(row['total'])}</p>
    <table style="width: 100%; border-collapse: collapse; font-size: 12px; border: 1px solid #ddd;">
        <tr style="background-color: #f9f9f9;">
            <th style="padding: 5px; border: 1px solid #ddd;">License Type</th>
            <th style="padding: 5px; border: 1px solid #ddd;">Count</th>
        </tr>
        <tr>
            <td style="padding: 5px; border: 1px solid #ddd;">SSML (Small Scale Mining)</td>
            <td style="padding: 5px; border: 1px solid #ddd;">{int(row['ssml'])}</td>
        </tr>
        <tr>
            <td style="padding: 5px; border: 1px solid #ddd;">ML (Mining Lease)</td>
            <td style="padding: 5px; border: 1px solid #ddd;">{int(row['ml'])}</td>
        </tr>
        <tr>
            <td style="padding: 5px; border: 1px solid #ddd;">QL (Quarry License)</td>
            <td style="padding: 5px; border: 1px solid #ddd;">{int(row['ql'])}</td>
        </tr>
    </table>
    <p style="margin: 10px 0 0; font-size: 10px; color: #666; font-style: italic;">Data: Approximate Q1 2022 (NMCO). For real-time, integrate API.</p>
</div>
""", axis=1)

# Step 6: Create base map
m = folium.Map(
    location=[9.0820, 8.6753],
    zoom_start=6,
    tiles='OpenStreetMap',
    control_scale=True
)

# Step 7: Add choropleth layer
folium.Choropleth(
    geo_data=gdf,
    data=gdf,
    columns=['NAME_1', 'total'],
    key_on='feature.properties.NAME_1',
    fill_color='YlOrRd',
    fill_opacity=0.7,
    line_opacity=0.5,
    legend_name='Number of Mineral Licenses',
    nan_fill_color='white',
    nan_fill_opacity=0.2
).add_to(m)

# Step 8: Add GeoJson layer with tooltips, popups, and highlighting
folium.GeoJson(
    gdf,
    style_function=lambda x: {
        'fillColor': 'red' if x['properties']['total'] > 0 else 'white',
        'weight': 1,
        'color': 'black',
        'fillOpacity': 0.3
    },
    highlight_function=lambda x: {
        'weight': 4,
        'color': 'red',
        'fillOpacity': 0.8
    },
    tooltip=folium.GeoJsonTooltip(
        fields=['NAME_1', 'total'],
        aliases=['State:', 'Total Valid Licenses:'],
        localize=True,
        sticky=True,
        labels=True,
        style="font-size: 12px; padding: 5px; background-color: #fff; border-radius: 3px;"
    ),
    popup=folium.GeoJsonPopup(
        fields=['popup_html'],
        aliases=[''],
        style="font-size: 12px; padding: 0;",
        max_width=300,
        sticky=False,
        closeButton=True,
        autoClose=False
    ),
    name='Nigeria States'
).add_to(m)

# Step 9: Add persistent labels
for idx, row in gdf[gdf['total'] > 0].iterrows():
    centroid = row.geometry.centroid
    folium.Marker(
        location=[centroid.y, centroid.x],
        icon=folium.features.DivIcon(
            html=f'<div style="font-size: 10px; font-weight: bold; color: black; text-align: center;background: rgba(255, 255, 255, 0.0); padding: 2px; border-radius: 3px;">{int(row["total"])}</div>',
            icon_size=(30, 30)
        )
    ).add_to(m)

# Step 10: Add custom JavaScript and CSS for highlighting and popup styling
js_code = f"""
<script>
window.addEventListener('load', function() {{
    setTimeout(function() {{
        var container = document.getElementById('{m.get_name()}');
        if (container && container._leaflet_map) {{
            var map = container._leaflet_map;
            var selectedLayer = null;

            function highlightFeature(e) {{
                var layer = e.target;
                if (selectedLayer && selectedLayer !== layer) {{
                    resetHighlight({{target: selectedLayer}});
                }}
                layer.setStyle({{
                    weight: 4,
                    color: 'red',
                    fillOpacity: 0.8
                }});
                layer.bringToFront();
                selectedLayer = layer;
            }}

            function resetHighlight(e) {{
                var layer = e.target;
                layer.setStyle({{
                    weight: 1,
                    color: 'black',
                    fillOpacity: 0.3
                }});
                if (selectedLayer === layer) {{
                    selectedLayer = null;
                }}
            }}

            map.eachLayer(function(layer) {{
                if (layer instanceof L.GeoJSON) {{
                    layer.eachLayer(function(featureLayer) {{
                        featureLayer.on({{
                            mouseover: highlightFeature,
                            mouseout: function(e) {{
                                if (selectedLayer !== e.target) {{
                                    resetHighlight(e);
                                }}
                            }},
                            click: highlightFeature
                        }});
                    }});
                }}
            }});

            map.on('click', function(e) {{
                if (!e.originalEvent.target.closest('.leaflet-interactive')) {{
                    if (selectedLayer) {{
                        resetHighlight({{target: selectedLayer}});
                    }}
                }}
            }});
        }} else {{
            console.error('Map container or _leaflet_map not found.');
        }}
    }}, 100);
}});
</script>

<style>
.leaflet-popup-content-wrapper {{
    border-radius: 5px;
    box-shadow: 0 2px 5px rgba(0,0,0,0.2);
    background: #fff;
}}
.leaflet-popup-close-button {{
    top: 5px !important;
    right: 5px !important;
    font-size: 14px !important;
    color: #333 !important;
    cursor: pointer !important;
    z-index: 1000 !important;
}}
.leaflet-popup-tip {{
    background: #fff !important;
}}
body {{
    margin: 0;
    padding: 0;
    font-family: Arial, sans-serif;
}}
#map {{
    width: 100vw;
    height: 100vh;
}}
</style>
"""

# Inject JS and CSS
m.get_root().html.add_child(folium.Element(js_code))

# Step 11: Add layer control and title
folium.LayerControl().add_to(m)
title_html = """
<div style="position: fixed; top: 10px; left: 50%; transform: translateX(-50%); z-index: 1000; background: rgba(255, 255, 255, 0.9); padding: 10px; border-radius: 5px; box-shadow: 0 2px 5px rgba(0,0,0,0.2);">
    <h3 style="margin: 0; font-size: 20px; text-align: center;"><b>Interactive Mineral Licenses Distribution in Nigeria</b></h3>
</div>
"""
m.get_root().html.add_child(folium.Element(title_html))

# Step 12: Save as index.html for static hosting
print("Saving map to index.html...")
m.save('index.html')
print("Map saved! Ready for deployment on GitHub Pages or Netlify.")
print("To check for errors: Open index.html in a browser, press F12, and view the Console tab.")