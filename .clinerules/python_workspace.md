# Python Workspace Patterns

## UV Workspace Management

### Use `uv sync` for Workspace Installation
- **Rule**: In UV workspaces, use `uv sync` instead of `pip install -e .` for installing workspace members
- **Rationale**: Workspace members are automatically editable by default in UV workspaces
- **Pattern**: Run `uv sync` from the root directory to install all workspace dependencies and members
- **Example**:
```bash
# CORRECT - Install all workspace members and dependencies
uv sync

# AVOID - Manual editable installation of workspace members
cd libs/package_name && pip install -e .
```

### Virtual Environment Activation
- **Rule**: Activate the virtual environment before running any Python commands
- **Pattern**: Use `source .venv/bin/activate` or the appropriate activation command for your environment
- **Example**:
```bash
# Activate virtual environment first
source .venv/bin/activate

# Then run UV commands
uv sync
```

### Workspace Structure
- **Rule**: Use proper workspace structure with libs/ or apps/ directory for packages
- **Pattern**: Each package should have its own pyproject.toml with proper src-layout structure
- **Example Structure**:
```
project-root/
├── pyproject.toml (workspace root)
├── libs/
│   ├── package1/
│   │   ├── pyproject.toml
│   │   └── src/package1/
│   └── package2/
│       ├── pyproject.toml
│       └── src/package2/
└── apps/
    └── app1/
        ├── pyproject.toml
        └── src/app1/
