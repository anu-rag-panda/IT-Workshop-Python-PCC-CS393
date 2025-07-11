# Dictionaries in Python

## Introduction
A dictionary is an unordered, mutable collection of key-value pairs. Dictionaries are defined using curly braces `{}`. Each key must be unique and immutable.

## Accessing Values in Dictionaries
Values are accessed using their keys: `dict[key]`. If the key does not exist, a `KeyError` is raised.

## Working with Dictionaries
- **Adding/Updating:** `dict[key] = value`
- **Deleting:** `del dict[key]`
- **Iterating:** Use `.items()`, `.keys()`, `.values()` for iteration.

## Properties
- Keys must be immutable (e.g., strings, numbers, tuples).
- Values can be any data type.
- Dictionaries are mutable and unordered.

## Functions and Methods
- `len(dict)`, `dict.get(key)`, `dict.pop(key)`, `dict.clear()`, `dict.update(other_dict)`

## Example
```python
d = {'a': 1, 'b': 2}
print(d['a'])           # Access value
d['c'] = 3              # Add new key-value
print(d.get('d', 0))    # Safe access with default
for k, v in d.items():  # Iterate
    print(k, v)
```