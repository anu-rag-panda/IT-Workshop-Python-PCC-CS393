# Tuple Introduction
tup = (10, 20, 30, 40, 50)
print("Tuple:", tup)

# Accessing tuples
print("First element:", tup[0])
print("Slice [1:4]:", tup[1:4])

# Operations
tup2 = (60, 70)
concat = tup + tup2
print("Concatenated tuple:", concat)
repeat = tup * 2
print("Repeated tuple:", repeat)
print("Is 30 in tuple?", 30 in tup)
print("Length of tuple:", len(tup))

# Working with tuples
mixed = (1, "apple", 3.14)
print("Mixed tuple:", mixed)

# Functions and Methods
print("Max value:", max(tup))
print("Min value:", min(tup))
print("Sum:", sum(tup))
print("Count of 20:", tup.count(20))
print("Index of 40:", tup.index(40))