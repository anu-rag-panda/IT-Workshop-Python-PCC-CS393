# Defining a function
def greet(name):
    print(f"Hello, {name}!")

# Calling a function
greet("Alice")

# Types of functions
def add(a, b):
    return a + b

print("Sum:", add(5, 7))

# Function arguments
def info(name, age=18):
    print(f"Name: {name}, Age: {age}")

info("Bob")
info("Carol", 22)

def show_args(*args, **kwargs):
    print("Args:", args)
    print("Kwargs:", kwargs)

show_args(1, 2, 3, x=10, y=20)

# Anonymous function
square = lambda x: x * x
print("Square of 4:", square(4))

# Global and local variables
x = 5
def change_global():
    global x
    x = 10

change_global()
print("Global x:", x)

def local_example():
    y = 20
    print("Local y:", y)

local_example()