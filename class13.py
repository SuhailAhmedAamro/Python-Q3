# ## **13. Python File Handling**  

# Python allows us to work with files to read, write, and manipulate data efficiently. File handling is useful for storing data, logging, configuration files, and more.

# ---

# ## **1️⃣ Opening a File in Python**
# Python provides the built-in `open()` function to work with files.

# ### **Syntax:**
# ```python
# file = open("filename", "mode")
# ```
# | Mode | Description |
# |------|------------|
# | `"r"` | Read mode (default) |
# | `"w"` | Write mode (overwrites file) |
# | `"a"` | Append mode (adds to existing content) |
# | `"x"` | Creates a new file (fails if it exists) |
# | `"b"` | Binary mode (e.g., images) |
# | `"t"` | Text mode (default) |

# 🔹 **Example: Opening a file for reading**  
# ```python
# file = open("example.txt", "r")
# content = file.read()
# print(content)
# file.close()
# ```

# ---

# ## **2️⃣ Reading a File**
# Python provides multiple ways to read a file:

# ### **1. Read Entire File (`read()`)**
# ```python
# file = open("example.txt", "r")
# content = file.read()
# print(content)
# file.close()
# ```

# ### **2. Read First N Characters (`read(n)`)**
# ```python
# file = open("example.txt", "r")
# content = file.read(10)  # Reads first 10 characters
# print(content)
# file.close()
# ```

# ### **3. Read Line by Line (`readline()`)**
# ```python
# file = open("example.txt", "r")
# line = file.readline()  # Reads first line
# print(line)
# file.close()
# ```

# ### **4. Read All Lines (`readlines()`)**
# ```python
# file = open("example.txt", "r")
# lines = file.readlines()  # Returns a list of lines
# print(lines)
# file.close()
# ```

# ---

# ## **3️⃣ Writing to a File**
# The `"w"` mode is used to write to a file. **⚠ Warning:** This **overwrites** existing content.

# 🔹 **Example: Writing to a File**
# ```python
# file = open("example.txt", "w")
# file.write("Hello, World!\nThis is a test file.")
# file.close()
# ```

# ---

# ## **4️⃣ Appending Data to a File**
# The `"a"` mode is used to **append** new content **without overwriting**.

# 🔹 **Example: Appending to a File**
# ```python
# file = open("example.txt", "a")
# file.write("\nAdding more content.")
# file.close()
# ```

# ---

# ## **5️⃣ Using `with open()` (Best Practice)**
# Using `with open()`, we don’t need to manually close the file. It automatically handles closing the file.

# 🔹 **Example: Reading a File Safely**
# ```python
# with open("example.txt", "r") as file:
#     content = file.read()
#     print(content)  # File automatically closes after this block
# ```

# 🔹 **Example: Writing to a File Safely**
# ```python
# with open("example.txt", "w") as file:
#     file.write("This is a safer way to write files.")
# ```

# ---

# ## **6️⃣ Checking if a File Exists**
# The `os` module allows us to check if a file exists before performing operations.

# 🔹 **Example: Checking File Existence**
# ```python
# import os

# if os.path.exists("example.txt"):
#     print("File exists!")
# else:
#     print("File not found.")
# ```

# ---

# ## **7️⃣ Deleting a File**
# We can use the `os` module to delete files.

# 🔹 **Example: Deleting a File**
# ```python
# import os

# if os.path.exists("example.txt"):
#     os.remove("example.txt")
#     print("File deleted.")
# else:
#     print("File does not exist.")
# ```

# ---

# ## **8️⃣ Working with Binary Files**
# Binary files include images, videos, and PDFs. We use `"rb"` and `"wb"` modes.

# 🔹 **Example: Copying an Image**
# ```python
# with open("image.jpg", "rb") as source:
#     with open("copy.jpg", "wb") as destination:
#         destination.write(source.read())
# ```

# ---

# ## **🔟 Recap**
# | Operation  | Mode | Function |
# |------------|------|------------|
# | Read a file | `"r"` | `read()`, `readline()`, `readlines()` |
# | Write a file | `"w"` | `write()` (overwrites file) |
# | Append to a file | `"a"` | `write()` (adds to file) |
# | Binary files | `"rb"`, `"wb"` | `read()` and `write()` in binary mode |
# | Check file existence | - | `os.path.exists()` |
# | Delete a file | - | `os.remove()` |

# ---

# 🚀 **Next Steps: Do you want to move to the next topic: Python Exception Handling?**