# ## **15. Python Modules and Packages**  

# Python **modules** and **packages** help organize and reuse code efficiently.

# ---

# ## **1️⃣ What is a Module?**
# A **module** is a single Python file (`.py`) that contains reusable code (functions, variables, classes).

# 🔹 **Example: Creating a Simple Module (`math_operations.py`)**
# ```python
# # math_operations.py (Module)
# def add(a, b):
#     return a + b

# def subtract(a, b):
#     return a - b
# ```

# 🔹 **Importing and Using the Module**
# ```python
# import math_operations

# print(math_operations.add(5, 3))      # Output: 8
# print(math_operations.subtract(10, 4)) # Output: 6
# ```

# ---

# ## **2️⃣ Different Ways to Import Modules**
# ### **1. Import the Whole Module**
# ```python
# import math_operations
# print(math_operations.add(2, 3))  # Output: 5
# ```

# ### **2. Import Specific Functions**
# ```python
# from math_operations import add
# print(add(2, 3))  # Output: 5
# ```

# ### **3. Import with an Alias**
# ```python
# import math_operations as mo
# print(mo.add(2, 3))  # Output: 5
# ```

# ### **4. Import Everything (`*`)**
# ```python
# from math_operations import *
# print(add(2, 3))  # Output: 5
# ```
# ⚠ **Warning:** This is not recommended because it may overwrite existing function names.

# ---

# ## **3️⃣ Built-in Python Modules**
# Python provides many built-in modules like `math`, `random`, `os`, `sys`, etc.

# 🔹 **Example: Using the `math` Module**
# ```python
# import math

# print(math.sqrt(16))  # Output: 4.0
# print(math.factorial(5))  # Output: 120
# ```

# 🔹 **Example: Using the `random` Module**
# ```python
# import random

# print(random.randint(1, 10))  # Output: Random number between 1 and 10
# ```

# ---

# ## **4️⃣ What is a Package?**
# A **package** is a collection of modules inside a folder with an `__init__.py` file.  
# Packages help organize larger programs.

# 🔹 **Example: Creating a Package Structure**
# ```
# my_package/
# │── __init__.py  (Makes it a package)
# │── math_operations.py
# │── string_operations.py
# ```

# 🔹 **Example: Importing from a Package**
# ```python
# from my_package import math_operations
# print(math_operations.add(2, 3))  # Output: 5
# ```

# ---

# ## **5️⃣ Installing and Using External Packages**
# Python has a package manager called `pip` for installing third-party libraries.

# 🔹 **Example: Installing a Package**
# ```sh
# pip install requests
# ```

# 🔹 **Example: Using an Installed Package**
# ```python
# import requests

# response = requests.get("https://api.github.com")
# print(response.status_code)  # Output: 200
# ```

# ---

# ## **6️⃣ Checking Installed Modules and Packages**
# 🔹 **List all installed packages**
# ```sh
# pip list
# ```

# 🔹 **Check details of a specific package**
# ```sh
# pip show requests
# ```

# 🔹 **Uninstall a package**
# ```sh
# pip uninstall requests
# ```

# ---

# ## **🔟 Recap**
# | Concept | Description |
# |---------|------------|
# | **Module** | A single Python file (`.py`) with functions and classes |
# | **Package** | A folder containing multiple modules and an `__init__.py` file |
# | **Importing** | `import module_name` or `from module_name import function` |
# | **Built-in Modules** | `math`, `random`, `os`, `sys`, etc. |
# | **Third-Party Modules** | Install using `pip install package_name` |

# ---

# 🚀 **Next Steps: Do you want to move to the next topic: Python Object-Oriented Programming (OOP)?**