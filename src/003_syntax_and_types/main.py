# =====================================
# Syntax and data types
# =====================================

# --- Comments ---
# This is a single-line comment

"""
This is a multi-line comment
Often used for documentation
"""

# --- Variables and Basic Types ---

# Integers and floats
integer_number = 10          # int
decimal_number = 3.14        # float

# Boolean values
is_active = True             # bool
is_disabled = False

# String (text)
message = "Hello, Python!"   # str

# None - represents the absence of a value
empty_value = None           # NoneType

# --- Type Checking ---
print(type(integer_number))          # <class 'int'>
print(isinstance(message, str))      # True

# --- Type Conversion (Casting) ---
number_str = "42"
converted_number = int(number_str)   # from str to int
print(converted_number + 10)         # 52

float_str = "3.14"
converted_float = float(float_str)   # from str to float
print(converted_float * 2)           # 6.28

# --- String Operations ---
greeting = "Hello"
name = "Alice"

# Concatenation
full_greeting = greeting + ", " + name + "!"
print(full_greeting)

# f-string interpolation
print(f"{greeting}, {name}! Welcome.")

# --- Collections ---

# List: ordered, mutable, allows duplicates
fruits = ["apple", "banana", "cherry"]
fruits.append("date")
print(fruits)

# Tuple: ordered, immutable
coordinates = (10.5, 20.3)
print(coordinates)

# Set: unordered, no duplicates
unique_numbers = {1, 2, 3, 3, 2}
print(unique_numbers)  # {1, 2, 3}

# Dictionary: key-value pairs
person = {
    "name": "Alice",
    "age": 30,
    "is_member": True
}
print(person["name"])   # Alice

# --- Control Flow ---

# if/elif/else structure
age = 18
if age >= 18:
    print("Adult")
elif age >= 13:
    print("Teen")
else:
    print("Child")

# --- Loop: for ---
print("Loop through list:")
for fruit in fruits:
    print(fruit)

# --- Loop: while ---
count = 0
while count < 3:
    print("Counting:", count)
    count += 1

# --- Loop Control ---
for i in range(5):
    if i == 3:
        break       # exits the loop when i is 3
    if i == 1:
        continue    # skips this iteration
    print("i =", i)

# --- Function Example ---
def greet(name: str) -> str:
    """Returns a greeting string for the given name."""
    return f"Hello, {name}!"

print(greet("Bob"))
