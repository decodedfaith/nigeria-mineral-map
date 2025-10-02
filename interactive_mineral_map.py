# import geopandas as gpd
# import pandas as pd
# import folium
# import fiona

# # Step 1: List available layers for debugging
# print("Available layers in gadm41_NGA.gpkg:")
# print(fiona.listlayers('gadm41_NGA.gpkg'))

# # Step 2: Load GeoPackage
# try:
#     print("Loading GeoPackage...")
#     gdf = gpd.read_file('gadm41_NGA.gpkg', layer='ADM_ADM_1')
#     # Ensure CRS is EPSG:4326 for Folium
#     if gdf.crs != 'EPSG:4326':
#         gdf = gdf.to_crs('EPSG:4326')
#     print("GeoPackage loaded successfully!")
#     print("State names:", gdf['NAME_1'].tolist())
# except Exception as e:
#     print(f"Error loading GeoPackage: {e}")
#     exit(1)

# # Step 3: Enhanced data with license breakdowns (sample; replace with real feed)
# data = {
#     'NAME_1': [
#         'Abia', 'Adamawa', 'Akwa Ibom', 'Anambra', 'Bauchi', 'Bayelsa', 'Benue', 'Borno', 'Cross River',
#         'Delta', 'Ebonyi', 'Edo', 'Ekiti', 'Enugu', 'Federal Capital Territory', 'Gombe', 'Imo', 'Jigawa',
#         'Kaduna', 'Kano', 'Katsina', 'Kebbi', 'Kogi', 'Kwara', 'Lagos', 'Nasarawa', 'Niger', 'Ogun',
#         'Ondo', 'Osun', 'Oyo', 'Plateau', 'Rivers', 'Sokoto', 'Taraba', 'Yobe', 'Zamfara'
#     ],
#     'total': [
#         1, 60, 0, 3, 50, 0, 8, 20, 150, 0, 4, 0, 80, 5, 120, 10, 2, 30,
#         450, 25, 30, 40, 320, 100, 0, 380, 200, 250, 90, 280, 0, 220, 0, 35, 70, 20, 180
#     ],
#     'ssml': [
#         1, 50, 0, 2, 40, 0, 6, 15, 120, 0, 3, 0, 60, 4, 90, 8, 1, 25,
#         350, 20, 25, 30, 250, 80, 0, 300, 150, 200, 70, 220, 0, 180, 0, 30, 50, 15, 140
#     ],
#     'ml': [
#         0, 5, 0, 1, 5, 0, 1, 3, 20, 0, 1, 0, 15, 1, 20, 1, 1, 3,
#         80, 3, 3, 5, 50, 15, 0, 60, 30, 40, 15, 50, 0, 30, 0, 3, 15, 3, 30
#     ],
#     'ql': [
#         0, 5, 0, 0, 5, 0, 1, 2, 10, 0, 0, 0, 5, 0, 10, 1, 0, 2,
#         20, 2, 2, 5, 20, 5, 0, 20, 20, 10, 5, 10, 0, 10, 0, 2, 5, 2, 10
#     ]
# }

# # Step 4: Merge data with GeoDataFrame
# print("Merging data...")
# try:
#     titles_df = pd.DataFrame(data)
#     gdf = gdf.merge(titles_df, on='NAME_1', how='left').fillna(0)
#     print("Data merged successfully!")
# except Exception as e:
#     print(f"Error merging data: {e}")
#     exit(1)

# # Step 5: Create base map centered on Nigeria
# m = folium.Map(
#     location=[9.0820, 8.6753],  # Nigeria centroid (lat, lon)
#     zoom_start=6,
#     tiles='OpenStreetMap'
# )

# # Step 6: Add choropleth layer
# folium.Choropleth(
#     geo_data=gdf,
#     data=gdf,
#     columns=['NAME_1', 'total'],
#     key_on='feature.properties.NAME_1',
#     fill_color='YlOrRd',
#     fill_opacity=0.7,
#     line_opacity=0.5,
#     legend_name='Number of Mineral Licenses',
#     nan_fill_color='white',
#     nan_fill_opacity=0.2
# ).add_to(m)

# # Step 7: Add GeoJson layer with tooltips and click handling
# map_id = m.get_name()  # Get dynamic map ID

# # js_code = f"""
# # window.onload = function() {{
# #     var map = {map_id};
# #     var selectedLayer = null;
# #     var breakdownMarkers = {{}};
# #     // Initialize breakdown markers with debug logging
# #     document.querySelectorAll('.breakdown-marker').forEach(function(el) {{
# #         var state = el.getAttribute('data-state');
# #         console.log('Initializing marker for state: ' + state);
# #         breakdownMarkers[state] = el;
# #     }});
# #     console.log('Breakdown markers initialized:', Object.keys(breakdownMarkers));
# #     function highlightFeature(e) {{
# #         var layer = e.target;
# #         // Reset previous selection
# #         if (selectedLayer) {{
# #             selectedLayer.setStyle({{
# #                 weight: 1,
# #                 color: 'black',
# #                 fillOpacity: 0.3
# #             }});
# #             var prevState = selectedLayer.feature.properties.NAME_1;
# #             if (breakdownMarkers[prevState]) {{
# #                 console.log('Hiding marker for: ' + prevState);
# #                 breakdownMarkers[prevState].style.display = 'none';
# #             }}
# #         }}
# #         // Highlight clicked state
# #         layer.setStyle({{
# #             weight: 4,
# #             color: 'red',
# #             fillOpacity: 0.8
# #         }});
# #         selectedLayer = layer;
# #         // Show breakdown marker
# #         var state = layer.feature.properties.NAME_1;
# #         if (breakdownMarkers[state]) {{
# #             console.log('Showing marker for: ' + state);
# #             breakdownMarkers[state].style.display = 'block';
# #         }} else {{
# #             console.log('No marker found for: ' + state);
# #         }}
# #     }}
# #     function resetHighlight(e) {{
# #         if (selectedLayer) {{
# #             selectedLayer.setStyle({{
# #                 weight: 1,
# #                 color: 'black',
# #                 fillOpacity: 0.3
# #             }});
# #             var prevState = selectedLayer.feature.properties.NAME_1;
# #             if (breakdownMarkers[prevState]) {{
# #                 console.log('Hiding marker for: ' + prevState);
# #                 breakdownMarkers[prevState].style.display = 'none';
# #             }}
# #             selectedLayer = null;
# #         }}
# #     }}
# #     map.on('click', resetHighlight);
# # }};
# # """
# # m.get_root().script.add_child(folium.Element(f"<script>{js_code}</script>"))

