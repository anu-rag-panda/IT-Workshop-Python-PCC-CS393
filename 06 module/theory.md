# Tuples in Python

## Introduction
A tuple is an immutable, ordered collection of elements. Tuples are similar to lists, but unlike lists, their elements cannot be changed after creation. Tuples are defined using parentheses `()`.

## Accessing Tuples
Elements in a tuple can be accessed using indexing and slicing, similar to lists.

## Operations on Tuples
- **Concatenation:** Combine two tuples using `+`.
- **Repetition:** Repeat a tuple using `*`.
- **Membership:** Check if an element exists using `in`.
- **Length:** Use `len()` to get the number of elements.

## Working with Tuples
Tuples can store heterogeneous data types. They are commonly used for fixed collections of items, such as coordinates or database records.

## Functions and Methods
- **Built-in Functions:** `len()`, `max()`, `min()`, `sum()`, `sorted()`
- **Tuple Methods:** `.count(value)`, `.index(value)`

## Example
```python
t = (1, 2, 3, 4)
print(t[0])        # Accessing first element
print(t[1:3])      # Slicing
print(len(t))      # Length
print(t.count(2))  # Counting occurrences
```