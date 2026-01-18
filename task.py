from storage import load_data, save_data
from utils import current_data, back


# Creates a new task and saves it to the JSON file
def create_task():

    # Get the current date
    current_date = current_data()

    # Load existing data
    dados = load_data()

    # Display header
    print("====== ADDING A NEW TASK ======\n")

    # Ask the user for the task description
    description = str(input("Enter your new task: ")).strip()

    # Create the task structure
    new_task = {
        "id": len(dados["Tasks"]) + 1,   # Generate a new ID
        "description": description,      # Task description
        "status": 'todo',                # Default status
        "createdAt": current_date,       # Creation date
        "updateAt": ""                   # Update date (empty at creation)
    }

    # Add the task to the list
    dados["Tasks"].append(new_task)

    # Save updated data
    save_data(dados)

    # Success message
    print("\nTask added successfully (ID: {})!".format(new_task["id"]))


# Updates the description of an existing task
def update_description(index):

    # Load data from JSON
    data = load_data()

    try:
        # Ask for a new description
        data["Tasks"][index]["description"] = str(input("Type a new description: "))

        # Update the update date
        data["Tasks"][index]["updateAt"] = current_data()

        # Save changes
        save_data(data)
        
        # Success message
        print(f"\033[32mTask updated successfully!\033[0m")

    except ValueError:
        # Error message if update fails
        print("\033[31mThe task could not be updated.\033[0m")
        return


# Updates the status of an existing task
def update_status(index):
    # Load data from JSON
    data = load_data()

    try:
        # Get the current task status
        current_status = data["Tasks"][index]["status"]

        # Available status options
        status_options = {
            "1": "todo",
            "2": "in-progress",
            "0": "done"
        }

        # Remove the current status from the menu
        filtered_options = {
            key: value
            for key, value in status_options.items()
            if value != current_status
        }

        # Display status menu
        print("\n====== UPDATE STATUS ======")
        for key, descricao in filtered_options.items():
            print(f"{key} - {descricao}")

        # Ask the user to choose a new status
        option = input("Choose one option: ")

        # Get the selected status
        new_status = filtered_options.get(option)
        if new_status:
            # Update status and update date
            data["Tasks"][index]["status"] = new_status
            data["Tasks"][index]["updateAt"] = current_data()

            # Save changes
            save_data(data)

            # Success message
            print("\033[32mTask updated successfully!\033[0m")
        else:
            # Invalid option message
            print("\033[31mInvalid option!\033[0m")

    except (IndexError, KeyError):
        # Error message if update fails
        print("\033[31mThe task could not be updated.\033[0m")


# Allows the user to choose and update a task
def updating_task():
    try:
        # Ask for the task ID
        id_task = int(input("Enter the ID of the task you want to update: \n"))
    except ValueError:
        # Invalid ID message
        print("ID inválido")
        return

    # Load data from JSON
    data = load_data()

    # Search for the task by ID
    for index, task in enumerate(data["Tasks"]):
        if task["id"] == id_task:
            # Display selected task details
            print(
                f"Task selected:\n"
                f"\033[32mID\033[0m: {task['id']}\n"
                f"\033[32mDescription\033[0m: {task['description']}\n"
                f"\033[32mStatus\033[0m: {task['status']}"
            )

            # Sub-menu options
            sub_options = {
                "1": ("Update description", lambda: update_description(index)),
                "2": ("Update status",      lambda: update_status(index)),
                "0": ("Voltar", back)
            }

            # Display menu
            print("\n====== MENU ======")
            for key, (descricao, _) in sub_options.items():
                print(f"{key} - {descricao}")

            # Get user option
            option = input("Choose one option: ")

            # Execute selected action
            action = sub_options.get(option)
            if action:
                action[1]()
            else:
                print("Invalid option!")

            return

    # Message if task is not found
    print("\033[31mTask not found!\033[0m")


# Deletes a task by ID
def delete_task():
    # Load data from JSON
    data = load_data()

    try:
        # Ask for the task ID
        selected_task = int(input("Enter the ID of the task you want to delete: "))
    except ValueError:
        # Invalid ID message
        print("\033[31mInvalid ID!\033[0m")
        return

    # Search for the task
    for index, task in enumerate(data["Tasks"]):
        if task["id"] == selected_task:
            # Remove the task
            del data["Tasks"][index]

            # Reorganize task IDs
            for new_id, task in enumerate(data["Tasks"], start=1):
                task["id"] = new_id

            # Save changes
            save_data(data)

            # Success message
            print("\033[32mTask deleted successfully!\033[0m")
            return

    # Message if task is not found
    print("\033[31mTask not found!\033[0m")
