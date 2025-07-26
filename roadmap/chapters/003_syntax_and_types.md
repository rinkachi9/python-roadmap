# Syntax and data types

This chapter introduces the foundational building blocks of Python: its syntax and built-in data types. Understanding these is essential for writing valid and efficient Python code.

---

## ✅ Syntax overview

Python emphasizes readability and simplicity. Here's what makes its syntax unique:

### 1. **Indentation-Based Blocks**

* Python uses **indentation instead of braces** to define code blocks.
* The standard is 4 spaces per indentation level.

```python
if condition:
    do_something()
else:
    do_something_else()
```

### 2. **Statements and line structure**

* Each statement typically goes on its own line.
* Use `\` to break long statements.

```python
total = a + b + \
        c + d
```

### 3. **Comments**

* Single-line comment: `# This is a comment`
* Multi-line comment (conventionally): triple quotes `'''` or `"""`

```python
# This is a single-line comment
""" This is a
multi-line comment """
```

### 4. **Case Sensitivity**

* Python is case-sensitive: `Variable`, `variable`, and `VARIABLE` are different.

### 5. **Identifiers**

* Must start with a letter or underscore.
* Can contain letters, digits, and underscores.
* Cannot use keywords as names (e.g., `class`, `for`, `True`, etc.).

---

## 🧮 Data types

Python supports several built-in data types categorized into:

### 🔢 Basic types

| Type    | Example       | Description                      |
| ------- | ------------- | -------------------------------- |
| `int`   | `x = 42`      | Integer numbers                  |
| `float` | `x = 3.14`    | Decimal numbers                  |
| `bool`  | `x = True`    | Boolean logic: `True` or `False` |
| `str`   | `x = "Hello"` | Text (string) data               |
| `None`  | `x = None`    | Represents the absence of value  |

### 📦 Collection types

| Type    | Example            | Description                     |
| ------- | ------------------ | ------------------------------- |
| `list`  | `[1, 2, 3]`        | Ordered, mutable collection     |
| `tuple` | `(1, 2, 3)`        | Ordered, immutable collection   |
| `set`   | `{1, 2, 3}`        | Unordered, unique elements only |
| `dict`  | `{"key": "value"}` | Key-value mappings              |

### 📌 Notes:

* Strings are immutable.
* Lists can contain mixed data types.
* Dictionaries require keys to be immutable (e.g., str, int, tuple).

---

## 🔄 Type conversion

Python allows casting between types:

```python
int("10")       # Converts string to int
float("3.14")   # Converts string to float
str(123)        # Converts int to string
list("abc")     # Converts string to list: ['a', 'b', 'c']
```

---

## 🧪 Type checking

Use `type()` and `isinstance()`:

```python
x = [1, 2, 3]
print(type(x))               # <class 'list'>
print(isinstance(x, list))   # True
```

---

## 🧠 Summary

* Python syntax is simple, readable, and whitespace-sensitive.
* There are multiple built-in types for numbers, text, collections, and control.
* Type conversion and inspection are explicit and encouraged.

This foundation prepares you to work with functions, conditionals, loops, and more advanced topics.
