# Nigeria Mineral Map

[![Python](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Live Demo](https://img.shields.io/badge/Live%20Demo-GitHub%20Pages-brightgreen)](https://decodedfaith.github.io/nigeria-mineral-map/)
[![Geospatial](https://img.shields.io/badge/geospatial-Folium%20%7C%20GeoPandas-green.svg)](https://geopandas.org/)

An interactive web-based map visualizing Nigeria's solid mineral resources, such as iron ore, coal, barite, and limestone. Built with Python for data processing and geospatial analysis, using sources like the Nigerian Geological Survey Agency (NGSA) datasets. The app enables users to explore mineral deposits by state, with filters for resource type and interactive UI enhancements.

## Live Demo
Try the interactive map right now: [View on GitHub Pages](https://decodedfaith.github.io/nigeria-mineral-map/).

(If the site is down for updates, see local setup below.)

## Features
- **Data Loading & Processing**: Ingests geospatial data (e.g., shapefiles from NGSA) and processes it for visualization.
- **Map Building**: Renders interactive maps using Folium/Leaflet.js.
- **UI Enhancement**: Custom overlays, tooltips, and Cython-accelerated computations for performance.
- **Export Options**: Download filtered data as CSV or GeoJSON.

## Installation
For development or local runs:
1. Clone the repository:
git clone https://github.com/decodedfaith/nigeria-mineral-map.git
cd nigeria-mineral-map
text2. Create a virtual environment (recommended):
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
text3. Install dependencies:
pip install -r requirements.txt
text## Usage
- **Hosted Version**: Access the live site at [https://decodedfaith.github.io/nigeria-mineral-map/](https://decodedfaith.github.io/nigeria-mineral-map/). Filter by "iron ore" to see deposits in Abia and Anambra states.
- **Local Run**: Launch the app with:
python main.py
textOpen your browser to `http://localhost:5000` (or the port shown).

For development, install in editable mode:
pip install -e .
text## Project Structure
nigeria-mineral-map/
├── src/
│   ├── init.py
│   ├── data_loader.py      # Loads NGSA shapefiles and CSV data
│   ├── data_processor.py   # Cleans and aggregates mineral data
│   ├── map_builder.py      # Generates Folium maps with markers/clusters
│   └── ui_enhancer.py      # Adds JS/CSS for interactivity (Cython-optimized)
├── data/                   # External datasets (e.g., NGSA minerals shapefile)
├── docs/                   # Additional documentation
├── main.py                 # Entry point: Orchestrates the app
├── requirements.txt        # Python dependencies
├── setup.py                # Packaging config
├── README.md               # This file
└── LICENSE                 # MIT License
text## Data Sources
- Nigerian Geological Survey Agency (NGSA): [Mineral Resources Map](https://ngsa.gov.ng/) (download shapefiles; add to `/data/`).
- Avoid committing large files—use `.gitignore` and fetch via script if needed.

## Contributing
See [CONTRIBUTING.md](CONTRIBUTING.md) for details.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments
- Built with [GeoPandas](https://geopandas.org/), [Folium](https://python-visualization.github.io/folium/), and Cython.
- Data courtesy of NGSA.
- Hosted on [GitHub Pages](https://pages.github.com/). (https://decodedfaith.github.io/nigeria-mineral-map/)