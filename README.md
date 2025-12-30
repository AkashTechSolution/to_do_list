# To-Do List Web Application (Django)

# Project Overview

This project is a **To-Do List web application** built using **Python and Django**.  
It provides:

- RESTful APIs for specified **CRUD operations** on tasks (This project doesn't include update and delete operations)
- HTML templates for a simple **web interface**
- **SQLite** database for data storage
- **Raw SQL queries** (No use of Django ORM as per project constraint)
- **Function-based views only** (No Generic ViewSets)

# Tech Stack

Backend - **Python, Django**  
Database - **SQLite** (default Django database)  
Testing framework - **pytest** (for automate API testing process)  
Frontend - **HTML** (Django Templates)

# Command to create virtual environment (for Windows system)
python -m venv venv
venv\Scripts\activate

# Command to run the Application 
python manage.py runserver

- Then we will open "http://127.0.0.1:8000/" in a web browser

# HTML Templates -
- http://127.0.0.1:8000/      - It will show the web page with the feature to add task 
- http://127.0.0.1:8000/add/     - It will show the page for entering the details of the task
- http://127.0.0.1:8000/api/tasks/      - It will display the list of all tasks created

# API Documentation - 

**Create Task** 

- Endpoint: /api/tasks/create/
- Method: POST
- Request (JSON): 

{
    "title": "Vegetable",
    "description": "Buy some vegetables",
    "due_date": "2025-12-28",
    "status": "Pending"
}

- Success Response - 

{
  "message": "Task created"
}

**Retrieve all tasks**

- Endpoint: /api/tasks/
- Method: GET
- Response:
[
  {
    "id": 1,
    "title": "Vegetable",
    "description": "Buy some vegetables",
    "due_date": "2025-12-28",
    "status": "Pending"
  },
  {
    "id": 2,
    "title": "Dairy Products",
    "description": "Milk, Cheese, Curd",
    "due_date": "2025-12-30",
    "status": "Pending"
  }
]

# Testing framework -
This project uses pytest for automated testing of API endpoints.
- Command to run tests: 

pytest

Output:
========= test session starts =========
platform win32 -- Python 3.13.7, pytest-9.0.2, pluggy-1.6.0
django: version: 6.0, settings: to_do_list.settings (from ini)
rootdir: E:\Django_Project\to_do_list
configfile: pytest.ini
plugins: django-4.11.1
collected 3 items                      

tasks\test_tasks.py ...          [100%]

========== 3 passed in 0.29s ========== 

# Covered test scenarios - 
- Create task
- Retrieve task list
- Input validation
- Error handling

# Logging and Exception handling - 
- Logging is implemented using Python’s logging module
- INFO logs are recorded for successful operations
- ERROR logs are recorded for database or runtime failures

