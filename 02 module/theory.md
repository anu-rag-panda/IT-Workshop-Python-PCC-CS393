# Module 2: Conditional Statements and Looping

## 2.1 Conditional Statements

### `if` Statement

Executes a block only if the condition is true.

```python
x = 10

if x > 5:
    print("x is greater than 5!")
    print(x, "is greater than 5!")
```

### `if-else` Statement

Chooses between two blocks.

```python
x = 3

if x % 2 == 0:
    print("Even")
else:
    print("Odd")
```

### `if-elif-else` (Ladder)

Multiple conditions.

```python
marks = 85

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 60:
    print("Grade C")
else:
    print("Fail")

```

### Nested `if`

An `if` inside another `if`.

```python
x = 15
if x > 10:
    if x < 20:
        print("x is between 10 and 20")

```

## 2.2 Looping Statements

### `for` Loop

Used to iterate over a sequence (list, string, etc.)

```python
for i in range(5):
    print(i)
```

### `while` Loop

Executes as long as the condition is true.

```python
count = 0
while count < 5:
    print(count)
    count += 1

```

### `Nested Loops`

Loops inside loops.

```python
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i} * {j} = {i*j}") # f is called f-string, short for formatted string literal.

```

