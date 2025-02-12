# ## **5. Functions in Python**  

# A **function** is a reusable block of code that performs a specific task. Functions help in code organization, reusability, and modularity.  

# ### **Types of Functions in Python**  
# ✅ **Built-in Functions** – Predefined functions like `print()`, `len()`, `type()`, etc.  
# ✅ **User-defined Functions** – Created by users using the `def` keyword  
# ✅ **Lambda Functions** – Anonymous functions using the `lambda` keyword  
# ✅ **Recursive Functions** – Functions that call themselves  

# ---

# ## **1️⃣ Creating and Using Functions**  
# A function is defined using the `def` keyword.

# ### **Basic Function**
# ```python
def greet():
    print("Hello, welcome to Python!")

greet()  # Calling the function
# ```
# ✅ **Output:**  
# ```
# Hello, welcome to Python!
# ```

# ---

# ## **2️⃣ Function with Parameters and Arguments**  
# Parameters allow functions to accept inputs.

# ### **Example: Function with Parameters**
# ```python
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")  # Passing "Alice" as an argument
# ```
# ✅ **Output:**  
# ```
# Hello, Alice!
# ```

# ---

# ### **Example: Function with Multiple Parameters**
# ```python
def add_numbers(a, b):
    return a + b  # Returning the sum

result = add_numbers(5, 10)
print("Sum:", result)
# ```
# ✅ **Output:**  
# ```
# Sum: 15
# ```

# ---

# ## **3️⃣ Default and Keyword Arguments**
# ✅ **Default Arguments** – Assigns a default value if no argument is provided  
# ✅ **Keyword Arguments** – Specifies arguments by parameter name  

# ### **Example: Default Argument**
# ```python
def greet(name="Guest"):
    print(f"Hello, {name}!")

greet()       # Uses default value "Guest"
greet("Bob")  # Uses provided value "Bob"
# ```
# ✅ **Output:**  
# ```
# Hello, Guest!
# Hello, Bob!
# ```

# ---

# ### **Example: Keyword Arguments**
# ```python
def display_info(name, age):
    print(f"Name: {name}, Age: {age}")

display_info(age=25, name="Alice")  # Order does not matter
# ```
# ✅ **Output:**  
# ```
# Name: Alice, Age: 25
# ```

# ---

# ## **4️⃣ Return Statement in Functions**  
# Functions can return values using the `return` statement.

# ### **Example: Function Returning a Value**
# ```python
def square(num):
    return num * num  # Returns the square of num

result = square(4)
print("Square:", result)
# ```
# ✅ **Output:**  
# ```
# Square: 16
# ```

# ---

# ## **5️⃣ Lambda Functions (Anonymous Functions)**  
# A **lambda function** is a short, single-line function with no name.

# ### **Syntax:**  
# ```python
# lambda arguments: expression
# ```

# ### **Example: Lambda Function**
# ```python
square = lambda x: x * x
print(square(5))
# ```
# ✅ **Output:**  
# ```
# 25
# ```

# ---

# ### **Example: Lambda with Multiple Parameters**
# ```python
add = lambda a, b: a + b
print(add(3, 7))
# ```
# ✅ **Output:**  
# ```
# 10
# ```

# ---

# ## **6️⃣ Recursive Functions**  
# A **recursive function** is a function that calls itself.

# ### **Example: Factorial Using Recursion**
# ```python
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))  # 5 * 4 * 3 * 2 * 1 = 120
# ```
# ✅ **Output:**  
# ```
# 120
# ```

# ---

# ## **Example Program: Function to Find Maximum of Three Numbers**
# ```python
def find_max(a, b, c):
    return max(a, b, c)

print(find_max(10, 20, 15))  # Output: 20
# ```

# ---

# ## **Recap**
# 🔹 **Built-in Functions** – Already available in Python  
# 🔹 **User-defined Functions** – Defined using `def`  
# 🔹 **Parameters & Arguments** – Input values to functions  
# 🔹 **Default & Keyword Arguments** – Provide default values and flexibility  
# 🔹 **Lambda Functions** – Short, one-liner anonymous functions  
# 🔹 **Recursive Functions** – Functions that call themselves  

# Would you like to move on to the **next topic: Object-Oriented Programming (OOP) in Python?** 🚀