from storage import load_data
from utils import back

# Shows all tasks stored in the JSON file
def list_all_tasks():

    # Load data from JSON
    dados = load_data()

    # Print header
    print("\n" + "="*76)
    print(" "*30 + "TO-DO LIST")
    print("="*76)

    # Check if there are no tasks
    if not dados["Tasks"]:
        print("No tasks were found")
        return
    
    # Print table header
    print(f'{"id":<5} {"description": <30} {"status": <10} {"CreatedAt": <10} {"updateAt": <10}')
    print("-"*76)

    # Print all tasks
    for i in dados["Tasks"]:
        print(f'{i['id']:<5} {i['description']:<30} {i['status']: <10} {i['createdAt']: <10} {i['updateAt']: <10}')
        print("-"*76)

    # Print footer
    print("="*76 + "\n")


# Lists only tasks with status "todo"
def list_todo_tasks():
    # Load data from JSON
    data = load_data()

    # Flag to check if any task was found
    found = False

    # Loop through all tasks
    for task in data["Tasks"]:
        if task["status"] == "todo":
            # Print header only once
            if not found:
                print("\n" + "="*76)
                print(" "*30 + "Todo tasks")
                print("="*76)

                print(
                    f'{"id":<5} {"description": <30} {"status": <10} {"CreatedAt": <10} {"updateAt": <10}')
                print("-"*76)
                
                found = True

            # Print task data
            print(f'{task['id']:<5} {task['description']:<30} {task['status']: <10} {task['createdAt']: <10} {task['updateAt']: <10}')
            print("-"*76)
    
    # Message if no todo tasks were found
    if not found:
        print("\033[33mNo tasks todo were found.\033[0m")


# Lists only tasks with status "in-progress"
def list_progress_tasks():
    # Load data from JSON
    data = load_data()

    # Flag to check if any task was found
    found = False

    # Loop through all tasks
    for task in data["Tasks"]:
        if task["status"] == "in-progress":
            # Print header only once
            if not found:
                print("\n" + "="*76)
                print(" "*30 + "Progress tasks")
                print("="*76)

                print(
                    f'{"id":<5} {"description": <30} {"status": <10} {"CreatedAt": <10} {"updateAt": <10}')
                print("-"*76)
                
                found = True

            # Print task data
            print(f'{task['id']:<5} {task['description']:<30} {task['status']: <10} {task['createdAt']: <10} {task['updateAt']: <10}')
            print("-"*76)
    
    # Message if no tasks are in progress
    if not found:
        print("\033[33mNo tasks in progress.\033[0m")


# Lists only tasks with status "done"
def list_done_tasks():
    # Load data from JSON
    data = load_data()

    # Flag to check if any task was found
    found = False

    # Loop through all tasks
    for task in data["Tasks"]:
        if task["status"] == "done":
            # Print header only once
            if not found:
                print("\n" + "="*76)
                print(" "*30 + "Done tasks")
                print("="*76)

                print(
                    f'{"id":<5} {"description": <30} {"status": <10} {"CreatedAt": <10} {"updateAt": <10}')
                print("-"*76)
                
                found = True

            # Print task data
            print(f'{task['id']:<5} {task['description']:<30} {task['status']: <10} {task['createdAt']: <10} {task['updateAt']: <10}')
            print("-"*76)
    
    # Message if no completed tasks were found
    if not found:
        print("\033[33mNo tasks completed.\033[0m")


# Displays listing menu options
def listing_options():
    # Menu options and their respective functions
    options = {
        "1": ("List all tasks", list_all_tasks),
        "2": ("List todo tasks", list_todo_tasks),
        "3": ("list tasks in progress", list_progress_tasks),
        "4": ("List done task", list_done_tasks),  
        "0": ("Back listing", back)
    }

    # Print menu
    print("\n====== MENU ======")
    for key, (descricao, _) in options.items():
        print(f"{key} - {descricao}")

    # Ask user for an option
    option = input("Choose one option: ")

    # Execute selected option
    action = options.get(option)
    if action:
        action[1]()
