# Naming Conventions

## Overview

This document standardizes naming conventions to eliminate confusion between dashes and underscores in Python projects.

## Core Principle: Context-Specific Naming

The naming convention follows a **context-based approach** where the format depends on the usage context:

```
Package Distribution Names (PyPI/pip): Use dashes (kebab-case)
Python Import Names: Use underscores (snake_case)
Directory Names: Use underscores (snake_case)
Database/Schema Names: Use underscores (snake_case)
Git Repository Names: Use dashes (kebab-case)
```

## Naming Rules by Context

### 1. Package Distribution Names (PyPI)
**Rule**: Always use **dashes** (kebab-case)

**Examples**:
- `my-package` (not `my_package`)
- `data-utils` (not `data_utils`)

**Where Used**:
- `pyproject.toml` `[project] name` field
- `pip install` commands
- `uv add` commands
- Package dependencies in `pyproject.toml`

**Example**:
```toml
[project]
name = "my-package"  # ✓ CORRECT

[project.dependencies]
dependencies = [
    "data-utils",  # ✓ CORRECT
]
```

### 2. Python Import Names
**Rule**: Always use **underscores** (snake_case)

**Examples**:
- `import my_package` (not `import my-package`)
- `from data_utils import something`

**Where Used**:
- Python import statements
- Module references in code
- `__init__.py` files

**Example**:
```python
# ✓ CORRECT
from my_package.core import MyClass
from data_utils.helpers import helper_function

# ✗ INCORRECT
from my-package.core import MyClass  # Python doesn't allow dashes in imports
```

### 3. Directory Names
**Rule**: Always use **underscores** (snake_case)

**Examples**:
- `libs/my_package/` (not `libs/my-package/`)
- `src/my_package/` (not `src/my-package/`)

**Where Used**:
- All directory structures
- Source code directories
- Test directories

**Example**:
```
libs/
├── my_package/      # ✓ CORRECT
└── data_utils/      # ✓ CORRECT
```

### 4. Database and Schema Names
**Rule**: Always use **underscores** (snake_case)

**Examples**:
- `my_database` (not `my-database`)
- `user_data` (not `user-data`)

**Where Used**:
- Database names
- Schema names
- Table names and prefixes

**Example**:
```python
# ✓ CORRECT
DATABASE_NAME = "my_database"
table_name = "user_data"

# ✗ INCORRECT
DATABASE_NAME = "my-database"
```

### 5. Git Repository Names
**Rule**: Use **dashes** (kebab-case)

**Examples**:
- `my-project` (not `my_project`)

**Where Used**:
- GitHub repository names
- Git clone URLs

**Example**:
```bash
# ✓ CORRECT
git clone git@github.com:username/my-project.git

# ✗ INCORRECT
git clone git@github.com:username/my_project.git
```

### 6. Configuration Files and YAML
**Rule**: Use **underscores** for identifiers, **dashes** for file names

**Examples**:
- File names: `docker-compose.yml`, `pre-commit-config.yaml`
- YAML keys/values: `database_name: my_database`

**Where Used**:
- YAML configuration files
- Docker compose files
- CI/CD configuration

**Example**:
```yaml
# File: docker-compose.yml (dash in filename)
# ✓ CORRECT
database_name: my_database  # underscore in value
services:
  my_service:  # underscore in key
    image: myapp
```

### 7. Environment Variables
**Rule**: Use **underscores** (SCREAMING_SNAKE_CASE)

**Examples**:
- `MY_APP_SETTINGS`
- `DATABASE_URL`

**Where Used**:
- Environment variable names
- Settings configuration

**Example**:
```bash
# ✓ CORRECT
export MY_APP_SETTINGS="..."
export DATABASE_URL="postgresql://..."
```

## Quick Reference Table

| Context | Format | Example | Rationale |
|---------|--------|---------|-----------|
| PyPI Package Name | `kebab-case` | `my-package` | PyPI/pip convention |
| Python Import | `snake_case` | `import my_package` | Python syntax requirement |
| Directory Name | `snake_case` | `libs/my_package/` | Matches Python imports |
| Database/Schema | `snake_case` | `my_database` | SQL convention |
| Git Repository | `kebab-case` | `my-project` | GitHub convention |
| YAML File Name | `kebab-case` | `docker-compose.yml` | Common convention |
| YAML Keys/Values | `snake_case` | `database_name: my_db` | Consistency with code |
| Environment Vars | `SCREAMING_SNAKE_CASE` | `MY_APP_SETTINGS` | Shell convention |

## Common Patterns

### Package References
```toml
# In pyproject.toml dependencies
[project.dependencies]
dependencies = [
    "my-package",      # ✓ Package name with dash
    "data-utils",      # ✓ Package name with dash
]

[tool.uv.sources]
my-package = { workspace = true }  # ✓ Package name with dash
```

### Python Code
```python
# In Python files
from my_package.core import something    # ✓ Import with underscore
from data_utils.helpers import Helper    # ✓ Import with underscore

# Database references
database_name = "my_database"  # ✓ Database with underscore
```

### File Paths
```bash
# Directory structure
libs/my_package/src/my_package/  # ✓ All underscores
libs/data_utils/                 # ✓ All underscores

# File names
docker-compose.yml               # ✓ Dash in filename
.pre-commit-config.yaml          # ✓ Dash in filename
```

## Migration Guide

If you encounter inconsistent naming:

1. **Package names in dependencies**: Use dashes (`my-package`)
2. **Python imports**: Use underscores (`import my_package`)
3. **Directory names**: Use underscores (`libs/my_package/`)
4. **Database names**: Use underscores (`my_database`)
5. **When in doubt**: Check this guide

## Why This Matters

- **Python Syntax**: Python doesn't allow dashes in import statements
- **Package Managers**: PyPI and pip use dashes by convention
- **Consistency**: Following conventions reduces cognitive load
- **Tooling**: Many tools expect specific naming patterns
- **Interoperability**: Different systems have different requirements

## Examples

### ✓ CORRECT Usage
```python
# Package installation
pip install my-package

# Python import
from my_package.core import MyClass

# Directory structure
libs/my_package/src/my_package/

# Database name
DATABASE_NAME = "my_database"
```

### ✗ INCORRECT Usage (to avoid)
```python
# Don't mix conventions
pip install my_package  # Wrong: use my-package
from my-package import something  # Wrong: Python syntax error
libs/my-package/  # Wrong: use my_package
database_name = "my-database"  # Wrong: use my_database
```

## Summary

**Remember**: The separator choice is **context-dependent**, not arbitrary. Each context has technical or conventional reasons for its preferred format. When you follow these rules, the codebase becomes more maintainable and less confusing.