# # # Add breakdown markers (hidden by default)
# # for idx, row in gdf.iterrows():
# #     total = int(row['total'])
# #     if total > 0:  # Only for states with licenses
# #         try:
# #             centroid = row.geometry.centroid
# #             lat, lon = centroid.y, centroid.x
# #             # Sanitize state name for CSS class
# #             safe_state = row['NAME_1'].replace(' ', '_').replace("'", "")
# #             breakdown_html = f"""
# #             <div class="breakdown-marker" data-state="{row['NAME_1']}" style="width: 180px; font-size: 14px; background: rgba(255, 255, 255, 0.9); padding: 10px; border: 1px solid #333; display: none; z-index: 1000; line-height: 1.5;">
# #                 <b>{row['NAME_1']}</b><br>
# #                 Total: {total}<br>
# #                 SSML: {int(row['ssml'])}<br>
# #                 ML: {int(row['ml'])}<br>
# #                 QL: {int(row['ql'])}
# #             </div>
# #             """
# #             folium.Marker(
# #                 location=[lat, lon],
# #                 icon=folium.features.DivIcon(
# #                     html=breakdown_html,
# #                     icon_size=(180, 120),
# #                     className=f"breakdown-marker-{safe_state}"
# #                 )
# #             ).add_to(m)
# #         except Exception as e:
# #             print(f"Warning: Could not add breakdown marker for {row['NAME_1']}: {e}")



# # Step 7: Add hover tooltips, click popups, and persistent labels
# for idx, row in gdf.iterrows():
#     total = int(row['total'])
#     ssml = int(row['ssml'])
#     ml = int(row['ml'])
#     ql = int(row['ql'])
    
#     # Calculate centroid for labels and popups
#     centroid = row.geometry.centroid
#     lat, lon = centroid.y, centroid.x  # Folium uses lat/lon (y/x)
    
#     # Hover tooltip: State and total licenses
#     tooltip = folium.GeoJsonTooltip(
#         fields=['NAME_1', 'total'],
#         aliases=['State:', 'Total Valid Licenses:'],
#         localize=True,
#         sticky=True,
#         labels=True,
#         style="font-size: 12px; padding: 5px;"
#     )
    
#     # Click popup: Breakdown table
#     popup_html = f"""
#     <div style="width: 250px;">
#         <h4><b>{row['NAME_1']}</b></h4>
#         <p><strong>Total Valid Licenses:</strong> {total}</p>
#         <table border="1" style="width:100%; border-collapse: collapse; font-size: 12px;">
#             <tr><th>License Type</th><th>Count</th></tr>
#             <tr><td>SSML (Small Scale Mining)</td><td>{ssml}</td></tr>
#             <tr><td>ML (Mining Lease)</td><td>{ml}</td></tr>
#             <tr><td>QL (Quarry License)</td><td>{ql}</td></tr>
#         </table>
#         <p><em>Data: Approximate Q1 2022 (NMCO). For real-time, integrate API.</em></p>
#     </div>
#     """
    
#     # Add GeoJson layer for tooltips and popups
#     folium.GeoJson(
#         gdf[gdf['NAME_1'] == row['NAME_1']],
#         style_function=lambda x: {
#             'fillColor': 'red' if x['properties']['total'] > 0 else 'white',
#             'weight': 1,
#             'fillOpacity': 0.3
#         },
#         tooltip=tooltip,
#         popup=folium.Popup(popup_html, max_width=300)
#     ).add_to(m)
    
#     # Add persistent label for total licenses (visible by default)
#     if total > 0:  # Only label states with licenses
#         folium.Marker(
#             location=[lat, lon],
#             icon=folium.features.DivIcon(
#                 html=f'<div style="font-size: 10px; font-weight: bold; color: black; text-align: center;">{total}</div>',
#                 icon_size=(30, 30)
#             )
#         ).add_to(m)

# # Add single GeoJson layer with click event binding
# folium.GeoJson(
#     gdf,
#     style_function=lambda x: {
#         'fillColor': 'red' if x['properties']['total'] > 0 else 'white',
#         'weight': 1,
#         'color': 'black',
#         'fillOpacity': 0.3
#     },
#     highlight_function=lambda x: {
#         'weight': 4,
#         'color': 'red',
#         'fillOpacity': 0.8
#     },
#     tooltip=folium.GeoJsonTooltip(
#         fields=['NAME_1', 'total'],
#         aliases=['State:', 'Total Valid Licenses:'],
#         localize=True,
#         sticky=True,
#         labels=True,
#         style="font-size: 12px; padding: 5px;"
#     ),
#     name='Nigeria States',
#     # Bind click event directly
#     popup=None
# ).add_to(m).add_child(folium.Element(
#     f'<script>{map_id}.eachLayer(function(layer) {{ if (layer.feature && layer.feature.properties.NAME_1) {{ layer.on("click", highlightFeature); }} }});</script>'
# ))

