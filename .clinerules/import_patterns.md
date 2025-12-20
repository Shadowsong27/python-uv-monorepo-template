# Import Patterns

## Explicit Imports in __init__.py
- **Rule**: Avoid importing everything from submodules in `__init__.py` files
- **Rationale**: Reduces namespace pollution and makes dependencies explicit
- **Example**:
```python
# AVOID - importing everything
from .submodule import *

# PREFER - explicit imports only when needed
# Leave __init__.py minimal or empty for most packages
```

## Explicit Import Usage
- **Rule**: Use explicit imports rather than wildcard imports
- **Rationale**: Makes dependencies clear and avoids namespace conflicts
- **Example**:
```python
# AVOID
from some_module import *

# PREFER
from some_module import SpecificClass, specific_function
```

## Import Organization
- **Rule**: Organize imports in a consistent order
- **Pattern**: Follow PEP 8 import ordering:
  1. Standard library imports
  2. Related third-party imports
  3. Local application/library specific imports
- **Example**:
```python
# Standard library
import os
import sys
from pathlib import Path

# Third-party
import numpy as np
import pandas as pd

# Local
from my_package.core import MyClass
from my_package.utils import helper_function
```

## Relative vs Absolute Imports
- **Rule**: Prefer absolute imports for clarity
- **Exception**: Use relative imports within a package when it improves readability
- **Example**:
```python
# PREFER - Absolute imports
from my_package.submodule import MyClass

# ACCEPTABLE - Relative imports within the same package
from .submodule import MyClass
from ..parent_module import ParentClass
