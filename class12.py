# ## **12. Object-Oriented Programming (OOP) in Python**  

# **Object-Oriented Programming (OOP)** is a programming paradigm that uses objects and classes to structure code. It helps in creating reusable, modular, and organized code.

# ---

# ## **1️⃣ What is OOP?**  
# OOP is based on the concept of **objects**, which are instances of **classes**. A **class** defines the blueprint for creating objects.

# ### **Key OOP Concepts:**
# 1. **Class** – A blueprint for creating objects.
# 2. **Object** – An instance of a class.
# 3. **Encapsulation** – Hiding data using private attributes and methods.
# 4. **Inheritance** – One class can inherit properties from another.
# 5. **Polymorphism** – The ability to use the same method in different ways.
# 6. **Abstraction** – Hiding complex implementation details.

# ---

# ## **2️⃣ Creating a Class and Object**
# A **class** is created using the `class` keyword.  

# ### **Example: Defining a Class and Creating an Object**
# ```python
# class Car:
#     def __init__(self, brand, model):
#         self.brand = brand  # Attribute
#         self.model = model  # Attribute

#     def display_info(self):  # Method
#         print(f"Car: {self.brand} {self.model}")

# # Creating an object (instance) of the Car class
# car1 = Car("Toyota", "Corolla")
# car1.display_info()
# ```

# ✅ **Output:**
# ```
# Car: Toyota Corolla
# ```

# ---

# ## **3️⃣ The `__init__()` Method (Constructor)**
# The `__init__()` method is called automatically when an object is created.

# 🔹 Example:
# ```python
# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def greet(self):
#         print(f"Hello, my name is {self.name} and I am {self.age} years old.")

# # Creating an object
# s1 = Student("Alice", 20)
# s1.greet()
# ```

# ✅ **Output:**
# ```
# Hello, my name is Alice and I am 20 years old.
# ```

# ---

# ## **4️⃣ Encapsulation (Data Hiding)**
# Encapsulation restricts access to certain attributes to prevent accidental modification.

# 🔹 Example:
# ```python
# class BankAccount:
#     def __init__(self, account_number, balance):
#         self.__account_number = account_number  # Private attribute
#         self.__balance = balance  # Private attribute

#     def deposit(self, amount):
#         self.__balance += amount
#         print(f"Deposited: ${amount}. New Balance: ${self.__balance}")

#     def get_balance(self):  # Getter method
#         return self.__balance

# # Creating an object
# account = BankAccount("12345", 1000)
# account.deposit(500)

# # Accessing private attribute using getter method
# print("Balance:", account.get_balance())
# ```

# ✅ **Output:**
# ```
# Deposited: $500. New Balance: $1500
# Balance: 1500
# ```
# 🚨 **Note:** Private attributes (prefix `__`) cannot be accessed directly outside the class.

# ---

# ## **5️⃣ Inheritance (Reusing Code)**
# Inheritance allows a class to inherit methods and attributes from another class.

# 🔹 Example:
# ```python
# # Parent class
# class Animal:
#     def __init__(self, name):
#         self.name = name

#     def speak(self):
#         return "Some sound"

# # Child class inheriting from Animal
# class Dog(Animal):
#     def speak(self):  # Overriding method
#         return "Bark"

# # Creating objects
# a = Animal("Generic Animal")
# d = Dog("Buddy")

# print(a.name, "says:", a.speak())
# print(d.name, "says:", d.speak())
# ```

# ✅ **Output:**
# ```
# Generic Animal says: Some sound
# Buddy says: Bark
# ```

# ---

# ## **6️⃣ Polymorphism (Same Method, Different Behavior)**
# Polymorphism allows different classes to use the same method in different ways.

# 🔹 Example:
# ```python
# class Bird:
#     def speak(self):
#         return "Chirp"

# class Cat:
#     def speak(self):
#         return "Meow"

# # Function demonstrating polymorphism
# def animal_sound(animal):
#     print(animal.speak())

# # Using different objects with the same method
# bird = Bird()
# cat = Cat()

# animal_sound(bird)  # Output: Chirp
# animal_sound(cat)   # Output: Meow
# ```

# ---

# ## **7️⃣ Abstraction (Hiding Implementation Details)**
# Abstraction allows us to hide complex logic and expose only necessary details.

# 🔹 Example using `abc` (Abstract Base Class):
# ```python
# from abc import ABC, abstractmethod

# class Vehicle(ABC):  # Abstract class
#     @abstractmethod
#     def start(self):
#         pass  # Must be implemented in child class

# class Car(Vehicle):
#     def start(self):
#         print("Car engine started.")

# # Creating an object
# c = Car()
# c.start()
# ```

# ✅ **Output:**
# ```
# Car engine started.
# ```
# 🚨 **Note:** Abstract classes cannot be instantiated directly.

# ---

# ## **8️⃣ Method Overriding**
# A child class can override methods from its parent class.

# 🔹 Example:
# ```python
# class Parent:
#     def show(self):
#         print("This is the Parent class.")

# class Child(Parent):
#     def show(self):  # Overriding method
#         print("This is the Child class.")

# c = Child()
# c.show()
# ```

# ✅ **Output:**
# ```
# This is the Child class.
# ```

# ---

# ## **9️⃣ Multiple Inheritance**
# Python allows a class to inherit from multiple parent classes.

# 🔹 Example:
# ```python
# class A:
#     def method_a(self):
#         print("Method from class A")

# class B:
#     def method_b(self):
#         print("Method from class B")

# class C(A, B):  # Multiple inheritance
#     pass

# c = C()
# c.method_a()
# c.method_b()
# ```

# ✅ **Output:**
# ```
# Method from class A
# Method from class B
# ```

# ---

# ## **🔟 Class vs. Instance Attributes**
# - **Instance Attributes**: Unique to each object.
# - **Class Attributes**: Shared by all instances.

# 🔹 Example:
# ```python
# class Employee:
#     company = "TechCorp"  # Class attribute

#     def __init__(self, name):
#         self.name = name  # Instance attribute

# e1 = Employee("Alice")
# e2 = Employee("Bob")

# print(e1.company)  # TechCorp
# print(e2.company)  # TechCorp
# ```

# ---

# ## **🔹 Recap**
# | Concept        | Description |
# |---------------|------------|
# | **Class & Object** | Blueprint & instance of a class |
# | **Encapsulation** | Hides internal details from outside |
# | **Inheritance** | Reuses code from parent class |
# | **Polymorphism** | Same method, different behavior |
# | **Abstraction** | Hides implementation details |
# | **Method Overriding** | Redefines method in child class |
# | **Multiple Inheritance** | Inherits from multiple classes |

# ---

# 🎯 **Next Steps: Do you want to practice some OOP exercises or move to the next topic: Python File Handling?** 🚀