# ## **11. Working with APIs in Python**  

# An **API (Application Programming Interface)** allows applications to communicate with each other. APIs enable us to send and receive data over the internet, making them essential for web development, mobile apps, and automation.

# Python provides several libraries to work with APIs, the most popular being the `requests` library.

# ---

# ## **1️⃣ What is an API?**
# An **API** is a set of rules that allow one program to interact with another. APIs use **HTTP requests** to perform operations such as:
# - **GET** – Retrieve data  
# - **POST** – Send data  
# - **PUT/PATCH** – Update data  
# - **DELETE** – Remove data  

# ### **Example: API in Real Life**
# - Weather apps fetch data from a weather API.
# - E-commerce websites fetch product details from a database using an API.
# - Payment gateways interact with bank APIs to process payments.

# ---

# ## **2️⃣ Installing the `requests` Library**
# The `requests` library is used to send HTTP requests.

# 🔹 Install it using `pip`:
# ```bash
# pip install requests
# ```

# ---

# ## **3️⃣ Sending a GET Request**  
# A **GET request** is used to fetch data from an API.

# 🔹 Example: Fetching data from a public API (JSONPlaceholder)
# ```python
# import requests

# url = "https://jsonplaceholder.typicode.com/posts/1"
# response = requests.get(url)  # Send GET request

# # Print status code and response data
# print("Status Code:", response.status_code)
# print("Response Data:", response.json())
# ```

# ✅ **Output:**
# ```
# Status Code: 200
# {
#   "userId": 1,
#   "id": 1,
#   "title": "Sample Post",
#   "body": "This is a sample post content."
# }
# ```

# ---

# ## **4️⃣ Sending a POST Request**  
# A **POST request** is used to send data to an API.

# 🔹 Example: Sending data to an API
# ```python
# import requests

# url = "https://jsonplaceholder.typicode.com/posts"
# data = {
#     "title": "New Post",
#     "body": "This is the content of the new post.",
#     "userId": 1
# }

# response = requests.post(url, json=data)

# print("Status Code:", response.status_code)
# print("Response Data:", response.json())
# ```

# ✅ **Output:**
# ```
# Status Code: 201
# {
#   "id": 101,
#   "title": "New Post",
#   "body": "This is the content of the new post.",
#   "userId": 1
# }
# ```
# 🚀 The new post is created with `id: 101`.

# ---

# ## **5️⃣ Sending a PUT Request (Updating Data)**
# A **PUT request** is used to update existing data.

# 🔹 Example: Updating a post
# ```python
# import requests

# url = "https://jsonplaceholder.typicode.com/posts/1"
# data = {
#     "title": "Updated Title",
#     "body": "Updated content of the post.",
#     "userId": 1
# }

# response = requests.put(url, json=data)

# print("Status Code:", response.status_code)
# print("Response Data:", response.json())
# ```

# ✅ **Output:**
# ```
# Status Code: 200
# {
#   "id": 1,
#   "title": "Updated Title",
#   "body": "Updated content of the post.",
#   "userId": 1
# }
# ```

# ---

# ## **6️⃣ Sending a DELETE Request (Removing Data)**
# A **DELETE request** is used to delete data.

# 🔹 Example: Deleting a post
# ```python
# import requests

# url = "https://jsonplaceholder.typicode.com/posts/1"
# response = requests.delete(url)

# print("Status Code:", response.status_code)
# ```

# ✅ **Output:**
# ```
# Status Code: 200
# ```
# 🚀 The post is successfully deleted.

# ---

# ## **7️⃣ Handling API Errors**
# APIs might return errors due to bad requests, authentication failures, or server issues.

# 🔹 Example: Handling Errors
# ```python
# import requests

# url = "https://jsonplaceholder.typicode.com/invalid-endpoint"

# response = requests.get(url)

# if response.status_code == 200:
#     print("Data:", response.json())
# else:
#     print(f"Error: {response.status_code} - {response.reason}")
# ```

# ✅ **Output:**
# ```
# Error: 404 - Not Found
# ```

# ---

# ## **8️⃣ Using API Authentication**
# Some APIs require **authentication** using an **API key** or **Bearer Token**.

# 🔹 Example: Sending a request with an API Key
# ```python
# import requests

# url = "https://api.example.com/data"
# headers = {
#     "Authorization": "Bearer YOUR_API_KEY"
# }

# response = requests.get(url, headers=headers)

# print(response.json())
# ```

# 📌 **Replace `YOUR_API_KEY` with a valid API key.**

# ---

# ## **9️⃣ Working with JSON Data**
# Most APIs return data in **JSON format**. You can **parse JSON** using `response.json()`.

# 🔹 Example: Parsing JSON data
# ```python
# import requests

# url = "https://jsonplaceholder.typicode.com/users"
# response = requests.get(url)

# users = response.json()

# # Print names of all users
# for user in users:
#     print(user["name"])
# ```

# ✅ **Output:**
# ```
# Leanne Graham
# Ervin Howell
# Clementine Bauch
# ...
# ```

# ---

# ## **🔟 Using APIs with Query Parameters**
# Some APIs accept **query parameters** to filter data.

# 🔹 Example: Fetching posts from user `id=1`
# ```python
# import requests

# url = "https://jsonplaceholder.typicode.com/posts"
# params = {"userId": 1}  # Query parameters

# response = requests.get(url, params=params)

# print(response.json())
# ```

# ✅ **Output:**
# ```
# [
#   {"userId": 1, "id": 1, "title": "Post 1", "body": "..."},
#   {"userId": 1, "id": 2, "title": "Post 2", "body": "..."}
# ]
# ```

# ---

# ## **1️⃣1️⃣ Rate Limiting & API Best Practices**
# APIs may **rate limit** users, restricting the number of requests per second.

# ### ✅ **Best Practices for API Requests**
# 1️⃣ Use **exponential backoff** (retry failed requests after a delay).  
# 2️⃣ Avoid **making too many requests** in a short time.  
# 3️⃣ Use **pagination** when fetching large datasets.  
# 4️⃣ **Cache API responses** to reduce redundant requests.  
# 5️⃣ Handle **timeouts and exceptions** properly.

# 🔹 Example: Handling Timeouts
# ```python
# import requests

# try:
#     response = requests.get("https://jsonplaceholder.typicode.com/posts", timeout=5)
#     print(response.json())
# except requests.exceptions.Timeout:
#     print("Request timed out! Try again later.")
# ```

# ---

# ## **✅ Recap**
# 🔹 **API** – Allows applications to communicate via HTTP requests.  
# 🔹 **HTTP Methods** – `GET`, `POST`, `PUT`, `DELETE` for interacting with APIs.  
# 🔹 **`requests` Library** – Used to send HTTP requests in Python.  
# 🔹 **Handling Errors** – Check response status codes and handle errors properly.  
# 🔹 **Authentication** – Use API keys or tokens when required.  
# 🔹 **Working with JSON** – Parse API responses using `response.json()`.  
# 🔹 **Best Practices** – Handle rate limits, use caching, and manage timeouts.

# ---

# 🚀 **Would you like to move on to the next topic: Object-Oriented Programming (OOP) in Python?**