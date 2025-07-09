# Module 3: Control Statements — `break`, `continue`, `pass`

Control statements are used to alter the flow of execution inside loops or conditionals.

## 3.1 `break` Statement

- Terminates the loop immediately.

- Control moves to the statement after the loop.

Example:

```python
for i in range(1, 10):
    if i == 5:
        break
    print(i)

```

Output: `1 2 3 4`

## 3.2 `continue` Statement

Skips the current iteration and jumps to the next iteration of the loop.

Example:

```python
for i in range(1, 6):
    if i == 3:
        continue
    print(i)

```

Output: `1 2 4 5`

## 3.3 pass Statement

Acts as a placeholder. Does nothing.

Used when a statement is syntactically required but you don’t want any command to execute.

Example:

```python
for i in range(3):
    pass  # placeholder for future code

if True:
    pass

```
