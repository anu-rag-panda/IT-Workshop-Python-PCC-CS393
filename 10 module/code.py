# Basic exception handling
try:
    num = int(input("Enter an integer: "))
    result = 10 / num
    print("Result:", result)
except ZeroDivisionError:
    print("Error: Division by zero!")
except ValueError:
    print("Error: Invalid input!")
else:
    print("No exception occurred.")
finally:
    print("This block always executes.")

# User defined exception
class NegativeNumberError(Exception):
    pass

try:
    value = int(input("Enter a positive number: "))
    if value < 0:
        raise NegativeNumberError("Negative numbers are not allowed.")
    print("You entered:", value)
except NegativeNumberError as e:
    print("Custom Exception:", e)