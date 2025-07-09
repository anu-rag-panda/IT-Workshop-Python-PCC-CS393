# Creating and modifying a list
numbers = [10, 20, 30]
numbers.append(40)
numbers.insert(1, 15)
print("Updated List:", numbers)

# Deleting items
numbers.remove(20)
print("After removing 20:", numbers)
popped = numbers.pop()
print("Popped item:", popped)

# Sorting and reversing
marks = [56, 23, 89, 12]
marks.sort()
print("Sorted marks:", marks)
marks.reverse()
print("Reversed:", marks)
