# ## **10. Working with Databases in Python**  

# Databases allow you to store and manage large volumes of data in an organized way. Python provides several libraries to interact with databases, such as **SQLite**, **MySQL**, **PostgreSQL**, and more.

# In this section, we'll focus on **SQLite**, a lightweight database built into Python, which doesn't require any server installation.

# ---

# ### **1️⃣ What is SQLite?**  
# **SQLite** is a serverless, self-contained, and zero-configuration database engine. It is used for local storage in many applications. It stores the entire database in a single file, which is easy to manage.

# ---

# ### **2️⃣ Connecting to SQLite Database**  
# Python's `sqlite3` module allows you to interact with SQLite databases.

# #### **Example: Connecting to SQLite Database**
# ```python
# import sqlite3

# # Connect to SQLite database (it creates the file if it doesn't exist)
# connection = sqlite3.connect("mydatabase.db")

# # Create a cursor object to execute SQL queries
# cursor = connection.cursor()

# # Close the connection after use
# connection.close()
# ```

# ---

# ### **3️⃣ Creating a Database Table**  
# You can create tables to store your data.

# #### **Example: Creating a Table**
# ```python
# import sqlite3

# # Connect to SQLite database
# connection = sqlite3.connect("mydatabase.db")
# cursor = connection.cursor()

# # Create a new table named 'students'
# cursor.execute('''
#     CREATE TABLE IF NOT EXISTS students (
#         id INTEGER PRIMARY KEY,
#         name TEXT,
#         age INTEGER
#     )
# ''')

# # Commit changes and close the connection
# connection.commit()
# connection.close()
# ```

# ---

# ### **4️⃣ Inserting Data into a Table**  
# You can insert records into a table using SQL `INSERT INTO`.

# #### **Example: Inserting Data**
# ```python
# import sqlite3

# # Connect to SQLite database
# connection = sqlite3.connect("mydatabase.db")
# cursor = connection.cursor()

# # Insert data into the 'students' table
# cursor.execute("INSERT INTO students (name, age) VALUES (?, ?)", ("Alice", 20))
# cursor.execute("INSERT INTO students (name, age) VALUES (?, ?)", ("Bob", 22))

# # Commit changes and close the connection
# connection.commit()
# connection.close()
# ```

# ---

# ### **5️⃣ Querying Data from a Table**  
# You can retrieve data using the `SELECT` statement.

# #### **Example: Querying Data**
# ```python
# import sqlite3

# # Connect to SQLite database
# connection = sqlite3.connect("mydatabase.db")
# cursor = connection.cursor()

# # Query all students from the 'students' table
# cursor.execute("SELECT * FROM students")

# # Fetch all results
# students = cursor.fetchall()

# for student in students:
#     print(student)

# # Close the connection
# connection.close()
# ```
# ✅ **Output:**  
# ```
# (1, 'Alice', 20)
# (2, 'Bob', 22)
# ```

# ---

# ### **6️⃣ Updating Data in a Table**  
# You can update existing records using the `UPDATE` statement.

# #### **Example: Updating Data**
# ```python
# import sqlite3

# # Connect to SQLite database
# connection = sqlite3.connect("mydatabase.db")
# cursor = connection.cursor()

# # Update Alice's age
# cursor.execute("UPDATE students SET age = ? WHERE name = ?", (21, "Alice"))

# # Commit changes and close the connection
# connection.commit()
# connection.close()
# ```

# ---

# ### **7️⃣ Deleting Data from a Table**  
# You can delete records using the `DELETE` statement.

# #### **Example: Deleting Data**
# ```python
# import sqlite3

# # Connect to SQLite database
# connection = sqlite3.connect("mydatabase.db")
# cursor = connection.cursor()

# # Delete Bob from the 'students' table
# cursor.execute("DELETE FROM students WHERE name = ?", ("Bob",))

# # Commit changes and close the connection
# connection.commit()
# connection.close()
# ```

# ---

# ### **8️⃣ Handling Errors with Try-Except in Database Operations**  
# Database operations might fail due to issues like syntax errors, constraint violations, or connection problems. It's essential to handle such errors.

# #### **Example: Error Handling**
# ```python
# import sqlite3

# try:
#     connection = sqlite3.connect("mydatabase.db")
#     cursor = connection.cursor()

#     # Intentional error: Missing column in the query
#     cursor.execute("INSERT INTO students (name) VALUES (?)", ("Charlie",))

#     connection.commit()
# except sqlite3.Error as e:
#     print(f"Database error: {e}")
# finally:
#     connection.close()
# ```

# ---

# ### **9️⃣ Using Context Managers with SQLite**  
# You can use context managers (`with` statement) to automatically manage database connections and ensure they are properly closed.

# #### **Example: Using Context Manager**
# ```python
# import sqlite3

# # Using context manager to connect and execute queries
# with sqlite3.connect("mydatabase.db") as connection:
#     cursor = connection.cursor()

#     # Create table
#     cursor.execute('''
#         CREATE TABLE IF NOT EXISTS students (
#             id INTEGER PRIMARY KEY,
#             name TEXT,
#             age INTEGER
#         )
#     ''')

#     # Insert data
#     cursor.execute("INSERT INTO students (name, age) VALUES (?, ?)", ("Alice", 20))
#     cursor.execute("INSERT INTO students (name, age) VALUES (?, ?)", ("Bob", 22))

#     # Commit is automatically handled by the context manager
# ```

# ---

# ### **10️⃣ Closing the Connection Properly**  
# When you finish interacting with the database, it is crucial to close the connection using `connection.close()`. Failing to do so might cause memory leaks or issues with database locking.

# ---

# ## **Recap**
# 🔹 **SQLite** – A lightweight, self-contained database system built into Python.  
# 🔹 **Connecting to SQLite** – Use `sqlite3.connect()` to connect to a database file.  
# 🔹 **CRUD Operations** – Perform **Create**, **Read**, **Update**, and **Delete** operations using SQL statements.  
# 🔹 **Error Handling** – Use `try-except` blocks to manage database-related errors.  
# 🔹 **Context Manager** – Automatically manage database connections and close them using the `with` statement.

# Would you like to move on to the **next topic: Working with APIs in Python?** 🚀