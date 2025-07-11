# Exception Handling in Python

## Exception
An exception is an error that occurs during program execution and disrupts the normal flow. Common exceptions include `ZeroDivisionError`, `ValueError`, and `FileNotFoundError`.

## Exception Handling
Python uses `try`, `except`, `else`, and `finally` blocks to handle exceptions gracefully and prevent program crashes.

### Except Clause
The `except` clause catches and handles exceptions. You can specify the exception type or use a generic handler.

### Try-Finally Clause
The `finally` block executes code regardless of whether an exception occurred, often used for cleanup actions like closing files.

### User Defined Exception
You can create custom exceptions by subclassing the `Exception` class.

## Example
```python
try:
    x = int(input("Enter a number: "))
    print(10 / x)
except ZeroDivisionError:
    print("Cannot divide by zero!")
except ValueError:
    print("Invalid input!")
finally:
    print("Execution complete.")

# User defined exception
class MyError(Exception):
    pass

try:
    raise MyError("Custom error occurred")
except MyError as e:
    print(e)
```

## Extra: Best Practices
- Catch specific exceptions for better error handling.
- Use `finally` for resource cleanup.
- Document custom exceptions for clarity.