# # # Step 8: Add persistent total labels without background
# # print("Adding persistent total labels...")
# # for idx, row in gdf.iterrows():
# #     total = int(row['total'])
# #     if total > 0:
# #         try:
# #             centroid = row.geometry.centroid
# #             lat, lon = centroid.y, centroid.x + 0.05  # Slight offset to avoid overlap
# #             folium.Marker(
# #                 location=[lat, lon],
# #                 icon=folium.features.DivIcon(
# #                     html=f'<div style="font-size: 10px; font-weight: bold; color: black; text-align: center;">{total}</div>',
# #                     icon_size=(40, 20)
# #                 )
# #             ).add_to(m)
# #         except Exception as e:
# #             print(f"Warning: Could not add total label for {row['NAME_1']}: {e}")

# # Step 9: Add legend and title
# folium.LayerControl().add_to(m)
# title_html = '<h3 align="center" style="font-size:20px"><b>Interactive Mineral Licenses Distribution in Nigeria</b></h3>'
# m.get_root().html.add_child(folium.Element(title_html))

# # Step 10: Save as HTML
# print("Saving interactive map to interactive_mineral_map.html...")
# m.save('interactive_mineral_map.html')
# print("Map saved! Open 'interactive_mineral_map.html' in a browser.")
# print("To check for errors: Open the HTML, press F12, and look at the Console tab.")





# import geopandas as gpd
# import pandas as pd
# import folium
# import fiona

# # Step 1: List available layers for debugging
# print("Available layers in gadm41_NGA.gpkg:")
# print(fiona.listlayers('gadm41_NGA.gpkg'))

# # Step 2: Load GeoPackage
# try:
#     print("Loading GeoPackage...")
#     gdf = gpd.read_file('gadm41_NGA.gpkg', layer='ADM_ADM_1')
#     # Ensure CRS is EPSG:4326 for Folium
#     if gdf.crs != 'EPSG:4326':
#         gdf = gdf.to_crs('EPSG:4326')
#     print("GeoPackage loaded successfully!")
#     print("State names:", gdf['NAME_1'].tolist())
# except Exception as e:
#     print(f"Error loading GeoPackage: {e}")
#     exit(1)

# # Step 3: Enhanced data with license breakdowns (sample; replace with real feed)
# data = {
#     'NAME_1': [
#         'Abia', 'Adamawa', 'Akwa Ibom', 'Anambra', 'Bauchi', 'Bayelsa', 'Benue', 'Borno', 'Cross River',
#         'Delta', 'Ebonyi', 'Edo', 'Ekiti', 'Enugu', 'Federal Capital Territory', 'Gombe', 'Imo', 'Jigawa',
#         'Kaduna', 'Kano', 'Katsina', 'Kebbi', 'Kogi', 'Kwara', 'Lagos', 'Nasarawa', 'Niger', 'Ogun',
#         'Ondo', 'Osun', 'Oyo', 'Plateau', 'Rivers', 'Sokoto', 'Taraba', 'Yobe', 'Zamfara'
#     ],
#     'total': [
#         1, 60, 0, 3, 50, 0, 8, 20, 150, 0, 4, 0, 80, 5, 120, 10, 2, 30,
#         450, 25, 30, 40, 320, 100, 0, 380, 200, 250, 90, 280, 0, 220, 0, 35, 70, 20, 180
#     ],
#     'ssml': [
#         1, 50, 0, 2, 40, 0, 6, 15, 120, 0, 3, 0, 60, 4, 90, 8, 1, 25,
#         350, 20, 25, 30, 250, 80, 0, 300, 150, 200, 70, 220, 0, 180, 0, 30, 50, 15, 140
#     ],
#     'ml': [
#         0, 5, 0, 1, 5, 0, 1, 3, 20, 0, 1, 0, 15, 1, 20, 1, 1, 3,
#         80, 3, 3, 5, 50, 15, 0, 60, 30, 40, 15, 50, 0, 30, 0, 3, 15, 3, 30
#     ],
#     'ql': [
#         0, 5, 0, 0, 5, 0, 1, 2, 10, 0, 0, 0, 5, 0, 10, 1, 0, 2,
#         20, 2, 2, 5, 20, 5, 0, 20, 20, 10, 5, 10, 0, 10, 0, 2, 5, 2, 10
#     ]
# }

# # Step 4: Merge data with GeoDataFrame
# print("Merging data...")
# try:
#     titles_df = pd.DataFrame(data)
#     gdf = gdf.merge(titles_df, on='NAME_1', how='left').fillna(0)
#     print("Data merged successfully!")
# except Exception as e:
#     print(f"Error merging data: {e}")
#     exit(1)

# # Step 5: Create base map centered on Nigeria
# m = folium.Map(
#     location=[9.0820, 8.6753],  # Nigeria centroid (lat, lon)
#     zoom_start=6,
#     tiles='OpenStreetMap'
# )

# # Step 6: Add choropleth layer
# folium.Choropleth(
#     geo_data=gdf,
#     data=gdf,
#     columns=['NAME_1', 'total'],
#     key_on='feature.properties.NAME_1',
#     fill_color='YlOrRd',
#     fill_opacity=0.7,
#     line_opacity=0.5,
#     legend_name='Number of Mineral Licenses',
#     nan_fill_color='white',
#     nan_fill_opacity=0.2
# ).add_to(m)

