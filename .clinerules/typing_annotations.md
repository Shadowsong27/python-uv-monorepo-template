# Type Annotations

## No Quoted Types Unless Required
- Do not quote types in type annotations unless they require delayed reference
- Use direct type names instead of quoted strings in return type annotations
- Only use quoted types for forward references or to avoid circular imports

Example:
```python
# CORRECT
def process_data(self) -> DataPayload:
    # Implementation
    return self

# ONLY when necessary for forward references or circular imports
def create_node(self) -> "TreeNode":
    # Implementation
    return TreeNode()
```

## Use Primitive Types When Available
- Use primitive types instead of imported types when available
- Use `list` instead of `List`, `dict` instead of `Dict`, etc.
- Only import types from typing module when necessary (e.g., for complex types like `Union`, `Optional`, etc.)

Example:
```python
# CORRECT
def load_documents(self, documents: list[Document]) -> list[ParsedDocument]:
    # Implementation
    return parsed_documents

# INCORRECT
from typing import List
def load_documents(self, documents: List[Document]) -> List[ParsedDocument]:
    # Implementation
    return parsed_documents
