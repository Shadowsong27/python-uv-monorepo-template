# {{project_name}}

{{project_description}}

## Project Structure

This project uses a uv workspace structure:

```
.
├── apps/
│   └── {{project_name}}/          # Main application package
│       ├── src/                   # Source code
│       ├── tests/                 # Tests
│       └── pyproject.toml         # Package configuration
├── .github/
│   └── workflows/                 # GitHub Actions workflows
├── pyproject.toml                 # Workspace configuration
├── release-please-config.json     # Release Please configuration
├── .release-please-manifest.json  # Release Please manifest
└── README.md                      # This file
```

## Development Setup

### Prerequisites

- Python 3.11+
- [uv](https://docs.astral.sh/uv/) package manager

### Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd {{project_name}}
```

2. Install dependencies using uv:
```bash
uv sync
```

3. Install pre-commit hooks:
```bash
uv run pre-commit install
```

## Usage

### Running the Application

```bash
uv run python -m {{project_name}}
```

### Running Tests

```bash
# Run all tests
uv run pytest

# Run tests with coverage
uv run pytest --cov=src --cov-report=html
```

### Code Quality

```bash
# Format code
uv run ruff format

# Lint code
uv run ruff check

# Run pre-commit hooks
uv run pre-commit run --all-files
```

## Development Workflow

1. Create a new branch for your feature/fix
2. Make your changes
3. Run tests and ensure they pass
4. Run code quality checks
5. Commit your changes (pre-commit hooks will run automatically)
6. Push your branch and create a pull request

## Release Management

This project uses [Release Please](https://github.com/googleapis/release-please) for automated releases:

- Releases are triggered by merging to the `main` branch
- Version bumps are determined by conventional commit messages
- Changelog is automatically generated
- GitHub releases are created automatically

### Conventional Commits

Use conventional commit messages for automatic version bumping:

- `feat:` - New features (minor version bump)
- `fix:` - Bug fixes (patch version bump)
- `feat!:` or `fix!:` - Breaking changes (major version bump)
- `docs:`, `style:`, `refactor:`, `test:`, `chore:` - No version bump

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests for new functionality
5. Ensure all tests pass
6. Submit a pull request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
