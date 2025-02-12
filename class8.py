# ## **8. Exception Handling in Python**  

# **Exception Handling** in Python allows us to deal with runtime errors, preventing the program from crashing unexpectedly. Python provides a robust mechanism to handle errors using the `try`, `except`, `else`, and `finally` blocks.

# ---

# ### **Key Concepts of Exception Handling:**  
# ✅ **Try Block** – Contains code that might raise an exception.  
# ✅ **Except Block** – Handles the exception if it occurs.  
# ✅ **Else Block** – Executes if no exception occurs.  
# ✅ **Finally Block** – Always executes, regardless of whether an exception occurs.  

# ---

# ## **1️⃣ Basic Try and Except**  
# The `try` block tests code for errors, and the `except` block catches them.

# ### **Example: Basic Exception Handling**
# ```python
# try:
#     result = 10 / 0  # This will raise a ZeroDivisionError
# except ZeroDivisionError:
#     print("Cannot divide by zero!")
# ```
# ✅ **Output:**  
# ```
# Cannot divide by zero!
# ```

# ---

# ## **2️⃣ Multiple Except Blocks**  
# You can handle different types of exceptions using multiple `except` blocks.

# ### **Example: Handling Multiple Exceptions**
# ```python
# try:
#     num1 = int(input("Enter a number: "))
#     result = 10 / num1
# except ZeroDivisionError:
#     print("Cannot divide by zero!")
# except ValueError:
#     print("Invalid input! Please enter a valid number.")
# ```
# ✅ **Output (if user inputs `0`):**  
# ```
# Cannot divide by zero!
# ```

# ---

# ## **3️⃣ Catching Multiple Exceptions in One Block**  
# You can catch multiple exceptions in a single `except` block by specifying them as a tuple.

# ### **Example: Catching Multiple Exceptions**
# ```python
# try:
#     num1 = int(input("Enter a number: "))
#     result = 10 / num1
# except (ZeroDivisionError, ValueError) as e:
#     print(f"Error: {e}")
# ```

# ---

# ## **4️⃣ Using Else Block**  
# The `else` block runs if no exception occurs in the `try` block.

# ### **Example: Using Else Block**
# ```python
# try:
#     num1 = int(input("Enter a number: "))
#     result = 10 / num1
# except (ZeroDivisionError, ValueError) as e:
#     print(f"Error: {e}")
# else:
#     print(f"Result is: {result}")
# ```

# ---

# ## **5️⃣ Using Finally Block**  
# The `finally` block always executes, no matter what, even if an exception was raised or not. It is often used for cleanup operations (e.g., closing files or network connections).

# ### **Example: Using Finally Block**
# ```python
# try:
#     num1 = int(input("Enter a number: "))
#     result = 10 / num1
# except (ZeroDivisionError, ValueError) as e:
#     print(f"Error: {e}")
# else:
#     print(f"Result is: {result}")
# finally:
#     print("Execution completed!")
# ```
# ✅ **Output:**  
# ```
# Enter a number: 2
# Result is: 5.0
# Execution completed!
# ```

# ---

# ## **6️⃣ Raising Exceptions Manually**  
# You can manually raise exceptions using the `raise` keyword.

# ### **Example: Raising an Exception**
# ```python
# def check_age(age):
#     if age < 18:
#         raise ValueError("Age must be at least 18!")
#     else:
#         print("You are eligible.")

# try:
#     check_age(16)
# except ValueError as e:
#     print(f"Error: {e}")
# ```
# ✅ **Output:**  
# ```
# Error: Age must be at least 18!
# ```

# ---

# ## **7️⃣ Custom Exceptions**  
# You can create your own exceptions by subclassing Python's built-in `Exception` class.

# ### **Example: Creating a Custom Exception**
# ```python
# class AgeLimitError(Exception):
#     def __init__(self, message):
#         self.message = message
#         super().__init__(self.message)

# def check_age(age):
#     if age < 18:
#         raise AgeLimitError("Age must be at least 18!")
#     else:
#         print("You are eligible.")

# try:
#     check_age(16)
# except AgeLimitError as e:
#     print(f"Custom Error: {e}")
# ```
# ✅ **Output:**  
# ```
# Custom Error: Age must be at least 18!
# ```

# ---

# ## **8️⃣ The `assert` Statement**  
# The `assert` statement helps to check if a condition is true. If the condition is false, it raises an `AssertionError`.

# ### **Example: Using `assert`**
# ```python
# age = -5
# assert age >= 0, "Age cannot be negative!"  # Raises AssertionError if condition is false
# ```
# ✅ **Output:**  
# ```
# AssertionError: Age cannot be negative!
# ```

# ---

# ## **Example Program: Full Exception Handling**
# ```python
# def divide(a, b):
#     try:
#         result = a / b
#     except ZeroDivisionError:
#         print("Error: Division by zero!")
#     except TypeError:
#         print("Error: Both inputs must be numbers!")
#     else:
#         print(f"Result: {result}")
#     finally:
#         print("Execution finished.")

# divide(10, 2)  # Valid input
# divide(10, 0)  # Division by zero
# divide(10, "5")  # Invalid input type
# ```
# ✅ **Output:**  
# ```
# Result: 5.0
# Execution finished.
# Error: Division by zero!
# Execution finished.
# Error: Both inputs must be numbers!
# Execution finished.
# ```

# ---

# ## **Recap**
# 🔹 **Try Block** – Code that might raise an exception  
# 🔹 **Except Block** – Catches and handles exceptions  
# 🔹 **Else Block** – Executes if no exception occurs  
# 🔹 **Finally Block** – Always executes, for cleanup operations  
# 🔹 **Raise Keyword** – Manually raise exceptions  
# 🔹 **Custom Exceptions** – Create your own error types by subclassing `Exception`  
# 🔹 **Assert Statement** – Checks conditions and raises errors if the condition is false  

# Would you like to move on to the **next topic: Modules and Packages in Python?** 🚀