# # Step 7: Add GeoJson layer with tooltips, popups, and highlighting
# map_id = m.get_name()
# js_code = f"""
# window.onload = function() {{
#     var map = {map_id};
#     var selectedLayer = null;
#     function highlightFeature(e) {{
#         var layer = e.target;
#         // Reset previous selection
#         if (selectedLayer) {{
#             selectedLayer.setStyle({{
#                 weight: 1,
#                 color: 'black',
#                 fillOpacity: 0.3
#             }});
#         }}
#         // Highlight clicked state
#         layer.setStyle({{
#             weight: 4,
#             color: 'red',
#             fillOpacity: 0.8
#         }});
#         selectedLayer = layer;
#     }}
#     function resetHighlight(e) {{
#         if (selectedLayer) {{
#             selectedLayer.setStyle({{
#                 weight: 1,
#                 color: 'black',
#                 fillOpacity: 0.3
#             }});
#             selectedLayer = null;
#         }}
#     }}
#     map.eachLayer(function(layer) {{
#         if (layer.feature && layer.feature.properties.NAME_1) {{
#             layer.on('click', highlightFeature);
#         }}
#     }});
#     map.on('click', resetHighlight);
# }};
# """
# m.get_root().script.add_child(folium.Element(f"<script>{js_code}</script>"))

# # Add single GeoJson layer
# folium.GeoJson(
#     gdf,
#     style_function=lambda x: {
#         'fillColor': 'red' if x['properties']['total'] > 0 else 'white',
#         'weight': 1,
#         'color': 'black',
#         'fillOpacity': 0.3
#     },
#     highlight_function=lambda x: {
#         'weight': 4,
#         'color': 'red',
#         'fillOpacity': 0.8
#     },
#     tooltip=folium.GeoJsonTooltip(
#         fields=['NAME_1', 'total'],
#         aliases=['State:', 'Total Valid Licenses:'],
#         localize=True,
#         sticky=True,
#         labels=True,
#         style="font-size: 12px; padding: 5px;"
#     ),
#     name='Nigeria States',
#     popup=None
# ).add_to(m)

# # Add popups at centroids
# for idx, row in gdf.iterrows():
#     total = int(row['total'])
#     if total > 0:  # Only for states with licenses
#         try:
#             centroid = row.geometry.centroid
#             lat, lon = centroid.y, centroid.x
#             popup_html = f"""
#             <div style="width: 180px; font-size: 14px; background: rgba(255, 255, 255, 0.9); padding: 10px; border: 1px solid #333; line-height: 1.5;">
#                 <b>{row['NAME_1']}</b><br>
#                 Total: {total}<br>
#                 SSML: {int(row['ssml'])}<br>
#                 ML: {int(row['ml'])}<br>
#                 QL: {int(row['ql'])}
#             </div>
#             """
#             folium.Marker(
#                 location=[lat, lon],
#                 popup=folium.Popup(popup_html, max_width=200),
#                 icon=folium.Icon(icon='')  # No icon, just popup
#             ).add_to(m)
#         except Exception as e:
#             print(f"Warning: Could not add popup for {row['NAME_1']}: {e}")

# # Step 8: Add persistent total labels without background
# print("Adding persistent total labels...")
# for idx, row in gdf.iterrows():
#     total = int(row['total'])
#     if total > 0:
#         try:
#             centroid = row.geometry.centroid
#             lat, lon = centroid.y, centroid.x + 0.05  # Offset to avoid overlap
#             folium.Marker(
#                 location=[lat, lon],
#                 icon=folium.features.DivIcon(
#                     html=f'<div style="font-size: 10px; font-weight: bold; color: black; text-align: center;">{total}</div>',
#                     icon_size=(40, 20)
#                 )
#             ).add_to(m)
#         except Exception as e:
#             print(f"Warning: Could not add total label for {row['NAME_1']}: {e}")

# # Step 9: Add legend and title
# folium.LayerControl().add_to(m)
# title_html = '<h3 align="center" style="font-size:20px"><b>Interactive Mineral Licenses Distribution in Nigeria</b></h3>'
# m.get_root().html.add_child(folium.Element(title_html))

# # Step 10: Save as HTML
# print("Saving interactive map to interactive_mineral_map.html...")
# m.save('interactive_mineral_map.html')
# print("Map saved! Open 'interactive_mineral_map.html' in a browser.")
# print("To check for errors: Open the HTML, press F12, and look at the Console tab.")












# import geopandas as gpd
# import pandas as pd
# import folium
# import fiona

# # Step 1: List available layers for debugging
# print("Available layers in gadm41_NGA.gpkg:")
# print(fiona.listlayers('gadm41_NGA.gpkg'))

# # Step 2: Load GeoPackage
# try:
#     print("Loading GeoPackage...")
#     gdf = gpd.read_file('gadm41_NGA.gpkg', layer='ADM_ADM_1')
#     print("GeoPackage loaded successfully!")
#     print("State names:", gdf['NAME_1'].tolist())
# except Exception as e:
#     print(f"Error loading GeoPackage: {e}")
#     exit(1)

