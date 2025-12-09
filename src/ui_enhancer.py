import folium

JS_CODE = """
<script>
window.addEventListener('load', function() {
    setTimeout(function() {
        var container = document.getElementById('{map_id}');
        if (container && container._leaflet_map) {
            var map = container._leaflet_map;
            var selectedLayer = null;

            function highlightFeature(e) {
                var layer = e.target;
                if (selectedLayer && selectedLayer !== layer) {
                    resetHighlight({target: selectedLayer});
                }
                layer.setStyle({
                    weight: 3,
                    color: '#ff4444',
                    fillOpacity: 0.6,
                    fillColor: '#ff4444'
                });
                layer.bringToFront();
                selectedLayer = layer;
            }

            function resetHighlight(e) {
                var layer = e.target;
                // Check if the feature has data (total > 0) to determine default style
                var featureTotal = layer.feature.properties.total;
                
                layer.setStyle({
                    weight: 1,
                    color: '#444',
                    fillOpacity: featureTotal > 0 ? 0.7 : 0.0, 
                    // Note: Fill color is handled by the Choropleth, but we reset border/opacity here
                });
                
                if (selectedLayer === layer) {
                    selectedLayer = null;
                }
            }

            map.eachLayer(function(layer) {
                if (layer instanceof L.GeoJSON) {
                    layer.eachLayer(function(featureLayer) {
                        // Apply CSS class for transitions
                        if (featureLayer.getElement()) {
                            featureLayer.getElement().classList.add('geojson-layer');
                        }
                        
                        featureLayer.on({
                            mouseover: highlightFeature,
                            mouseout: function(e) {
                                if (selectedLayer !== e.target) {
                                    resetHighlight(e);
                                }
                            },
                            click: highlightFeature
                        });
                    });
                }
            });
            
            // Re-apply transitions when layers change (e.g. zoom/pan might re-render)
            map.on('layeradd', function(e) {
                if (e.layer.getElement && e.layer.feature) {
                    e.layer.getElement().classList.add('geojson-layer');
                }
            });

            map.on('click', function(e) {
                if (!e.originalEvent.target.closest('.leaflet-interactive')) {
                    if (selectedLayer) {
                        resetHighlight({target: selectedLayer});
                    }
                }
            });
        }
    }, 500); // Increased timeout slightly to ensure map render
});
</script>

<style>
/* Glassmorphism Popup */
.leaflet-popup-content-wrapper {
    background: rgba(30, 30, 30, 0.9);
    backdrop-filter: blur(10px);
    -webkit-backdrop-filter: blur(10px);
    border: 1px solid rgba(255, 255, 255, 0.1);
    border-radius: 12px;
    box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
    color: #fff;
    padding: 0;
}
.leaflet-popup-tip {
    background: rgba(30, 30, 30, 0.9);
}
.leaflet-popup-close-button {
    color: #fff !important;
    font-size: 16px !important;
    top: 8px !important;
    right: 8px !important;
}

/* Smooth Transitions for Map Paths */
path.leaflet-interactive {
    transition: stroke 0.3s ease, fill-opacity 0.3s ease, stroke-width 0.3s ease;
}

body { margin: 0; padding: 0; font-family: 'Inter', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; background: #1a1a1a; }
#map { width: 100vw; height: 100vh; }
</style>
"""

TITLE_HTML = """
<div style="
    position: fixed; 
    top: 20px; 
    left: 20px; 
    z-index: 1000; 
    width: 300px;
    background: rgba(15, 15, 15, 0.75);
    backdrop-filter: blur(15px);
    -webkit-backdrop-filter: blur(15px);
    border: 1px solid rgba(255, 255, 255, 0.1);
    padding: 20px; 
    border-radius: 16px; 
    box-shadow: 0 4px 30px rgba(0, 0, 0, 0.5);
    color: white;
    font-family: 'Inter', sans-serif;
">
    <h3 style="margin: 0 0 10px 0; font-size: 18px; font-weight: 700; letter-spacing: -0.5px; background: linear-gradient(90deg, #fff, #aaa); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">Nigeria Mineral Map</h3>
    <p style="margin: 0 0 15px 0; font-size: 13px; color: #aaa; line-height: 1.4;">
        Visualizing mineral license distribution across 36 states + FCT.
    </p>
    <div style="display: flex; gap: 10px; font-size: 11px; color: #888;">
        <span style="display: flex; align-items: center;"><span style="width: 8px; height: 8px; background: #bd0026; display: inline-block; margin-right: 5px; border-radius: 50%;"></span> High Activity</span>
        <span style="display: flex; align-items: center;"><span style="width: 8px; height: 8px; background: #ffeda0; display: inline-block; margin-right: 5px; border-radius: 50%;"></span> Low Activity</span>
    </div>
</div>
"""

def enhance_ui(m: folium.Map) -> folium.Map:
    """Inject JS/CSS and title."""
    map_id = m.get_name()
    js_with_id = JS_CODE.replace('{map_id}', map_id)
    m.get_root().html.add_child(folium.Element(js_with_id))
    m.get_root().html.add_child(folium.Element(TITLE_HTML))
    return m

