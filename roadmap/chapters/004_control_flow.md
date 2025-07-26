Control flow

This chapter covers control flow constructs in Python, including **conditional statements**, **loops**, and **loop
control statements**. These allow your program to make decisions, repeat actions, and manage execution paths
dynamically.

---

## ✅ Conditional statements

Python provides `if`, `elif`, and `else` statements for decision-making.

### Syntax:

```python
if condition:
# block executed if condition is True
elif another_condition:
# block executed if previous condition is False but this is True
else:
# block executed if all above conditions are False
```

### Example:

```python
age = 20
if age < 13:
    print("Child")
elif age < 18:
    print("Teenager")
else:
    print("Adult")
```

### Truthy and falsy values:

In conditions, Python evaluates the **truthiness** of values:

| Value            | Evaluates As |
|------------------|--------------|
| `0`, `0.0`       | False        |
| `None`           | False        |
| `""`, `[]`, `{}` | False        |
| Other values     | True         |

---

## 🔁 Loops

### `for` Loop

Used to iterate over sequences (lists, tuples, strings, ranges, etc).

```python
for item in iterable:
# do something
```

#### Example:

```python
for i in range(5):
    print(i)
```

### `while` Loop

Executes as long as the condition is true.

```python
while condition:
# repeat while condition is True
```

#### Example:

```python
count = 0
while count < 3:
    print("Count:", count)
    count += 1
```

---

## ⚙️ Loop control statements

These are used inside loops to alter the control flow:

### `break`

Exits the current loop immediately.

```python
for i in range(10):
    if i == 5:
        break
    print(i)
```

### `continue`

Skips the rest of the current loop iteration.

```python
for i in range(5):
    if i == 2:
        continue
    print(i)
```

### `pass`

A placeholder that does nothing (used when syntax requires a block).

```python
if True:
    pass  # TODO: implement later
```

---

## 🧪 The `else` clause in loops

Python allows an `else` block after loops, which runs **only if the loop wasn't terminated by `break`.**

```python
for i in range(3):
    print(i)
else:
    print("Loop completed without break")
```

---

## 🔄 Structural pattern matching (`match` / `case`)

Python 3.10 introduced structural pattern matching with `match`/`case` statements.

### Basic Syntax:

```python
match variable:
    case pattern1:
    # block if pattern1 matches
    case pattern2:
    # block if pattern2 matches
    case _:
    # default case
```

### Example – Simple Match:

```python
status_code = 404

match status_code:
    case 200:
        print("OK")
    case 404:
        print("Not Found")
    case 500:
        print("Server Error")
    case _:
        print("Unknown Status")
```

### Example – Complex Match:

```python
command = ("move", 10, 20)

match command:
    case ("move", x, y):
        print(f"Move to coordinates: {x}, {y}")
    case ("stop", ):
        print("Stop command received")
    case _:
        print("Unknown command")
```

### Notes:

* `case _:` acts like `else`
* Supports destructuring and matching by value/type/structure
* Ideal for replacing long `if`/`elif` chains

---

## 🧠 Summary

* `if`/`elif`/`else` controls decision-making.
* `for` and `while` loops handle iteration.
* `break`, `continue`, and `pass` modify loop execution.
* `else` on loops runs when no `break` occurred.
* `match`/`case` enables structural pattern matching (Python 3.10+).

Understanding control flow is fundamental for building all logical structures in Python.
