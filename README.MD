# CLI Task Tracker (Roadmap.sh Project)

A simple **command-line task tracker** developed in **Python**, where the user can create, list, update, and delete tasks using a menu-driven interface.  
All tasks are stored in a **JSON file**, allowing data persistence between executions.

---

## About the Project

This project was created as part of the [**roadmap.sh learning platform**](https://roadmap.sh/projects/task-tracker), focused on practicing:

- Python fundamentals  
- File handling with JSON  
- CLI menu navigation  
- Functions and modularization  
- Data structures (lists and dictionaries)  
- Basic CRUD operations  

The goal of the application is to manage tasks efficiently from the terminal.

---

## How the Application Works

- The program creates a `banco.json` file automatically if it does not exist  
- The user interacts with the system through menus  
- Each task has an ID, description, status, creation date, and update date  
- Tasks can be filtered by status  

## Features

- Create new tasks  
- List all tasks  
- List tasks by status  
  - Todo  
  - In progress  
  - Done  
- Update task description  
- Update task status  
- Delete tasks  
- Automatic task ID reordering  
- Persistent storage using JSON  
- Simple and clear CLI interface  

---

## Project Structure

├── main.py # Application entry point <br>
├── menu.py # Main menu and option execution<br>
├── task.py # Create, update and delete tasks<br>
├── listtask.py # Task listing functions<br>
├── storage.py # JSON read/write operations<br>
├── utils.py # Utility functions<br>
└── banco.json # JSON file used as storage


---

## JSON Data Structure

```json
{
  "Tasks": [
    {
      "id": 1,
      "description": "Example task",
      "status": "todo",
      "createdAt": "2026-01-18",
      "updateAt": ""
    }
  ]
}
```

# How to Run the Application

1. Requirements

Python 3.8 or higher

2. Clone the repository

```
git clone https://github.com/Ramos-Victor/Task-Tracker-CLI
cd Task-Tracker-CLI
```

3. Run the program
```
python3 main.py
```

# Learning Objectives

This project helps reinforce knowledge of:

* Python functions

* JSON file manipulation

* Loops and conditionals

* Dictionaries and lists

* CLI application design

* Modular project structure