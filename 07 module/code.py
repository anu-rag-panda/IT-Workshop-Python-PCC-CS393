# Dictionary Introduction
d = {'name': 'Alice', 'age': 25, 'city': 'Kolkata'}
print("Dictionary:", d)

# Accessing values
print("Name:", d['name'])
print("Age:", d.get('age'))
print("Country (default):", d.get('country', 'India'))

# Working with dictionaries
d['age'] = 26  # Update value
d['profession'] = 'Engineer'  # Add new key-value
del d['city']  # Delete key
print("Updated dictionary:", d)

# Iterating
for key in d:
    print(f"{key}: {d[key]}")

for key, value in d.items():
    print(f"{key} => {value}")

# Properties and methods
print("Keys:", list(d.keys()))
print("Values:", list(d.values()))
print("Length:", len(d))
print("Pop 'age':", d.pop('age'))
print("After pop:", d)
d.clear()
print("After clear:", d)