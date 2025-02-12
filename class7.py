# ## **7. File Handling in Python**  

# File handling allows Python to read, write, and manipulate files. Python provides built-in functions for working with files, such as `open()`, `read()`, and `write()`.  

# ### **Types of File Handling Modes in Python**  
# | Mode | Description |
# |------|-------------|
# | `'r'` | Read mode (default) – Opens file for reading. |
# | `'w'` | Write mode – Creates a new file or overwrites an existing file. |
# | `'a'` | Append mode – Adds content to an existing file. |
# | `'r+'` | Read and write mode. |
# | `'w+'` | Write and read mode – Overwrites existing content. |
# | `'a+'` | Append and read mode. |

# ---

# ## **1️⃣ Opening a File in Python**  
# The `open()` function is used to open a file.  

# ### **Syntax:**  
# ```python
# file = open("filename.txt", "mode")
# ```
# After performing operations, **always close the file** using `file.close()` to free resources.

# ---

# ## **2️⃣ Reading from a File**  
# ### **Example: Reading a File (`'r'` mode)**
# ```python
# file = open("sample.txt", "r")  # Open file in read mode
# content = file.read()  # Read full content
# print(content)
# file.close()  # Always close the file
# ```

# ✅ **Alternative: Using `with open()` (Auto-closing)**
# ```python
# with open("sample.txt", "r") as file:
#     content = file.read()
#     print(content)
# # No need to explicitly close the file
# ```

# ---

# ### **Reading Line by Line**
# ```python
# with open("sample.txt", "r") as file:
#     for line in file:
#         print(line.strip())  # Removes extra spaces and new lines
# ```

# ---

# ## **3️⃣ Writing to a File**  
# Writing mode (`'w'`) **overwrites** existing content.

# ### **Example: Writing to a File (`'w'` mode)**
# ```python
# with open("sample.txt", "w") as file:
#     file.write("Hello, this is a new file!\n")
#     file.write("Python file handling is easy.\n")
# ```
# ✅ **Output (sample.txt):**  
# ```
# Hello, this is a new file!
# Python file handling is easy.
# ```

# ---

# ### **Appending Data (`'a'` mode)**  
# Appending **adds** content without overwriting.

# ```python
# with open("sample.txt", "a") as file:
#     file.write("This line is appended.\n")
# ```

# ✅ **Updated Output (sample.txt):**  
# ```
# Hello, this is a new file!
# Python file handling is easy.
# This line is appended.
# ```

# ---

# ## **4️⃣ Reading and Writing in the Same File (`'r+'` and `'w+'`)**  
# ### **Example: Read and Write (`'r+'` mode)**
# ```python
# with open("sample.txt", "r+") as file:
#     content = file.read()
#     file.write("\nAdding more content!")  # Writing after reading
# ```

# ---

# ## **5️⃣ Working with Binary Files (`'rb'` and `'wb'`)**  
# Binary files are used for **images, videos, or non-text files**.

# ### **Reading a Binary File (`'rb'`)**
# ```python
# with open("image.jpg", "rb") as file:
#     binary_data = file.read()
#     print(binary_data[:10])  # Print first 10 bytes
# ```

# ### **Writing a Binary File (`'wb'`)**
# ```python
# with open("copy.jpg", "wb") as file:
#     file.write(binary_data)
# ```

# ---

# ## **6️⃣ File Handling with `os` and `shutil` Modules**  
# The `os` module helps **manage files and directories**.

# ### **Checking if a File Exists**
# ```python
# import os

# if os.path.exists("sample.txt"):
#     print("File exists!")
# else:
#     print("File not found!")
# ```

# ---

# ### **Deleting a File**
# ```python
# os.remove("sample.txt")
# ```

# ---

# ### **Copying a File**
# ```python
# import shutil
# shutil.copy("sample.txt", "backup.txt")
# ```

# ---

# ### **Renaming a File**
# ```python
# os.rename("sample.txt", "new_sample.txt")
# ```

# ---

# ## **Example Program: Writing, Reading, and Appending Data**
# ```python
# # Writing to a file
# with open("students.txt", "w") as file:
#     file.write("Alice, 23\n")
#     file.write("Bob, 25\n")

# # Reading from the file
# with open("students.txt", "r") as file:
#     print("File Content:\n", file.read())

# # Appending new data
# with open("students.txt", "a") as file:
#     file.write("Charlie, 22\n")

# # Reading after appending
# with open("students.txt", "r") as file:
#     print("Updated File Content:\n", file.read())
# ```

# ✅ **Output:**  
# ```
# File Content:
#  Alice, 23
# Bob, 25

# Updated File Content:
#  Alice, 23
# Bob, 25
# Charlie, 22
# ```

# ---

# ## **Recap**
# 🔹 **Reading (`'r'`)** – Reads content from a file  
# 🔹 **Writing (`'w'`)** – Creates a new file and overwrites content  
# 🔹 **Appending (`'a'`)** – Adds data to the end of a file  
# 🔹 **Reading & Writing (`'r+'`)** – Reads and updates a file  
# 🔹 **Binary Files (`'rb'`, `'wb'`)** – Handles non-text files  
# 🔹 **`os` Module** – Works with file management (delete, rename, check existence)  
# 🔹 **`shutil` Module** – Copies and moves files  

# Would you like to move on to the **next topic: Exception Handling in Python?** 🚀