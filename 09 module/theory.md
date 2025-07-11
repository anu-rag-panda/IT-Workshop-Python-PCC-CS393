# Modules and Input-Output in Python

## Modules
A module is a file containing Python code (functions, classes, variables) that can be imported and reused. Use the `import` statement to include modules.

### Importing Modules
- `import module_name`
- `from module_name import function_name`
- `import module_name as alias`

## Math Module
Provides mathematical functions like `sqrt()`, `pow()`, `sin()`, `cos()`, etc.
```python
import math
print(math.sqrt(16))
```

## Random Module
Used for generating random numbers and selections.
```python
import random
print(random.randint(1, 10))
```

## Packages
A package is a collection of modules in a directory with an `__init__.py` file. Packages help organize code.

## Composition
Composition refers to combining modules and packages to build complex programs.

## Input-Output

### Printing on Screen
Use `print()` to display output.

### Reading Data from Keyboard
Use `input()` to get user input (always returns a string).

### Opening and Closing Files
Use `open(filename, mode)` to open files. Always close files using `close()` or with a `with` statement.

### Reading and Writing Files
- `read()`, `readline()`, `readlines()` for reading.
- `write()`, `writelines()` for writing.

### Functions in Modules
Modules can contain functions that can be imported and used in other programs.

## Example
```python
import math
import random

print(math.pi)
print(random.choice([1, 2, 3]))

with open('sample.txt', 'w') as f:
    f.write('Hello, World!')
```

## Extra: Best Practices
- Use modules to organize code and avoid repetition.
- Always close files after use.
- Use packages for large projects.
- Prefer `with open()` for file operations to ensure proper resource management.