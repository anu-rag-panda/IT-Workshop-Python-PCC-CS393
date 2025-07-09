# Module 5: Lists in Python

A list is a collection of items that is:

- Ordered
- Mutable (can be changed)
- Heterogeneous (can store different types)

Lists are defined using square brackets `[]` .

```python
fruits = ["apple", "banana", "cherry"]
numbers = [1, 2, 3, 4, 5]
mixed = [1, "apple", True]
```

## 5.1 Accessing List Elements

```python
fruits = ["apple", "banana", "cherry"]
print(fruits[0])     # apple
print(fruits[-1])    # cherry
print(fruits[1:3])   # ['banana', 'cherry']
```

## 5.2 Basic List Operations

| **Operation** | **Example**       | **Result**     |
| ------------- | ----------------- | -------------- |
| Concatenation | `[1, 2] + [3, 4]` | `[1, 2, 3, 4]` |
| Repetition    | `[0] * 3`         | `[0, 0, 0]`    |
| Membership    | `2 in [1, 2, 3]`  | `True`         |
| Length        | `len([1, 2, 3])`  | `3`            |

## 5.3 List Methods

| **Method**     | **Description**                               |
| -------------- | --------------------------------------------- |
| `append(x)`    | Adds an item at the end                       |
| `insert(i, x)` | Inserts item at index `i`                     |
| `extend(iter)` | Extends list with items from another list     |
| `remove(x)`    | Removes first occurrence of item `x`          |
| `pop(i)`       | Removes item at index `i` (default last)      |
| `sort()`       | Sorts the list                                |
| `reverse()`    | Reverses the list                             |
| `index(x)`     | Returns index of first occurrence of item `x` |
| `count(x)`     | Counts how many times `x` appears             |
| `clear()`      | Removes all elements                          |