# # Step 3: Enhanced data with license breakdowns (sample; replace with real feed)
# data = {
#     'NAME_1': [
#         'Abia', 'Adamawa', 'Akwa Ibom', 'Anambra', 'Bauchi', 'Bayelsa', 'Benue', 'Borno', 'Cross River',
#         'Delta', 'Ebonyi', 'Edo', 'Ekiti', 'Enugu', 'Federal Capital Territory', 'Gombe', 'Imo', 'Jigawa',
#         'Kaduna', 'Kano', 'Katsina', 'Kebbi', 'Kogi', 'Kwara', 'Lagos', 'Nasarawa', 'Niger', 'Ogun',
#         'Ondo', 'Osun', 'Oyo', 'Plateau', 'Rivers', 'Sokoto', 'Taraba', 'Yobe', 'Zamfara'
#     ],
#     'total': [
#         1, 60, 0, 3, 50, 0, 8, 20, 150, 0, 4, 0, 80, 5, 120, 10, 2, 30,
#         450, 25, 30, 40, 320, 100, 0, 380, 200, 250, 90, 280, 0, 220, 0, 35, 70, 20, 180
#     ],
#     'ssml': [
#         1, 50, 0, 2, 40, 0, 6, 15, 120, 0, 3, 0, 60, 4, 90, 8, 1, 25,
#         350, 20, 25, 30, 250, 80, 0, 300, 150, 200, 70, 220, 0, 180, 0, 30, 50, 15, 140
#     ],
#     'ml': [
#         0, 5, 0, 1, 5, 0, 1, 3, 20, 0, 1, 0, 15, 1, 20, 1, 1, 3,
#         80, 3, 3, 5, 50, 15, 0, 60, 30, 40, 15, 50, 0, 30, 0, 3, 15, 3, 30
#     ],
#     'ql': [
#         0, 5, 0, 0, 5, 0, 1, 2, 10, 0, 0, 0, 5, 0, 10, 1, 0, 2,
#         20, 2, 2, 5, 20, 5, 0, 20, 20, 10, 5, 10, 0, 10, 0, 2, 5, 2, 10
#     ]
# }

# # Step 4: Merge data with GeoDataFrame
# print("Merging data...")
# try:
#     titles_df = pd.DataFrame(data)
#     gdf = gdf.merge(titles_df, on='NAME_1', how='left').fillna(0)
#     print("Data merged successfully!")
# except Exception as e:
#     print(f"Error merging data: {e}")
#     exit(1)

# # Step 5: Create base map centered on Nigeria
# m = folium.Map(
#     location=[9.0820, 8.6753],  # Nigeria centroid (lat, lon)
#     zoom_start=6,
#     tiles='OpenStreetMap'
# )

# # Step 6: Add choropleth layer
# folium.Choropleth(
#     geo_data=gdf,
#     data=gdf,
#     columns=['NAME_1', 'total'],
#     key_on='feature.properties.NAME_1',
#     fill_color='YlOrRd',
#     fill_opacity=0.7,
#     line_opacity=0.5,
#     legend_name='Number of Mineral Licenses',
#     nan_fill_color='white',
#     nan_fill_opacity=0.2
# ).add_to(m)

# # Step 7: Add hover tooltips, click popups, and persistent labels
# for idx, row in gdf.iterrows():
#     total = int(row['total'])
#     ssml = int(row['ssml'])
#     ml = int(row['ml'])
#     ql = int(row['ql'])
    
#     # Calculate centroid for labels and popups
#     centroid = row.geometry.centroid
#     lat, lon = centroid.y, centroid.x  # Folium uses lat/lon (y/x)
    
#     # Hover tooltip: State and total licenses
#     tooltip = folium.GeoJsonTooltip(
#         fields=['NAME_1', 'total'],
#         aliases=['State:', 'Total Valid Licenses:'],
#         localize=True,
#         sticky=True,
#         labels=True,
#         style="font-size: 12px; padding: 5px;"
#     )
    
#     # Click popup: Breakdown table
#     popup_html = f"""
#     <div style="width: 250px;">
#         <h4><b>{row['NAME_1']}</b></h4>
#         <p><strong>Total Valid Licenses:</strong> {total}</p>
#         <table border="1" style="width:100%; border-collapse: collapse; font-size: 12px;">
#             <tr><th>License Type</th><th>Count</th></tr>
#             <tr><td>SSML (Small Scale Mining)</td><td>{ssml}</td></tr>
#             <tr><td>ML (Mining Lease)</td><td>{ml}</td></tr>
#             <tr><td>QL (Quarry License)</td><td>{ql}</td></tr>
#         </table>
#         <p><em>Data: Approximate Q1 2022 (NMCO). For real-time, integrate API.</em></p>
#     </div>
#     """
    
#     # Add GeoJson layer for tooltips and popups
#     folium.GeoJson(
#         gdf[gdf['NAME_1'] == row['NAME_1']],
#         style_function=lambda x: {
#             'fillColor': 'red' if x['properties']['total'] > 0 else 'white',
#             'weight': 1,
#             'fillOpacity': 0.3
#         },
#         tooltip=tooltip,
#         popup=folium.Popup(popup_html, max_width=300)
#     ).add_to(m)
    
#     # Add persistent label for total licenses (visible by default)
#     if total > 0:  # Only label states with licenses
#         folium.Marker(
#             location=[lat, lon],
#             icon=folium.features.DivIcon(
#                 html=f'<div style="font-size: 10px; font-weight: bold; color: black; text-align: center;">{total}</div>',
#                 icon_size=(30, 30)
#             )
#         ).add_to(m)

# # Step 8: Add legend and title
# folium.LayerControl().add_to(m)
# title_html = '<h3 align="center" style="font-size:20px"><b>Interactive Mineral Licenses Distribution in Nigeria</b></h3>'
# m.get_root().html.add_child(folium.Element(title_html))

# # Step 9: Save as HTML
# print("Saving interactive map to interactive_mineral_map.html...")
# m.save('interactive_mineral_map.html')
# print("Map saved! Open 'interactive_mineral_map.html' in a browser.")


# import geopandas as gpd
# import pandas as pd
# import folium
# import fiona

