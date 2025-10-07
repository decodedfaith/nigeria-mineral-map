import folium
from typing import Optional

def build_base_map(center: list = [9.0820, 8.6753], zoom: int = 6) -> folium.Map:
    """Create and return base Folium map."""
    return folium.Map(
        location=center,
        zoom_start=zoom,
        tiles='OpenStreetMap',
        control_scale=True
    )

def add_choropleth_layer(m: folium.Map, gdf) -> folium.Map:
    """Add choropleth based on 'total' column."""
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
    return m

def add_geojson_layer(m: folium.Map, gdf) -> folium.Map:
    """Add interactive GeoJSON with tooltips and popups."""
    folium.GeoJson(
        gdf,
        style_function=lambda x: {
            'fillColor': 'red' if x['properties']['total'] > 0 else 'white',
            'weight': 1, 'color': 'black', 'fillOpacity': 0.3
        },
        highlight_function=lambda x: {'weight': 4, 'color': 'red', 'fillOpacity': 0.8},
        tooltip=folium.GeoJsonTooltip(
            fields=['NAME_1', 'total'],
            aliases=['State:', 'Total Valid Licenses:'],
            localize=True, sticky=True, labels=True,
            style="font-size: 12px; padding: 5px; background-color: #fff; border-radius: 3px;"
        ),
        popup=folium.GeoJsonPopup(
            fields=['popup_html'], aliases=[''],
            style="font-size: 12px; padding: 0;", max_width=300, sticky=False,
            closeButton=True, autoClose=False
        ),
        name='Nigeria States'
    ).add_to(m)
    return m

def add_labels(m: folium.Map, gdf) -> folium.Map:
    """Add persistent labels for states with >0 licenses."""
    for idx, row in gdf[gdf['total'] > 0].iterrows():
        centroid = row.geometry.centroid
        folium.Marker(
            location=[centroid.y, centroid.x],
            icon=folium.features.DivIcon(
                html=f'<div style="font-size: 10px; font-weight: bold; color: black; text-align: center;background: rgba(255, 255, 255, 0.0); padding: 2px; border-radius: 3px;">{int(row["total"])}</div>',
                icon_size=(30, 30)
            )
        ).add_to(m)
    return m

def build_map(gdf) -> folium.Map:
    """Orchestrate all layers into a complete map."""
    m = build_base_map()
    m = add_choropleth_layer(m, gdf)
    m = add_geojson_layer(m, gdf)
    m = add_labels(m, gdf)
    folium.LayerControl().add_to(m)
    return m