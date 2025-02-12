# ## **2. Python Basics (Variables, Data Types, and Operators)**  

# ### **1️⃣ Variables in Python**  
# A **variable** is a container for storing data. In Python, you don't need to 
# declare the type of a variable—it is dynamically assigned.  

# #### **Example:**
# ```python
name = "Alice"   # String
age = 25         # Integer
height = 5.6     # Float
is_student = True  # Boolean

print(name, age, height, is_student)
# ```
# ✅ Output:
# ```
# Alice 25 5.6 True
# ```

# #### **Rules for Naming Variables**  
# ✔ Can contain letters (a-z, A-Z), numbers (0-9), and underscores (_)  
# ✔ Cannot start with a number (`1name` ❌)  
# ✔ Case-sensitive (`name` and `Name` are different)  
# ✔ Should not use Python keywords (`if`, `for`, `class`, etc.)  

# ---

# ### **2️⃣ Data Types in Python**  
# Python has several built-in **data types**:

# | Data Type | Example |
# |-----------|---------|
# | `int`     | `x = 10` |
# | `float`   | `y = 3.14` |
# | `str`     | `name = "Alice"` |
# | `bool`    | `is_happy = True` |
# | `list`    | `fruits = ["apple", "banana", "cherry"]` |
# | `tuple`   | `coordinates = (10, 20, 30)` |
# | `set`     | `unique_numbers = {1, 2, 3, 4, 5}` |
# | `dict`    | `student = {"name": "Alice", "age": 25}` |

# ---

# ### **3️⃣ Type Conversion (Casting)**
# You can convert one data type to another using `int()`, `float()`, `str()`, etc.

# #### **Example:**
# ```python
a = 10      # int
b = "20"    # str

# Convert str to int before addition
sum_value = a + int(b)  

print(sum_value)  # Output: 30
# ```

# ---

# ### **4️⃣ User Input in Python**
# The `input()` function allows users to enter data.

# #### **Example:**
# ```python
name = input("Enter your name: ")
print("Hello, " + name + "!")
# ```
# ✅ Output:
# ```
# Enter your name: Alice
# Hello, Alice!
# ```

# By default, `input()` returns a string. Convert it if needed:
# ```python
age = int(input("Enter your age: "))  # Converts input to int
print("You are", age, "years old.")
# ```

# ---

# ### **5️⃣ Operators in Python**
# Operators are used for performing operations on variables and values.

# #### **A) Arithmetic Operators**
# | Operator | Meaning | Example |
# |----------|---------|---------|
# | `+` | Addition | `5 + 3 = 8` |
# | `-` | Subtraction | `5 - 3 = 2` |
# | `*` | Multiplication | `5 * 3 = 15` |
# | `/` | Division | `5 / 2 = 2.5` |
# | `//` | Floor Division | `5 // 2 = 2` |
# | `%` | Modulus (Remainder) | `5 % 2 = 1` |
# | `**` | Exponentiation | `2 ** 3 = 8` |

# #### **B) Comparison Operators**
# | Operator | Meaning | Example |
# |----------|---------|---------|
# | `==` | Equal to | `5 == 5` (True) |
# | `!=` | Not equal to | `5 != 3` (True) |
# | `>` | Greater than | `5 > 3` (True) |
# | `<` | Less than | `5 < 3` (False) |
# | `>=` | Greater than or equal to | `5 >= 5` (True) |
# | `<=` | Less than or equal to | `5 <= 3` (False) |

# #### **C) Logical Operators**
# | Operator | Meaning | Example |
# |----------|---------|---------|
# | `and` | Returns True if both conditions are True | `(5 > 3) and (10 > 5)` (True) |
# | `or` | Returns True if at least one condition is True | `(5 > 3) or (10 < 5)` (True) |
# | `not` | Reverses the result | `not(5 > 3)` (False) |

# #### **D) Assignment Operators**
# | Operator | Example | Equivalent to |
# |----------|---------|--------------|
# | `=` | `x = 5` | `x = 5` |
# | `+=` | `x += 3` | `x = x + 3` |
# | `-=` | `x -= 3` | `x = x - 3` |
# | `*=` | `x *= 3` | `x = x * 3` |
# | `/=` | `x /= 3` | `x = x / 3` |
# | `//=` | `x //= 3` | `x = x // 3` |
# | `%=` | `x %= 3` | `x = x % 3` |

# ---

# ### **6️⃣ Example Program Using Everything So Far**
# ```python
# Get user input
name = input("Enter your name: ")
age = int(input("Enter your age: "))
# Perform some operations
next_year_age = age + 1
is_adult = age >= 18
# Print the results
print("Hello,", name + "!")
print("Next year, you will be", next_year_age, "years old.")
print("Are you an adult?", is_adult)
# ```
# ✅ **Sample Output:**
# ```
# Enter your name: Alice
# Enter your age: 20
# Hello, Alice!
# Next year, you will be 21 years old.
# Are you an adult? True
# ```

# ---

# This covers **Python Variables, Data Types, User Input, and Operators.**  

# Would you like to move on to the **next topic: Control Flow Statements (if-else, loops)?** 🚀