# # Step 1: List available layers for debugging
# print("Available layers in gadm41_NGA.gpkg:")
# print(fiona.listlayers('gadm41_NGA.gpkg'))

# # Step 2: Load GeoPackage
# try:
#     print("Loading GeoPackage...")
#     gdf = gpd.read_file('gadm41_NGA.gpkg', layer='ADM_ADM_1')
#     if gdf.crs != 'EPSG:4326':
#         gdf = gdf.to_crs('EPSG:4326')
#     print("GeoPackage loaded successfully!")
#     print("State names:", gdf['NAME_1'].tolist())
# except Exception as e:
#     print(f"Error loading GeoPackage: {e}")
#     exit(1)

# # Step 3: Enhanced data with license breakdowns
# data = {
#     'NAME_1': [
#         'Abia', 'Adamawa', 'Akwa Ibom', 'Anambra', 'Bauchi', 'Bayelsa', 'Benue', 'Borno', 'Cross River',
#         'Delta', 'Ebonyi', 'Edo', 'Ekiti', 'Enugu', 'Federal Capital Territory', 'Gombe', 'Imo', 'Jigawa',
#         'Kaduna', 'Kano', 'Katsina', 'Kebbi', 'Kogi', 'Kwara', 'Lagos', 'Nasarawa', 'Niger', 'Ogun',
#         'Ondo', 'Osun', 'Oyo', 'Plateau', 'Rivers', 'Sokoto', 'Taraba', 'Yobe', 'Zamfara'
#     ],
#     'total': [
#         1, 60, 0, 3, 50, 0, 8, 20, 150, 0, 4, 0, 80, 5, 120, 10, 2, 30,
#         450, 25, 30, 40, 320, 100, 0, 380, 200, 250, 90, 280, 0, 220, 0, 35, 70, 20, 180
#     ],
#     'ssml': [
#         1, 50, 0, 2, 40, 0, 6, 15, 120, 0, 3, 0, 60, 4, 90, 8, 1, 25,
#         350, 20, 25, 30, 250, 80, 0, 300, 150, 200, 70, 220, 0, 180, 0, 30, 50, 15, 140
#     ],
#     'ml': [
#         0, 5, 0, 1, 5, 0, 1, 3, 20, 0, 1, 0, 15, 1, 20, 1, 1, 3,
#         80, 3, 3, 5, 50, 15, 0, 60, 30, 40, 15, 50, 0, 30, 0, 3, 15, 3, 30
#     ],
#     'ql': [
#         0, 5, 0, 0, 5, 0, 1, 2, 10, 0, 0, 0, 5, 0, 10, 1, 0, 2,
#         20, 2, 2, 5, 20, 5, 0, 20, 20, 10, 5, 10, 0, 10, 0, 2, 5, 2, 10
#     ]
# }

# # Step 4: Merge data with GeoDataFrame
# print("Merging data...")
# try:
#     titles_df = pd.DataFrame(data)
#     gdf = gdf.merge(titles_df, on='NAME_1', how='left').fillna(0)
#     print("Data merged successfully!")
# except Exception as e:
#     print(f"Error merging data: {e}")
#     exit(1)

# # Step 5: Create base map centered on Nigeria
# m = folium.Map(
#     location=[9.0820, 8.6753],
#     zoom_start=6,
#     tiles='OpenStreetMap'
# )

# # Step 6: Add choropleth layer
# folium.Choropleth(
#     geo_data=gdf,
#     data=gdf,
#     columns=['NAME_1', 'total'],
#     key_on='feature.properties.NAME_1',
#     fill_color='YlOrRd',
#     fill_opacity=0.7,
#     line_opacity=0.5,
#     legend_name='Number of Mineral Licenses',
#     nan_fill_color='white',
#     nan_fill_opacity=0.2
# ).add_to(m)

# # Step 7: Add GeoJson layer with tooltips, popups, and highlight functionality
# map_id = m.get_name()

# # JavaScript for highlighting and resetting
# js_code = f"""
# var selectedLayer = null;
# function highlightFeature(e) {{
#     var layer = e.target;
#     if (selectedLayer && selectedLayer !== layer) {{
#         selectedLayer.setStyle({{
#             weight: 1,
#             color: 'black',
#             fillOpacity: 0.3
#         }});
#     }}
#     layer.setStyle({{
#         weight: 4,
#         color: 'red',
#         fillOpacity: 0.8
#     }});
#     selectedLayer = layer;
#     layer.bringToFront(); // Ensure highlighted layer is on top
# }}
# function resetHighlight(e) {{
#     if (selectedLayer) {{
#         selectedLayer.setStyle({{
#             weight: 1,
#             color: 'black',
#             fillOpacity: 0.3
#         }});
#         selectedLayer = null;
#     }}
# }}
# var map = {map_id};
# map.on('click', function(e) {{
#     if (!e.originalEvent.target.closest('.leaflet-interactive')) {{
#         resetHighlight(e);
#     }}
# }});
# """

# # Add GeoJson layer with tooltips, popups, and click events
# for idx, row in gdf.iterrows():
#     total = int(row['total'])
#     ssml = int(row['ssml'])
#     ml = int(row['ml'])
#     ql = int(row['ql'])
    
#     # Calculate centroid for labels
#     centroid = row.geometry.centroid
#     lat, lon = centroid.y, centroid.x
    
