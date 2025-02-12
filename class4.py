# ## **4. Data Structures in Python**  

# Data structures help store and organize data efficiently. Python provides several built-in data structures:  

# ✅ **Lists** – Ordered, mutable, allows duplicates  
# ✅ **Tuples** – Ordered, immutable, allows duplicates  
# ✅ **Sets** – Unordered, mutable, does NOT allow duplicates  
# ✅ **Dictionaries** – Key-value pairs, unordered  

# ---

# ## **1️⃣ Lists in Python**  
# A **list** is an **ordered collection** of items that can be modified (**mutable**). Lists allow duplicate values.

# ### **Creating a List**
# ```python
fruits = ["apple", "banana", "cherry", "apple"]
print(fruits)
# ```
# ✅ **Output:**  
# ```
# ['apple', 'banana', 'cherry', 'apple']
# ```

# ### **Accessing List Elements**
# ```python
print(fruits[0])  # First item
print(fruits[-1]) # Last item
# ```
# ✅ **Output:**  
# ```
# apple
# apple
# ```

# ### **Modifying a List**
# ```python
fruits[1] = "mango"  # Change banana to mango
print(fruits)
# ```
# ✅ **Output:**  
# ```
# ['apple', 'mango', 'cherry', 'apple']
# ```

# ### **Adding Elements**
# ```python
fruits.append("orange")  # Add at the end
fruits.insert(1, "grape")  # Add at index 1
print(fruits)
# ```

# ### **Removing Elements**
# ```python
fruits.remove("apple")  # Removes first occurrence of "apple"
fruits.pop(2)  # Removes element at index 2
print(fruits)
# ```

# ### **Looping Through a List**
# ```python
for fruit in fruits:
    print(fruit)
# ```

# ---

# ## **2️⃣ Tuples in Python**  
# A **tuple** is similar to a list, but **immutable** (cannot be changed).

# ### **Creating a Tuple**
# ```python
numbers = (10, 20, 30, 40)
print(numbers)
# ```

# ### **Accessing Elements**
# ```python
print(numbers[1])  # Output: 20
# ```

# ### **Tuple Packing & Unpacking**
# ```python
a, b, c = (1, 2, 3)
print(a, b, c)  # Output: 1 2 3
# ```

# ---

# ## **3️⃣ Sets in Python**  
# A **set** is an **unordered collection** that **does not allow duplicate values**.

# ### **Creating a Set**
# ```python
unique_numbers = {1, 2, 3, 3, 4, 5}
print(unique_numbers)
# ```
# ✅ **Output:**  
# ```
{1, 2, 3, 4, 5}  # Duplicates removed
# ```

# ### **Adding & Removing Elements**
# ```python
unique_numbers.add(6)   # Add 6
unique_numbers.remove(3)  # Remove 3
print(unique_numbers)
# ```

# ### **Set Operations**
# ```python
set1 = {1, 2, 3}
set2 = {3, 4, 5}

print(set1.union(set2))  # {1, 2, 3, 4, 5}
print(set1.intersection(set2))  # {3}
print(set1.difference(set2))  # {1, 2}
# ```

# ---

# ## **4️⃣ Dictionaries in Python**  
# A **dictionary** stores key-value pairs.

# ### **Creating a Dictionary**
# ```python
student = {
    "name": "Alice",
    "age": 25,
    "course": "Python"
}
print(student)
# ```

# ### **Accessing Dictionary Values**
# ```python
print(student["name"])  # Output: Alice
print(student.get("age"))  # Output: 25
# ```

# ### **Adding & Updating Key-Value Pairs**
# ```python
student["age"] = 26  # Update
student["city"] = "New York"  # Add new key-value pair
print(student)
# ```

# ### **Removing Elements**
# ```python
student.pop("city")  # Remove "city" key
del student["age"]  # Remove "age"
print(student)
# ```

# ---

# ## **Example Program: Using Lists, Tuples, Sets, and Dictionaries**
# ```python
students = [
    {"name": "Alice", "age": 22, "course": "Python"},
    {"name": "Bob", "age": 24, "course": "Java"}
]

for student in students:
    print(student["name"], "is enrolled in", student["course"])
# ```
# ✅ **Output:**  
# ```
# Alice is enrolled in Python
# Bob is enrolled in Java
# ```

# ---

# ## **Recap**
# 🔹 **Lists** → Ordered, mutable, allows duplicates  
# 🔹 **Tuples** → Ordered, immutable, allows duplicates  
# 🔹 **Sets** → Unordered, mutable, does NOT allow duplicates  
# 🔹 **Dictionaries** → Key-value pairs, unordered  

# Would you like to move on to the **next topic: Functions in Python?** 🚀