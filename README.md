# Python UV Monorepo Template

A modern Python monorepo template using [uv](https://docs.astral.sh/uv/) for fast dependency management and workspace organization.

## Project Structure

This project uses a uv workspace structure:

```
.
├── apps/
│   └── sample-app/                # Sample application package (rename this)
│       ├── src/                   # Source code
│       ├── tests/                 # Tests
│       └── pyproject.toml         # Package configuration
├── .cline/                        # Cline AI assistant configuration
│   ├── specs/                     # Project specifications and documentation
│   └── workspace_rules/           # Workspace-specific rules for Cline
├── .github/
│   └── workflows/                 # GitHub Actions workflows
├── pyproject.toml                 # Workspace configuration
├── release-please-config.json     # Release Please configuration
├── .release-please-manifest.json  # Release Please manifest
└── README.md                      # This file
```

## Getting Started

### Prerequisites

- Python 3.11+
- [uv](https://docs.astral.sh/uv/) package manager

### Customizing the Template

Before using this template, you'll need to replace the following placeholder values:

1. **Project Name**: Replace `sample-app` throughout the codebase with your actual project name:
   - Directory name: `apps/sample-app/` → `apps/your-project-name/`
   - Package name in `apps/sample-app/pyproject.toml`
   - Import statements in source code
   - Script entry points

2. **Template Placeholders**: Replace any remaining template placeholders:
   - `{{project_name}}` in configuration files
   - Author information in `pyproject.toml` files
   - Repository URLs and descriptions

3. **Package Structure**: Update the package structure in `apps/sample-app/src/sample_app/` to match your project name

### Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd your-project-name
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
# Run the sample app (update command after renaming)
uv run python -m sample_app

# Or use the script entry point
uv run sample-app
```

### Running Tests

```bash
# Run all tests
uv run pytest

# Run tests with coverage
uv run pytest --cov=src --cov-report=html

# Run tests for a specific app
uv run pytest apps/sample-app/tests/
```

### Code Quality

```bash
# Format code
uv run ruff format

# Lint code
uv run ruff check

# Fix linting issues automatically
uv run ruff check --fix

# Run pre-commit hooks
uv run pre-commit run --all-files
```

## Cline AI Assistant Integration

This template includes a `.cline/` directory for enhanced AI-assisted development:

- **`.cline/specs/`**: Store project specifications, requirements, and documentation that help Cline understand your project context
- **`.cline/workspace_rules/`**: Define workspace-specific rules and patterns for Cline to follow

To use with Cline:
1. Install the [Cline VS Code extension](https://marketplace.visualstudio.com/items?itemName=saoudrizwan.claude-dev)
2. Add your project specifications to `.cline/specs/`
3. Configure workspace rules in `.cline/workspace_rules/`

## Development Workflow

1. Create a new branch for your feature/fix
2. Make your changes
3. Run tests and ensure they pass
4. Run code quality checks
5. Commit your changes (pre-commit hooks will run automatically)
6. Push your branch and create a pull request

## Adding New Apps

To add a new application to the workspace:

1. Create a new directory under `apps/`:
```bash
mkdir apps/new-app
```

2. Create a `pyproject.toml` file following the pattern in `apps/sample-app/pyproject.toml`

3. Set up the source structure:
```bash
mkdir -p apps/new-app/src/new_app
mkdir -p apps/new-app/tests
```

4. The workspace will automatically detect the new app after running `uv sync`

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

## Features

- **Fast dependency management** with uv
- **Monorepo structure** for multiple related packages
- **Pre-commit hooks** for code quality
- **Automated testing** with pytest and coverage
- **Code formatting** with ruff
- **Automated releases** with Release Please
- **AI assistant integration** with Cline configuration
- **GitHub Actions** workflows for CI/CD

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests for new functionality
5. Ensure all tests pass and code quality checks pass
6. Submit a pull request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