#     # Popup HTML
#     popup_html = f"""
#     <div style="width: 250px;">
#         <h4><b>{row['NAME_1']}</b></h4>
#         <p><strong>Total Valid Licenses:</strong> {total}</p>
#         <table border="1" style="width:100%; border-collapse: collapse; font-size: 12px;">
#             <tr><th>License Type</th><th>Count</th></tr>
#             <tr><td>SSML (Small Scale Mining)</td><td>{ssml}</td></tr>
#             <tr><td>ML (Mining Lease)</td><td>{ml}</td></tr>
#             <tr><td>QL (Quarry License)</td><td>{ql}</td></tr>
#         </table>
#         <p><em>Data: Approximate Q1 2022 (NMCO). For real-time, integrate API.</em></p>
#     </div>
#     """
    
#     # Add GeoJson layer for each state
#     folium.GeoJson(
#         gdf[gdf['NAME_1'] == row['NAME_1']],
#         style_function=lambda x: {
#             'fillColor': 'red' if x['properties']['total'] > 0 else 'white',
#             'weight': 1,
#             'color': 'black',
#             'fillOpacity': 0.3
#         },
#         highlight_function=lambda x: {
#             'weight': 4,
#             'color': 'red',
#             'fillOpacity': 0.8
#         },
#         tooltip=folium.GeoJsonTooltip(
#             fields=['NAME_1', 'total'],
#             aliases=['State:', 'Total Valid Licenses:'],
#             localize=True,
#             sticky=True,
#             labels=True,
#             style="font-size: 12px; padding: 5px;"
#         ),
#         popup=folium.Popup(popup_html, max_width=300)
#     ).add_to(m).add_child(folium.Element(
#         f'<script>var layer = this; layer.on("click", highlightFeature);</script>'
#     ))
    
#     # Add persistent label for total licenses
#     if total > 0:
#         folium.Marker(
#             location=[lat, lon],
#             icon=folium.features.DivIcon(
#                 html=f'<div style="font-size: 10px; font-weight: bold; color: black; text-align: center;">{total}</div>',
#                 icon_size=(30, 30)
#             )
#         ).add_to(m)

# # Add JavaScript to map
# m.get_root().script.add_child(folium.Element(f"<script>{js_code}</script>"))

# # Step 8: Add legend and title
# folium.LayerControl().add_to(m)
# title_html = '<h3 align="center" style="font-size:20px"><b>Interactive Mineral Licenses Distribution in Nigeria</b></h3>'
# m.get_root().html.add_child(folium.Element(title_html))

# # Step 9: Save as HTML
# print("Saving interactive map to interactive_mineral_map.html...")
# m.save('interactive_mineral_map.html')
# print("Map saved! Open 'interactive_mineral_map.html' in a browser.")
# print("To check for errors: Open the HTML, press F12, and look at the Console tab.")

# import geopandas as gpd
# import pandas as pd
# import folium
# import fiona

# # Step 1: List available layers for debugging
# print("Available layers in gadm41_NGA.gpkg:")
# print(fiona.listlayers('gadm41_NGA.gpkg'))

# # Step 2: Load GeoPackage
# try:
#     print("Loading GeoPackage...")
#     gdf = gpd.read_file('gadm41_NGA.gpkg', layer='ADM_ADM_1')
#     if gdf.crs != 'EPSG:4326':
#         gdf = gdf.to_crs('EPSG:4326')
#     print("GeoPackage loaded successfully!")
#     print("State names:", gdf['NAME_1'].tolist())
# except Exception as e:
#     print(f"Error loading GeoPackage: {e}")
#     exit(1)

# # Step 3: Enhanced data with license breakdowns
# data = {
#     'NAME_1': [
#         'Abia', 'Adamawa', 'Akwa Ibom', 'Anambra', 'Bauchi', 'Bayelsa', 'Benue', 'Borno', 'Cross River',
#         'Delta', 'Ebonyi', 'Edo', 'Ekiti', 'Enugu', 'Federal Capital Territory', 'Gombe', 'Imo', 'Jigawa',
#         'Kaduna', 'Kano', 'Katsina', 'Kebbi', 'Kogi', 'Kwara', 'Lagos', 'Nasarawa', 'Niger', 'Ogun',
#         'Ondo', 'Osun', 'Oyo', 'Plateau', 'Rivers', 'Sokoto', 'Taraba', 'Yobe', 'Zamfara'
#     ],
#     'total': [
#         1, 60, 0, 3, 50, 0, 8, 20, 150, 0, 4, 0, 80, 5, 120, 10, 2, 30,
#         450, 25, 30, 40, 320, 100, 0, 380, 200, 250, 90, 280, 0, 220, 0, 35, 70, 20, 180
#     ],
#     'ssml': [
#         1, 50, 0, 2, 40, 0, 6, 15, 120, 0, 3, 0, 60, 4, 90, 8, 1, 25,
#         350, 20, 25, 30, 250, 80, 0, 300, 150, 200, 70, 220, 0, 180, 0, 30, 50, 15, 140
#     ],
#     'ml': [
#         0, 5, 0, 1, 5, 0, 1, 3, 20, 0, 1, 0, 15, 1, 20, 1, 1, 3,
#         80, 3, 3, 5, 50, 15, 0, 60, 30, 40, 15, 50, 0, 30, 0, 3, 15, 3, 30
#     ],
#     'ql': [
#         0, 5, 0, 0, 5, 0, 1, 2, 10, 0, 0, 0, 5, 0, 10, 1, 0, 2,
#         20, 2, 2, 5, 20, 5, 0, 20, 20, 10, 5, 10, 0, 10, 0, 2, 5, 2, 10
#     ]
# }

# # Step 4: Merge data with GeoDataFrame
# print("Merging data...")
# try:
#     titles_df = pd.DataFrame(data)
#     gdf = gdf.merge(titles_df, on='NAME_1', how='left').fillna(0)
#     print("Data merged successfully!")
# except Exception as e:
#     print(f"Error merging data: {e}")
#     exit(1)

