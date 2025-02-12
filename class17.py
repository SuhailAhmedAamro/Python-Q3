# ## **17. Python Advanced Topics**

# Advanced Python topics involve concepts that go beyond the basics, covering more complex areas like decorators, generators, context managers, metaclasses, and more.

# ---

# ## **1️⃣ Decorators**
# A **decorator** is a function that allows you to modify the behavior of another function or method. It's a way to add functionality to an existing code without modifying the code itself.

# 🔹 **Example: Simple Decorator**
# ```python
# def my_decorator(func):
#     def wrapper():
#         print("Before function call")
#         func()
#         print("After function call")
#     return wrapper

# @my_decorator
# def say_hello():
#     print("Hello!")

# say_hello()
# ```
# ✅ **Output:**
# ```
# Before function call
# Hello!
# After function call
# ```

# ---

# ## **2️⃣ Generators**
# A **generator** is a special type of iterator that is defined using a function and the `yield` keyword. It allows you to iterate over data without storing it all in memory at once.

# 🔹 **Example: Simple Generator**
# ```python
# def count_up_to(max):
#     count = 1
#     while count <= max:
#         yield count
#         count += 1

# for num in count_up_to(5):
#     print(num)
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

# ## **3️⃣ Context Managers and `with` Statement**
# A **context manager** is used to manage resources, such as files or network connections, ensuring that resources are properly acquired and released. The `with` statement is used to simplify the use of context managers.

# 🔹 **Example: Using `with` for File Handling**
# ```python
# with open('example.txt', 'w') as file:
#     file.write("Hello, World!")
# ```
# This automatically handles opening and closing the file, ensuring that it is closed even if an error occurs.

# ---

# ## **4️⃣ Metaclasses**
# A **metaclass** is a class for classes. It allows you to define how new classes are created. Metaclasses are advanced and can be used to modify the behavior of class creation and structure.

# 🔹 **Example: Simple Metaclass**
# ```python
# class Meta(type):
#     def __new__(cls, name, bases, dct):
#         dct['greet'] = lambda self: "Hello from the metaclass!"
#         return super().__new__(cls, name, bases, dct)

# class MyClass(metaclass=Meta):
#     pass

# obj = MyClass()
# print(obj.greet())  # Output: Hello from the metaclass!
# ```

# ---

# ## **5️⃣ Abstract Base Classes (ABC)**
# Abstract Base Classes (ABC) are classes that cannot be instantiated on their own and are meant to be subclasses by other classes. They define abstract methods that must be implemented by child classes.

# 🔹 **Example: ABC in Python**
# ```python
# from abc import ABC, abstractmethod

# class Shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass

# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius
    
#     def area(self):
#         return 3.14 * self.radius * self.radius

# circle = Circle(5)
# print(circle.area())  # Output: 78.5
# ```

# ---

# ## **6️⃣ Coroutines and `asyncio`**
# Coroutines are special types of functions used for asynchronous programming. They allow you to perform tasks without blocking the main execution flow, and are useful for I/O-bound operations.

# 🔹 **Example: Basic Coroutine with `asyncio`**
# ```python
# import asyncio

# async def say_hello():
#     print("Hello, World!")
#     await asyncio.sleep(1)
#     print("Goodbye!")

# asyncio.run(say_hello())
# ```
# In this example, the coroutine `say_hello` is executed asynchronously.

# ---

# ## **7️⃣ Lambda Functions**
# A **lambda function** is a small anonymous function that can have any number of arguments, but only one expression. It is often used for short, throwaway functions.

# 🔹 **Example: Lambda Function**
# ```python
# add = lambda x, y: x + y
# print(add(2, 3))  # Output: 5
# ```

# ---

# ## **8️⃣ List Comprehensions and Generator Expressions**
# **List comprehensions** allow you to create new lists by applying an expression to each element in an existing list or iterable. **Generator expressions** are similar but generate items lazily, saving memory.

# 🔹 **Example: List Comprehension**
# ```python
# numbers = [1, 2, 3, 4]
# squares = [x**2 for x in numbers]
# print(squares)  # Output: [1, 4, 9, 16]
# ```

# 🔹 **Example: Generator Expression**
# ```python
# numbers = [1, 2, 3, 4]
# squares_gen = (x**2 for x in numbers)
# for square in squares_gen:
#     print(square)
# ```

# ---

# ## **9️⃣ Multiple Inheritance**
# **Multiple inheritance** allows a class to inherit from more than one parent class. This can be useful for combining behaviors from multiple sources.

# 🔹 **Example: Multiple Inheritance**
# ```python
# class Animal:
#     def speak(self):
#         print("Animal speaks!")

# class Bird:
#     def fly(self):
#         print("Bird flies!")

# class Eagle(Animal, Bird):
#     pass

# eagle = Eagle()
# eagle.speak()  # Output: Animal speaks!
# eagle.fly()    # Output: Bird flies!
# ```

# ---

# ## **🔟 Recap: Advanced Python Topics**

# | Concept             | Description |
# |---------------------|-------------|
# | **Decorators**       | Functions that modify the behavior of other functions |
# | **Generators**       | Functions that yield values one at a time, saving memory |
# | **Context Managers** | Managing resources (e.g., files) with the `with` statement |
# | **Metaclasses**      | Classes that define the behavior of other classes |
# | **Abstract Base Classes (ABC)** | Classes that define abstract methods for subclasses |
# | **Coroutines**       | Asynchronous functions for non-blocking operations |
# | **Lambda Functions** | Anonymous, short functions with a single expression |
# | **List Comprehensions** | Concise way to create lists |
# | **Multiple Inheritance** | Inheriting from multiple parent classes |

# ---

# 🚀 **Next Steps: Do you want to dive deeper into any specific advanced topics, or are you ready to explore other Python concepts?**