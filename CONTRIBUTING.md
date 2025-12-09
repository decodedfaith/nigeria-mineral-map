# Contributing to Nigeria Mineral Map

Thank you for your interest in contributing to the Nigeria Mineral Map project! We welcome contributions from developers, data scientists, geologists, and anyone interested in making mineral data more accessible.

## How to Contribute

### Reporting Bugs
If you find a bug, please create a new issue on GitHub. Be sure to include:
- A clear, descriptive title
- Steps to reproduce the issue
- Expected vs. actual behavior
- Screenshots (if applicable)

### Suggesting Enhancements
We love new ideas! If you have a suggestion:
1. Check existing issues to see if it's already been proposed.
2. Open a new issue describing your idea and why it would be valuable.

### Pull Requests
1. **Fork the repository** to your own GitHub account.
2. **Create a new branch** for your feature or bugfix:
   ```bash
   git checkout -b feature/amazing-new-feature
   ```
3. **Make your changes** and commit them with clear, descriptive messages.
   - Follow the existing code style (PEP 8 for Python).
   - Ensure your code is well-documented.
4. **Push your branch** to your fork:
   ```bash
   git push origin feature/amazing-new-feature
   ```
5. **Open a Pull Request (PR)** against the `main` branch of this repository.
   - Describe your changes in detail.
   - Link to any relevant issues.

## Development Setup

1. Clone the repo:
   ```bash
   git clone https://github.com/decodedfaith/nigeria-mineral-map.git
   cd nigeria-mineral-map
   ```
2. Set up a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Code Standards

- **Python**: We follow [PEP 8](https://www.python.org/dev/peps/pep-0008/). Please ensure your code is readable and includes docstrings for functions and classes.
- **Data**: Do not commit large binary files or sensitive data.
- **Documentation**: Update `README.md` if you change how the application is built or used.

## License

By contributing, you agree that your contributions will be licensed under the MIT License.