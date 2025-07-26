# ==========================================
# Control flow: conditionals & loops
# ==========================================

# --- IF / ELIF / ELSE ---
age = 20

if age < 13:
    print("Child")
elif age < 18:
    print("Teenager")
else:
    print("Adult")

# Evaluating truthiness
value = []
if value:
    print("Non-empty list")
else:
    print("Empty list")  # This will be printed

# --- FOR LOOP with RANGE ---
print("\nFor loop with range:")
for i in range(5):
    print("i =", i)

# --- FOR LOOP over list ---
fruits = ["apple", "banana", "cherry"]
print("\nIterating over list:")
for fruit in fruits:
    print(fruit)

# --- WHILE LOOP ---
print("\nWhile loop example:")
count = 0
while count < 3:
    print("Count is:", count)
    count += 1

# --- BREAK & CONTINUE ---
print("\nUsing break and continue:")
for i in range(5):
    if i == 2:
        continue  # Skip this iteration
    if i == 4:
        break     # Exit loop when i is 4
    print("Loop value:", i)

# --- PASS STATEMENT ---
condition = True
if condition:
    pass  # Placeholder for future code

# --- ELSE IN LOOPS ---
print("\nFor-else demonstration:")
for i in range(3):
    print(i)
else:
    print("Loop completed normally")

print("\nFor-else with break:")
for i in range(3):
    if i == 1:
        break
    print(i)
else:
    print("This won't be printed due to break")

# --- MATCH / CASE (Python 3.10+) ---
print("\nMatch/case demonstration:")

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

# Matching complex structures
command = ("move", 10, 20)

match command:
    case ("move", x, y):
        print(f"Move to coordinates: {x}, {y}")
    case ("stop",):
        print("Stop command received")
    case _:
        print("Unknown command")

# Type-based match example
value = [1, 2, 3]

match value:
    case list():
        print("It's a list!")
    case dict():
        print("It's a dictionary!")
    case _:
        print("Unknown type")

# --- Summary Output ---
print("\nControl flow demo completed.")
