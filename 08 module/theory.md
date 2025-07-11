# Functions in Python

## Defining a Function
A function is a block of code that performs a specific task. Defined using the `def` keyword.

## Calling a Function
Invoke a function by its name followed by parentheses, passing arguments if required.

## Types of Functions
- **Built-in Functions:** Provided by Python (e.g., `print()`, `len()`).
- **User-defined Functions:** Created by the programmer.
- **Anonymous Functions:** Functions without a name, created using `lambda`.

## Function Arguments
- **Positional Arguments:** Passed by position.
- **Keyword Arguments:** Passed by name.
- **Default Arguments:** Have default values.
- **Variable-length Arguments:** `*args` (tuple), `**kwargs` (dictionary).

## Anonymous Functions
Created using `lambda` keyword for simple, one-line functions.

## Global and Local Variables
- **Local Variables:** Defined inside a function, accessible only within it.
- **Global Variables:** Defined outside functions, accessible everywhere. Use `global` keyword to modify inside functions.

## Example
```python
def add(a, b):
    return a + b

result = add(2, 3)

square = lambda x: x * x

x = 10
def foo():
    global x
    x = 20
```