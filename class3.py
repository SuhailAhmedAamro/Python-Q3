# ## **3. Control Flow Statements in Python**  

# Control flow statements allow us to make decisions and repeat actions in our programs. There are 
# **three main types** of control flow statements in Python:  

# ✅ **Conditional Statements (`if`, `elif`, `else`)** – Decision-making  
# ✅ **Loops (`for`, `while`)** – Repeating tasks  
# ✅ **Loop Control Statements (`break`, `continue`, `pass`)** – Controlling loops  

# ---

# ## **1️⃣ Conditional Statements (`if`, `elif`, `else`)**  
# Conditional statements help in **decision-making** by executing different blocks of code based on conditions.

# ### **Syntax:**
# ```python
# if condition:
#     # Code to execute if condition is True
# elif another_condition:
#     # Code to execute if previous condition is False but this one is True
# else:
#     # Code to execute if all conditions are False
# ```

# ### **Example 1: Simple `if` Statement**
# ```python
# age = 20

# if age >= 18:
#     print("You are an adult.")
# ```
# ✅ **Output:**
# ```
# You are an adult.
# ```

# ---

# ### **Example 2: `if-else` Statement**
# ```python
# num = int(input("Enter a number: "))

# if num % 2 == 0:
#     print("Even number")
# else:
#     print("Odd number")
# ```
# ✅ **Sample Output:**
# ```
# Enter a number: 7
# Odd number
# ```

# ---

# ### **Example 3: `if-elif-else` (Multiple Conditions)**
# ```python
# score = int(input("Enter your score: "))

# if score >= 90:
#     print("Grade: A")
# elif score >= 80:
#     print("Grade: B")
# elif score >= 70:
#     print("Grade: C")
# else:
#     print("Grade: F")
# ```
# ✅ **Sample Output:**
# ```
# Enter your score: 85
# Grade: B
# ```

# ---

# ## **2️⃣ Loops in Python**
# Loops are used to execute a block of code **multiple times**.

# ✅ `for` loop – Iterates over a sequence (list, tuple, string, etc.)  
# ✅ `while` loop – Runs as long as a condition is `True`  

# ---

# ### **A) `for` Loop**  
# The `for` loop is used to iterate over a sequence (like a list, tuple, or string).  

# #### **Example 1: Using `for` Loop with a List**
# ```python
# fruits = ["apple", "banana", "cherry"]

# for fruit in fruits:
#     print(fruit)
# ```
# ✅ **Output:**
# ```
# apple
# banana
# cherry
# ```

# ---

# #### **Example 2: Using `range()` in `for` Loop**
# ```python
# for i in range(1, 6):  # Numbers from 1 to 5
#     print(i)
# ```
# ✅ **Output:**
# ```
# 1
# 2
# 3
# 4
# 5
# ```

# ---

# ### **B) `while` Loop**  
# A `while` loop continues to execute **as long as a condition is True**.

# #### **Example 1: Simple `while` Loop**
# ```python
# count = 1

# while count <= 5:
#     print(count)
#     count += 1
# ```
# ✅ **Output:**
# ```
# 1
# 2
# 3
# 4
# 5
# ```

# ---

# #### **Example 2: User Input with `while` Loop**
# ```python
# password = ""

# while password != "secret":
#     password = input("Enter password: ")

# print("Access granted!")
# ```
# ✅ **Sample Output:**
# ```
# Enter password: pass123
# Enter password: hello
# Enter password: secret
# Access granted!
# ```

# ---

# ## **3️⃣ Loop Control Statements (`break`, `continue`, `pass`)**  

# These statements **modify loop behavior**.

# ### **A) `break` Statement (Exit the Loop)**
# ```python
# for i in range(1, 6):
#     if i == 3:
#         break  # Stops the loop when i = 3
#     print(i)
# ```
# ✅ **Output:**
# ```
# 1
# 2
# ```

# ---

# ### **B) `continue` Statement (Skip Current Iteration)**
# ```python
# for i in range(1, 6):
#     if i == 3:
#         continue  # Skips when i = 3
#     print(i)
# ```
# ✅ **Output:**
# ```
# 1
# 2
# 4
# 5
# ```

# ---

# ### **C) `pass` Statement (Do Nothing, Placeholder)**
# ```python
# for i in range(1, 6):
#     if i == 3:
#         pass  # Placeholder for future code
#     print(i)
# ```
# ✅ **Output:**
# ```
# 1
# 2
# 3
# 4
# 5
# ```

# ---

# ## **Example Program: Putting It All Together**
# ```python
# # User authentication system
# attempts = 3

# while attempts > 0:
#     password = input("Enter password: ")
    
#     if password == "python123":
#         print("Login successful!")
#         break  # Exit the loop
#     else:
#         print("Wrong password! Try again.")
#         attempts -= 1

# if attempts == 0:
#     print("Too many failed attempts. Access denied.")
# ```
# ✅ **Sample Output:**
# ```
# Enter password: pass
# Wrong password! Try again.
# Enter password: hello
# Wrong password! Try again.
# Enter password: python123
# Login successful!
# ```

# ---

# ## **Recap**
# 🔹 **Conditional Statements (`if`, `elif`, `else`)** → For decision-making  
# 🔹 **Loops (`for`, `while`)** → For repeating tasks  
# 🔹 **Loop Control (`break`, `continue`, `pass`)** → To control loop behavior  

# Would you like to move on to the **next topic: Data Structures in Python (Lists, Tuples, Sets, Dictionaries)?** 🚀