# Importing modules
import math
import random

# Math module usage
print("Square root of 25:", math.sqrt(25))
print("Value of pi:", math.pi)

# Random module usage
print("Random integer (1-100):", random.randint(1, 100))
print("Random choice from list:", random.choice(['apple', 'banana', 'cherry']))

# Printing on screen
print("Hello, Python Modules!")

# Reading data from keyboard
name = input("Enter your name: ")
print("Welcome,", name)

# Opening and writing to a file
with open('test.txt', 'w') as f:
    f.write("This is a test file.\n")
    f.write("Written using Python.\n")

# Reading from a file
with open('test.txt', 'r') as f:
    content = f.read()
    print("File content:\n", content)

# Example function in a module
def add(a, b):
    return a + b

print("Sum using function:", add(5, 7))