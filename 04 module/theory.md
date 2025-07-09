# Module 4: String Manipulation in Python

A string is a sequence of characters enclosed in single, double, or triple quotes.

```python
name1 = 'anurag'
name2 = "python"
name3 = """Multi-line
           string"""
```

## 4.1 Accessing Strings

Strings are indexed starting from 0.

```python
text = "Python"
print(text[0])  # P
print(text[-1]) # n (last character)
```

## 4.2 Basic String Operations

| **Operation** | **Example** | **Result** |
|-----------|---------|--------|
| Concatenation | `"Hello " + "World"` | `"Hello World"` |
| Repetition | `"Hi" * 3` | `"HiHiHi"` |
| Membership | `"a" in "apple"` | `True` |
| Length | `len("Python")` | `6` |

## 4.3 String Slicing

```python
text = "Python"
print(text[0:2])   # Py
print(text[2:])    # thon
print(text[:3])    # Pyt
print(text[-3:])   # hon
```

Syntax: `string[start:end:step]`

## 4.4 Common String Methods

| **Method** | **Description** |
|--------|-------------|
| `lower()` | Converts to lowercase |
| `upper()` | Converts to uppercase |
| `strip()` | Removes leading/trailing spaces |
| `replace(old,new)` | Replaces substrings |
| `split()` | Splits string into a list |
| `find()` | Returns index of substring |
| `startswith()` | Checks if string starts with a substring |
| `endswith()` | Checks if string ends with a substring |
| `isalpha()` | Checks if all characters are alphabetic |
| `isdigit()` | Checks if all characters are digits |

