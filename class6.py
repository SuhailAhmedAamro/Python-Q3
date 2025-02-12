# ## **6. Object-Oriented Programming (OOP) in Python**  

# Object-Oriented Programming (**OOP**) is a programming paradigm based on the concept of **objects** and **classes**. It helps organize code by grouping related properties and behaviors into reusable objects.  

# ### **Key Concepts of OOP in Python:**  
# ✅ **Class** – A blueprint for creating objects  
# ✅ **Object** – An instance of a class  
# ✅ **Attributes (Properties)** – Variables that store data about an object  
# ✅ **Methods (Functions in a Class)** – Functions that define the behavior of an object  
# ✅ **Constructor (`__init__` Method)** – Initializes object attributes when created  
# ✅ **Inheritance** – Allows a class to inherit properties and methods from another class  
# ✅ **Encapsulation** – Hides implementation details and protects data  
# ✅ **Polymorphism** – Allows different classes to use the same method name but behave differently  

# ---

# ## **1️⃣ Creating a Class and Object**  
# A **class** is a blueprint for objects, and an **object** is an instance of a class.

# ### **Example: Creating a Class and an Object**
# ```python
class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def display_info(self):
        print(f"Car: {self.brand} {self.model} ({self.year})")

# Creating an object
car1 = Car("Toyota", "Corolla", 2023)
car1.display_info()
# ```
# ✅ **Output:**  
# ```
# Car: Toyota Corolla (2023)
# ```

# ---

# ## **2️⃣ The `__init__` Constructor Method**  
# The `__init__` method runs automatically when an object is created.

# ```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

p1 = Person("Alice", 30)
p1.greet()
# ```
# ✅ **Output:**  
# ```
# Hello, my name is Alice and I am 30 years old.
# ```

# ---

# ## **3️⃣ Class vs Instance Variables**  
# 🔹 **Instance variables** are specific to an object.  
# 🔹 **Class variables** are shared among all objects of a class.

# ### **Example: Class and Instance Variables**
# ```python
class Dog:
    species = "Canine"  # Class variable (shared)

    def __init__(self, name, breed):
        self.name = name  # Instance variable (unique to each object)
        self.breed = breed

dog1 = Dog("Buddy", "Golden Retriever")
dog2 = Dog("Max", "Bulldog")

print(dog1.name, "is a", dog1.species)
print(dog2.name, "is a", dog2.species)
# ```
# ✅ **Output:**  
# ```
# Buddy is a Canine
# Max is a Canine
# ```

# ---

# ## **4️⃣ Inheritance in Python**  
# Inheritance allows a class (**child class**) to inherit attributes and methods from another class (**parent class**).

# ### **Example: Single Inheritance**
# ```python
class Animal:
    def speak(self):
        print("Animal makes a sound")

class Dog(Animal):  # Inherits from Animal
    def bark(self):
        print("Woof! Woof!")

dog = Dog()
dog.speak()  # Inherited method
dog.bark()   # Dog's own method
# ```
# ✅ **Output:**  
# ```
# Animal makes a sound
# Woof! Woof!
# ```

# ---

# ## **5️⃣ Method Overriding in Inheritance**  
# A child class can **override** a method from the parent class.

# ### **Example: Overriding a Method**
# ```python
class Animal:
    def speak(self):
        print("Animal makes a sound")

class Cat(Animal):
    def speak(self):
        print("Meow!")

cat = Cat()
cat.speak()  # Overridden method
# ```
# ✅ **Output:**  
# ```
# Meow!
# ```

# ---

# ## **6️⃣ Encapsulation (Private & Public Attributes)**  
# Encapsulation restricts access to certain data within a class.

# ### **Example: Private and Public Attributes**
# ```python
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # Private variable

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance

account = BankAccount(1000)
account.deposit(500)
print(account.get_balance())  # Access balance using a method
# ```
# ✅ **Output:**  
# ```
# 1500
# ```
# ❌ **Accessing private attributes directly (`account.__balance`) will cause an error.**

# ---

# ## **7️⃣ Polymorphism in Python**  
# Polymorphism allows different classes to use the **same method name** but have different implementations.

# ### **Example: Polymorphism with Methods**
# ```python
class Bird:
    def speak(self):
        print("Bird chirps")

class Dog:
    def speak(self):
        print("Dog barks")

animals = [Bird(), Dog()]

for animal in animals:
    animal.speak()  # Same method name, different behavior
# ```
# ✅ **Output:**  
# ```
# Bird chirps
# Dog barks
# ```

# ---

# ## **Example Program: Full OOP Implementation**
# ```python
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def show_details(self):
        print(f"Employee: {self.name}, Salary: ${self.salary}")

class Manager(Employee):  # Inheriting from Employee
    def __init__(self, name, salary, department):
        super().__init__(name, salary)  # Calling parent class constructor
        self.department = department

    def show_details(self):
        print(f"Manager: {self.name}, Department: {self.department}, Salary: ${self.salary}")

e1 = Employee("John", 50000)
m1 = Manager("Alice", 80000, "HR")

e1.show_details()
m1.show_details()
# ```
# ✅ **Output:**  
# ```
# Employee: John, Salary: $50000
# Manager: Alice, Department: HR, Salary: $80000
# ```

# ---

# ## **Recap**
# 🔹 **Class & Object** – Blueprint and instance of a class  
# 🔹 **Constructor (`__init__`)** – Initializes object attributes  
# 🔹 **Instance vs Class Variables** – Unique per object vs shared among all objects  
# 🔹 **Inheritance** – Child class inherits from parent class  
# 🔹 **Method Overriding** – Child class redefines a parent method  
# 🔹 **Encapsulation** – Restrict access to private attributes  
# 🔹 **Polymorphism** – Same method, different behavior  

# Would you like to move on to the **next topic: File Handling in Python?** 🚀