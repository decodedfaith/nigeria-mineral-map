import folium

JS_CODE = """
<script>
window.addEventListener('load', function() {{
    setTimeout(function() {{
        var container = document.getElementById('{map_id}');
        if (container && container._leaflet_map) {{
            var map = container._leaflet_map;
            var selectedLayer = null;

            function highlightFeature(e) {{
                var layer = e.target;
                if (selectedLayer && selectedLayer !== layer) {{
                    resetHighlight({{target: selectedLayer}});
                }}
                layer.setStyle({{
                    weight: 4, color: 'red', fillOpacity: 0.8
                }});
                layer.bringToFront();
                selectedLayer = layer;
            }}

            function resetHighlight(e) {{
                var layer = e.target;
                layer.setStyle({{
                    weight: 1, color: 'black', fillOpacity: 0.3
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
.leaflet-popup-content-wrapper {{ border-radius: 5px; box-shadow: 0 2px 5px rgba(0,0,0,0.2); background: #fff; }}
.leaflet-popup-close-button {{ top: 5px !important; right: 5px !important; font-size: 14px !important; color: #333 !important; cursor: pointer !important; z-index: 1000 !important; }}
.leaflet-popup-tip {{ background: #fff !important; }}
body {{ margin: 0; padding: 0; font-family: Arial, sans-serif; }}
#map {{ width: 100vw; height: 100vh; }}
</style>
"""

TITLE_HTML = """
<div style="position: fixed; top: 10px; left: 50%; transform: translateX(-50%); z-index: 1000; background: rgba(255, 255, 255, 0.9); padding: 10px; border-radius: 5px; box-shadow: 0 2px 5px rgba(0,0,0,0.2);">
    <h3 style="margin: 0; font-size: 20px; text-align: center;"><b>Interactive Mineral Licenses Distribution in Nigeria</b></h3>
</div>
"""

def enhance_ui(m: folium.Map) -> folium.Map:
    """Inject JS/CSS and title."""
    map_id = m.get_name()
    js_with_id = JS_CODE.format(map_id=map_id)
    m.get_root().html.add_child(folium.Element(js_with_id))
    m.get_root().html.add_child(folium.Element(TITLE_HTML))
    return m