# ## **14. Python Exception Handling**  

# Exception handling in Python is used to **manage errors** that occur during program execution, preventing the program from crashing unexpectedly.

# ---

# ## **1️⃣ What is an Exception?**  
# An **exception** is an error that occurs during execution and disrupts the normal flow of a program.

# 🔹 **Example: Division by Zero Error**
# ```python
# x = 10 / 0  # This will raise a ZeroDivisionError
# ```
# ✅ **Output:**
# ```
# ZeroDivisionError: division by zero
# ```

# ---

# ## **2️⃣ Handling Exceptions using `try-except`**  
# We use a `try-except` block to handle exceptions gracefully.

# 🔹 **Example: Handling Division by Zero**
# ```python
# try:
#     x = 10 / 0  # Code that may cause an error
# except ZeroDivisionError:
#     print("Error: Cannot divide by zero!")
# ```
# ✅ **Output:**
# ```
# Error: Cannot divide by zero!
# ```

# ---

# ## **3️⃣ Handling Multiple Exceptions**
# We can handle different types of exceptions separately.

# 🔹 **Example: Handling Multiple Errors**
# ```python
# try:
#     num = int(input("Enter a number: "))  # User input
#     result = 10 / num
# except ZeroDivisionError:
#     print("Error: Cannot divide by zero!")
# except ValueError:
#     print("Error: Invalid input! Please enter a number.")
# ```

# ✅ **Possible Outputs:**
# ```
# Input: 0 → Error: Cannot divide by zero!
# Input: abc → Error: Invalid input! Please enter a number.
# ```

# ---

# ## **4️⃣ Catching All Exceptions (`Exception`)**
# If we are unsure about the error type, we can use `Exception`.

# 🔹 **Example: Catching Any Error**
# ```python
# try:
#     x = 10 / int(input("Enter a number: "))
# except Exception as e:
#     print("An error occurred:", e)
# ```

# ✅ **Output (for invalid input):**
# ```
# An error occurred: invalid literal for int() with base 10: 'abc'
# ```

# ---

# ## **5️⃣ Using `else` with `try-except`**
# The `else` block runs only if **no exception** occurs.

# 🔹 **Example:**
# ```python
# try:
#     num = int(input("Enter a number: "))
#     result = 10 / num
# except ZeroDivisionError:
#     print("Error: Cannot divide by zero!")
# else:
#     print("Division successful:", result)
# ```

# ✅ **Output (if input is valid):**
# ```
# Division successful: 2.0  (Input: 5)
# ```

# ---

# ## **6️⃣ Using `finally` (Always Executes)**
# The `finally` block runs **no matter what happens**, even if an exception occurs.

# 🔹 **Example:**
# ```python
# try:
#     file = open("data.txt", "r")
#     content = file.read()
# except FileNotFoundError:
#     print("Error: File not found!")
# finally:
#     print("Closing the program.")
# ```

# ✅ **Output:**
# ```
# Error: File not found!
# Closing the program.
# ```

# ---

# ## **7️⃣ Raising Custom Exceptions (`raise`)**
# We can manually **raise exceptions** using the `raise` keyword.

# 🔹 **Example: Raising an Exception**
# ```python
# age = int(input("Enter your age: "))
# if age < 18:
#     raise ValueError("You must be at least 18 years old!")
# else:
#     print("Access granted.")
# ```

# ✅ **Output (if age < 18):**
# ```
# ValueError: You must be at least 18 years old!
# ```

# ---

# ## **8️⃣ Creating Custom Exception Classes**
# We can create **custom exceptions** by inheriting from the `Exception` class.

# 🔹 **Example: Custom Exception**
# ```python
# class AgeError(Exception):
#     pass

# try:
#     age = int(input("Enter your age: "))
#     if age < 18:
#         raise AgeError("You are too young!")
# except AgeError as e:
#     print("Custom Error:", e)
# ```

# ✅ **Output:**
# ```
# Custom Error: You are too young!
# ```

# ---

# ## **🔟 Recap: Key Exception Handling Techniques**
# | Method | Purpose |
# |--------|---------|
# | `try-except` | Handle exceptions |
# | `except Exception` | Catch any error |
# | `else` | Runs if no exception occurs |
# | `finally` | Always executes, even after an exception |
# | `raise` | Manually trigger an exception |
# | Custom Exception | Define your own exception |

# ---

# 🚀 **Next Steps: Do you want to move to the next topic: Python Modules and Packages?**