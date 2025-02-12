# ## **9. Modules and Packages in Python**  

# **Modules** and **packages** are essential for organizing and reusing code. A **module** is a file containing Python code, while a **package** is a collection of modules. Python allows you to **import** and use these to keep your code clean and modular.

# ---

# ### **1️⃣ What is a Module?**  
# A **module** is a Python file containing functions, classes, and variables. It can also include runnable code.

# ### **Creating and Using a Module**

# 1. **Create a Module**: Save your Python code in a file, e.g., `math_functions.py`.
# ```python
# # math_functions.py
# def add(a, b):
#     return a + b

# def subtract(a, b):
#     return a - b
# ```

# 2. **Import and Use the Module**: 
# ```python
# # main.py
# import math_functions

# result1 = math_functions.add(5, 3)
# result2 = math_functions.subtract(10, 4)

# print(result1)  # Output: 8
# print(result2)  # Output: 6
# ```

# ### **Alternative: Import Specific Functions**
# You can import specific functions from a module using the `from` keyword.

# ```python
# from math_functions import add

# result = add(5, 3)
# print(result)  # Output: 8
# ```

# ---

# ### **2️⃣ Built-in Modules in Python**  
# Python comes with several built-in modules that provide useful functionality.

# ### **Example: Using `math` Module**  
# The `math` module provides mathematical functions.

# ```python
# import math

# print(math.sqrt(16))  # Output: 4.0
# print(math.pi)        # Output: 3.141592653589793
# ```

# ### **Example: Using `random` Module**  
# The `random` module provides functions to generate random numbers.

# ```python
# import random

# print(random.randint(1, 100))  # Random integer between 1 and 100
# print(random.choice([1, 2, 3, 4, 5]))  # Random choice from list
# ```

# ---

# ### **3️⃣ What is a Package?**  
# A **package** is a collection of modules organized in directories. Each directory contains a special `__init__.py` file, which makes it a Python package.

# ### **Creating a Package**
# 1. **Create the Package Structure:**
# ```
# my_package/
#     __init__.py
#     module1.py
#     module2.py
# ```

# 2. **Code Inside Modules:**
# ```python
# # my_package/module1.py
# def greet():
#     print("Hello from module1!")

# # my_package/module2.py
# def farewell():
#     print("Goodbye from module2!")
# ```

# 3. **Import and Use the Package:**
# ```python
# from my_package import module1, module2

# module1.greet()   # Output: Hello from module1!
# module2.farewell()  # Output: Goodbye from module2!
# ```

# ---

# ### **4️⃣ Using `__init__.py` in Packages**  
# The `__init__.py` file is essential for defining a package. It can be empty, but it is used to initialize the package and its modules.

# ### **Example: `__init__.py` File**
# ```python
# # my_package/__init__.py
# from .module1 import greet
# from .module2 import farewell
# ```

# You can now import the functions directly from the package.

# ```python
# from my_package import greet, farewell

# greet()    # Output: Hello from module1!
# farewell() # Output: Goodbye from module2!
# ```

# ---

# ### **5️⃣ Python Standard Library Modules**  
# Python provides many standard libraries for various tasks, such as file handling, networking, and more.

# #### **Example: Using `os` Module**  
# The `os` module allows you to interact with the operating system.

# ```python
# import os

# print(os.getcwd())  # Get the current working directory
# os.mkdir("new_folder")  # Create a new directory
# ```

# ---

# ### **6️⃣ Installing External Packages (Using `pip`)**  
# To install external Python packages, use `pip`, Python's package manager.

# #### **Example: Installing `requests` Package**  
# The `requests` module is used to make HTTP requests.

# ```bash
# pip install requests
# ```

# #### **Example: Using `requests` to Fetch Data**
# ```python
# import requests

# response = requests.get("https://api.github.com")
# print(response.json())  # Print the JSON response
# ```

# ---

# ### **7️⃣ Managing Python Packages with `venv` (Virtual Environments)**  
# A **virtual environment** is a self-contained directory that contains a Python installation and can have its own set of installed packages.

# #### **Creating a Virtual Environment**
# ```bash
# python -m venv myenv
# ```

# #### **Activating the Virtual Environment**
# - **Windows**:  
# ```bash
# myenv\Scripts\activate
# ```
# - **Mac/Linux**:  
# ```bash
# source myenv/bin/activate
# ```

# #### **Installing Packages Inside Virtual Environment**
# ```bash
# pip install requests
# ```

# #### **Deactivating the Virtual Environment**
# ```bash
# deactivate
# ```

# ---

# ## **8️⃣ Using `pip freeze` to List Installed Packages**  
# To list all installed packages in the current environment, use the `pip freeze` command.

# ```bash
# pip freeze
# ```

# ---

# ## **Recap**
# 🔹 **Module** – A file containing Python code (functions, variables, classes).  
# 🔹 **Package** – A collection of modules stored in directories, with `__init__.py`.  
# 🔹 **Built-in Modules** – Python comes with many modules like `math`, `random`, `os`.  
# 🔹 **External Packages** – Can be installed using `pip`.  
# 🔹 **Virtual Environments** – Allow you to manage project-specific dependencies.  

# Would you like to move on to the **next topic: Working with Databases in Python?** 🚀