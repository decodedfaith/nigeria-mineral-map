markdown# Contributing to Nigeria Mineral Map

Thank you for considering contributing! We welcome improvements, bug fixes, new features, and documentation updates.

## Getting Started
1. Fork the repository on GitHub.
2. Clone your fork locally:
git clone https://github.com/YOUR_USERNAME/nigeria-mineral-map.git
cd nigeria-mineral-map
text3. Create a feature branch for your work:
git checkout -b feature/your-feature-name
text4. Install dependencies in a virtual environment (see [README.md](README.md) for setup).

## Making Changes
- **Code Style**: Follow [PEP 8](https://peps.python.org/pep-0008/). Use [Black](https://black.readthedocs.io/) for auto-formatting: `pip install black && black .`.
- **Testing**: Add unit tests in a `tests/` folder (use pytest). Run with `pytest`.
- **Geospatial Data**: If adding data, document sources in `/data/README.md` and avoid committing large files (use `.gitignore`).
- Commit often with clear messages (e.g., "Fix map zoom on mobile").

## Submitting Changes
1. Push your branch: `git push origin feature/your-feature-name`.
2. Open a [Pull Request (PR)](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request) on the original repo.
- Reference any related issues (e.g., "Closes #5").
- Explain what you changed and why.
3. Respond to feedback in the PR discussion.

## Code of Conduct
This project follows the [Contributor Covenant Code of Conduct](https://www.contributor-covenant.org/version/2/0/code_of_conduct/). By participating, you agree to abide by it. Reports of abusive behavior can be emailed to [komolafefaith@gmail.com]

## Questions?
Open an [issue](https://github.com/decodedfaith/nigeria-mineral-map/issues) or ask in discussions. Happy contributing!