# # Step 5: Add popup_html column for popups
# gdf['popup_html'] = gdf.apply(lambda row: f"""
# <div style="width: 250px;">
#     <h4><b>{row['NAME_1']}</b></h4>
#     <p><strong>Total Valid Licenses:</strong> {int(row['total'])}</p>
#     <table border="1" style="width:100%; border-collapse: collapse; font-size: 12px;">
#         <tr><th>License Type</th><th>Count</th></tr>
#         <tr><td>SSML (Small Scale Mining)</td><td>{int(row['ssml'])}</td></tr>
#         <tr><td>ML (Mining Lease)</td><td>{int(row['ml'])}</td></tr>
#         <tr><td>QL (Quarry License)</td><td>{int(row['ql'])}</td></tr>
#     </table>
#     <p><em>Data: Approximate Q1 2022 (NMCO). For real-time, integrate API.</em></p>
# </div>
# """, axis=1)

# # Step 6: Create base map centered on Nigeria
# m = folium.Map(
#     location=[9.0820, 8.6753],
#     zoom_start=6,
#     tiles='OpenStreetMap'
# )

# # Step 7: Add choropleth layer
# folium.Choropleth(
#     geo_data=gdf,
#     data=gdf,
#     columns=['NAME_1', 'total'],
#     key_on='feature.properties.NAME_1',
#     fill_color='YlOrRd',
#     fill_opacity=0.7,
#     line_opacity=0.5,
#     legend_name='Number of Mineral Licenses',
#     nan_fill_color='white',
#     nan_fill_opacity=0.2
# ).add_to(m)

# # Step 8: Add GeoJson layer with popups and highlighting
# geojson_layer = folium.GeoJson(
#     gdf,
#     style_function=lambda x: {
#         'fillColor': 'red' if x['properties']['total'] > 0 else 'white',
#         'weight': 1,
#         'color': 'black',
#         'fillOpacity': 0.3
#     },
#     highlight_function=lambda x: {
#         'weight': 4,
#         'color': 'red',
#         'fillOpacity': 0.8
#     },
#     tooltip=folium.GeoJsonTooltip(
#         fields=['NAME_1', 'total'],
#         aliases=['State:', 'Total Valid Licenses:'],
#         localize=True,
#         sticky=True,
#         labels=True,
#         style="font-size: 12px; padding: 5px;"
#     ),
#     popup=folium.GeoJsonPopup(
#         fields=['popup_html'],
#         aliases=[''],
#         style="font-size: 12px; padding: 5px;",
#         max_width=300
#     ),
#     name='Nigeria States'
# ).add_to(m)

# # Step 9: Add persistent labels
# for idx, row in gdf.iterrows():
#     total = int(row['total'])
#     if total > 0:
#         centroid = row.geometry.centroid
#         lat, lon = centroid.y, centroid.x
#         folium.Marker(
#             location=[lat, lon],
#             icon=folium.features.DivIcon(
#                 html=f'<div style="font-size: 10px; font-weight: bold; color: black; text-align: center;">{total}</div>',
#                 icon_size=(30, 30)
#             )
#         ).add_to(m)

# # Step 10: Add JavaScript for highlighting (click and hover)
# js_code = f"""
# <script>
# function setupMapInteractions() {{
#     var map = L.map('{m.get_name()}');
#     var selectedLayer = null;

#     function highlightFeature(e) {{
#         var layer = e.target;
#         if (selectedLayer && selectedLayer !== layer) {{
#             selectedLayer.setStyle({{
#                 weight: 1,
#                 color: 'black',
#                 fillOpacity: 0.3
#             }});
#         }}
#         layer.setStyle({{
#             weight: 4,
#             color: 'red',
#             fillOpacity: 0.8
#         }});
#         layer.bringToFront();
#         selectedLayer = layer;
#     }}

#     function resetHighlight(e) {{
#         if (selectedLayer) {{
#             selectedLayer.setStyle({{
#                 weight: 1,
#                 color: 'black',
#                 fillOpacity: 0.3
#             }});
#             selectedLayer = null;
#         }}
#     }}

#     // Find GeoJson layer and bind events
#     map.eachLayer(function(layer) {{
#         if (layer instanceof L.GeoJSON) {{
#             layer.eachLayer(function(featureLayer) {{
#                 try {{
#                     featureLayer.on({{
#                         click: highlightFeature,
#                         mouseover: highlightFeature,
#                         mouseout: resetHighlight
#                     }});
#                 }} catch (error) {{
#                     console.error('Error binding events to layer:', error);
#                 }}
#             }});
#         }}
#     }});

#     // Reset on map click outside
#     map.on('click', function(e) {{
#         if (!e.originalEvent.target.closest('.leaflet-interactive')) {{
#             resetHighlight(e);
#         }}
#     }});
# }}

# window.addEventListener('load', function() {{
#     setTimeout(setupMapInteractions, 100);
# }});
# </script>
# """

# # Add JS as a direct HTML element
# m.get_root().html.add_child(folium.Element(js_code))

# # Step 11: Add legend and title
# folium.LayerControl().add_to(m)
# title_html = '<h3 align="center" style="font-size:20px"><b>Interactive Mineral Licenses Distribution in Nigeria</b></h3>'
# m.get_root().html.add_child(folium.Element(title_html))

# # Step 12: Save as HTML
# print("Saving interactive map to interactive_mineral_map.html...")
# m.save('interactive_mineral_map.html')
# print("Map saved! Open 'interactive_mineral_map.html' in a browser.")
# print("To check for errors: Open the HTML, press F12, and look at the Console tab.")







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