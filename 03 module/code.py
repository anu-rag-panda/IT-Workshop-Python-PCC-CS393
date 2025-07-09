# Example of break
print("Using break:")
for char in "Python":
    if char == 'h':
        break
    print(char)

# Example of continue
print("\nUsing continue:")
for num in range(5):
    if num == 2:
        continue
    print(num)

# Example of pass
print("\nUsing pass:")
for i in range(3):
    if i == 1:
        pass  # nothing happens
    print("Loop:", i)
