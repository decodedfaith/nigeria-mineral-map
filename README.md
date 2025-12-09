# Nigeria Mineral Map

[![Python](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Live Demo](https://img.shields.io/badge/Live%20Demo-GitHub%20Pages-brightgreen)](https://decodedfaith.github.io/nigeria-mineral-map/)

> **MVP Status**: This is a Minimum Viable Product (MVP) demonstrating statistical visualization of Nigeria's mineral licensing distribution. The current version uses hardcoded sample data for demonstration purposes. See the [Roadmap](#roadmap--future-opportunities) for planned enhancements.

An interactive web-based choropleth map visualizing the distribution of mineral licenses across Nigeria's 36 states and the Federal Capital Territory. The tool provides a visual overview of Small Scale Mining Licenses (SSML), Mining Leases (ML), and Quarry Licenses (QL) by state.

## Live Demo

🚀 **[View Interactive Map on GitHub Pages](https://decodedfaith.github.io/nigeria-mineral-map/)**

Click on any state to view detailed license statistics in an interactive popup.

## Features

- **Interactive Choropleth Map**: Color-coded states based on total mineral license counts
- **State-Level Statistics**: Click any state to view breakdown by license type (SSML, ML, QL)
- **Hover Effects**: Visual highlighting of states on mouseover
- **Responsive Design**: Full-screen map interface optimized for desktop viewing
- **Geospatial Processing**: Built with Python geospatial libraries (GeoPandas, Folium)

## Current MVP Implementation

### Data Source
The current version uses **static, hardcoded data** representing an approximate snapshot from Q1 2022, sourced from Nigerian Mining Cadastre Office (NMCO) records. This data is embedded in [`src/data_processor.py`](src/data_processor.py) for demonstration purposes.

**Important**: This is **not** real-time data. The values are simplified for MVP demonstration and should not be used for official or commercial purposes.

### Architecture
- **Backend**: Python scripts process geospatial data and generate the map
- **Frontend**: Static HTML file (`index.html`) with embedded Leaflet.js and GeoJSON
- **Output**: ~16MB HTML file (large due to embedded Nigeria state boundaries GeoJSON)

## Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Setup Instructions

1. **Clone the repository**:
   ```bash
   git clone https://github.com/decodedfaith/nigeria-mineral-map.git
   cd nigeria-mineral-map
   ```

2. **Create and activate a virtual environment** (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Obtain geospatial data**:
   - Download Nigeria administrative boundaries (GADM level 1) from [GADM](https://gadm.org/download_country.html)
   - Place the `.gpkg` file in the `data/` directory as `gadm41_NGA.gpkg`
   - Alternatively, use any Nigeria state-level shapefile/GeoPackage

## Usage

### Generate the Map

Run the main script to generate the interactive map:

```bash
python main.py
```

This will:
1. Load the Nigeria state boundaries from `data/gadm41_NGA.gpkg`
2. Merge with the sample license data
3. Generate choropleth visualization
4. Save output to `index.html`

### View the Map

Open `index.html` in any modern web browser:

```bash
# macOS
open index.html

# Linux
xdg-open index.html

# Windows
start index.html
```

Or deploy to GitHub Pages for public access.

## Project Structure

```
nigeria-mineral-map/
├── src/
│   ├── __init__.py
│   ├── data_loader.py       # Loads GADM GeoPackage files
│   ├── data_processor.py    # Contains sample data and merging logic
│   ├── map_builder.py       # Generates Folium choropleth map
│   └── ui_enhancer.py       # Adds JavaScript interactivity
├── data/
│   └── gadm41_NGA.gpkg      # Nigeria state boundaries (user-provided)
├── index.html               # Generated interactive map
├── main.py                  # Entry point script
├── requirements.txt         # Python dependencies
├── LICENSE                  # MIT License
├── CONTRIBUTING.md          # Contribution guidelines
└── README.md                # This file
```

## Roadmap & Future Opportunities

This project is designed to scale and address real-world challenges in Nigeria's solid minerals sector. Planned enhancements include:

### 🎯 Phase 1: Real-Time Data Integration
- [ ] Connect to [Nigerian Mining Cadastre Portal](https://miningcadastre.gov.ng/) API
- [ ] Implement automated data refresh pipeline
- [ ] Add data validation and quality checks
- [ ] Display last-updated timestamp on map

### 🌍 Phase 2: Regional Expansion
- [ ] Extend coverage to West African countries (Ghana, Sierra Leone, etc.)
- [ ] Pan-African mineral license database integration
- [ ] Comparative analytics across countries

### 📊 Phase 3: Advanced Analytics
- [ ] Mineral type filtering (iron ore, coal, limestone, gold, etc.)
- [ ] Time-series visualization (license trends over years)
- [ ] Search functionality by state, mineral, or company
- [ ] Download filtered datasets as CSV/GeoJSON
- [ ] Mobile-responsive design

### 🔧 Phase 4: Performance & UX
- [ ] Migrate from embedded GeoJSON to tile-based mapping
- [ ] Implement dynamic data loading (reduce initial file size)
- [ ] Add legend and color scale customization
- [ ] Multi-language support (English, Hausa, Yoruba, Igbo)

### 🤝 Open-Source Collaboration
We welcome contributions! See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## Known Issues & Limitations

- **Large File Size**: `index.html` is ~16MB due to embedded Nigeria state GeoJSON. Future versions will use tiled mapping or external JSON files.
- **Static Data**: Current data is hardcoded and not real-time. API integration is planned.
- **Desktop-Optimized**: Mobile responsiveness is limited in the current version.

## Data Attribution

- **Geospatial Boundaries**: [GADM](https://gadm.org/) - Database of Global Administrative Areas
- **License Data**: Sample data inspired by Nigerian Mining Cadastre Office (NMCO) records (Q1 2022 approximation)

> **Disclaimer**: This tool is for informational and educational purposes only. For official mineral licensing data, consult the [Nigerian Mining Cadastre Office](https://miningcadastre.gov.ng/).

## Contributing

We welcome contributions from developers, geospatial analysts, and mining sector professionals! Please read our [Contributing Guidelines](CONTRIBUTING.md) and [Code of Conduct](CODE_OF_CONDUCT.md).

### How to Contribute
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/your-feature-name`)
3. Commit changes with clear messages
4. Push to your fork and submit a Pull Request

## License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Built with [GeoPandas](https://geopandas.org/), [Folium](https://python-visualization.github.io/folium/), and [Leaflet.js](https://leafletjs.com/)
- Nigeria boundary data courtesy of [GADM](https://gadm.org/)
- Inspired by the need for transparent, accessible mineral resource data in Nigeria

## Contact & Support

- **Project Maintainer**: [@decodedfaith](https://github.com/decodedfaith)
- **Issues**: [GitHub Issues](https://github.com/decodedfaith/nigeria-mineral-map/issues)
- **Discussions**: [GitHub Discussions](https://github.com/decodedfaith/nigeria-mineral-map/discussions)

---

**⭐ If you find this project useful, please consider starring the repository!**