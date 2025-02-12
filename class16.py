# ## **16. Python Object-Oriented Programming (OOP)**  

# Object-Oriented Programming (OOP) is a programming paradigm based on the concept of **objects**, which can hold **data** and **methods**. It focuses on modeling real-world entities into Python classes.

# ---

# ## **1️⃣ Key Concepts of OOP**  
# OOP is based on four key principles:
# 1. **Encapsulation**  
# 2. **Abstraction**  
# 3. **Inheritance**  
# 4. **Polymorphism**

# ---

# ## **2️⃣ Class and Object**
# A **class** is a blueprint for creating objects (instances). An **object** is an instance of a class.

# 🔹 **Example: Creating a Class and Object**
# ```python
# # Define the class
# class Dog:
#     def __init__(self, name, breed):
#         self.name = name
#         self.breed = breed
    
#     def bark(self):
#         print(f"{self.name} says Woof!")
    
# # Create an object
# dog1 = Dog("Buddy", "Golden Retriever")
# print(dog1.name)  # Output: Buddy
# dog1.bark()  # Output: Buddy says Woof!
# ```

# ---

# ## **3️⃣ Encapsulation**
# **Encapsulation** is the bundling of data (variables) and methods (functions) that operate on the data into a single unit (class).  
# It also involves restricting access to some of the object’s attributes, typically using **private** or **protected** access modifiers.

# 🔹 **Example: Encapsulation with Private Attributes**
# ```python
# class Car:
#     def __init__(self, make, model):
#         self.make = make
#         self.model = model
#         self.__speed = 0  # Private attribute
    
#     def accelerate(self):
#         self.__speed += 5
#         print(f"Speed: {self.__speed} km/h")
    
#     def get_speed(self):
#         return self.__speed

# car1 = Car("Toyota", "Corolla")
# car1.accelerate()  # Output: Speed: 5 km/h
# print(car1.get_speed())  # Output: 5
# ```
# ⚠ The `__speed` attribute is private and cannot be accessed directly.

# ---

# ## **4️⃣ Abstraction**
# **Abstraction** involves hiding the implementation details and showing only the necessary features of an object.  
# This is done using **abstract classes** and **methods**.

# 🔹 **Example: Abstraction with Abstract Base Class**
# ```python
# from abc import ABC, abstractmethod

# class Animal(ABC):
#     @abstractmethod
#     def make_sound(self):
#         pass

# class Dog(Animal):
#     def make_sound(self):
#         print("Woof!")

# dog1 = Dog()
# dog1.make_sound()  # Output: Woof!
# ```
# In this example, `make_sound()` is an abstract method that must be implemented by any subclass of `Animal`.

# ---

# ## **5️⃣ Inheritance**
# **Inheritance** allows one class (child class) to inherit the attributes and methods of another class (parent class), facilitating code reuse.

# 🔹 **Example: Inheritance**
# ```python
# class Animal:
#     def __init__(self, name):
#         self.name = name
    
#     def speak(self):
#         print(f"{self.name} makes a sound!")

# class Dog(Animal):
#     def speak(self):
#         print(f"{self.name} barks!")

# dog1 = Dog("Buddy")
# dog1.speak()  # Output: Buddy barks!
# ```
# In this example, the `Dog` class inherits from the `Animal` class but overrides the `speak()` method.

# ---

# ## **6️⃣ Polymorphism**
# **Polymorphism** allows methods to have the same name but behave differently based on the object type. It can be achieved via **method overriding** or **method overloading**.

# 🔹 **Example: Polymorphism via Method Overriding**
# ```python
# class Animal:
#     def speak(self):
#         print("Animal speaks!")

# class Dog(Animal):
#     def speak(self):
#         print("Dog barks!")

# class Cat(Animal):
#     def speak(self):
#         print("Cat meows!")

# animals = [Dog(), Cat()]

# for animal in animals:
#     animal.speak()
# ```
# ✅ **Output:**
# ```
# Dog barks!
# Cat meows!
# ```

# Here, both `Dog` and `Cat` classes override the `speak()` method, demonstrating polymorphism.

# ---

# ## **7️⃣ Constructor and Destructor**
# The **constructor** (`__init__`) is used to initialize objects. The **destructor** (`__del__`) is used to clean up when an object is deleted.

# 🔹 **Example: Constructor and Destructor**
# ```python
# class Person:
#     def __init__(self, name):
#         self.name = name
#         print(f"Person {self.name} created.")
    
#     def __del__(self):
#         print(f"Person {self.name} deleted.")

# p1 = Person("Alice")
# del p1  # Deletes the object and calls the destructor
# ```
# ✅ **Output:**
# ```
# Person Alice created.
# Person Alice deleted.
# ```

# ---

# ## **8️⃣ Recap: OOP Concepts**

# | Concept         | Description |
# |-----------------|-------------|
# | **Class**       | Blueprint for creating objects |
# | **Object**      | Instance of a class |
# | **Encapsulation** | Bundling data and methods, and restricting access to private attributes |
# | **Abstraction** | Hiding implementation details, showing only essential features |
# | **Inheritance** | Reusing code from parent classes by creating child classes |
# | **Polymorphism** | Same method name, but different behavior based on the object type |
# | **Constructor**  | Initializes objects |
# | **Destructor**   | Cleans up resources when objects are deleted |

# ---

# 🚀 **Next Steps: Do you want to move to the next topic: Python Advanced Topics or do you need any further clarification on OOP?**