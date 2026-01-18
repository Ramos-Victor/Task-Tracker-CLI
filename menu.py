from task import create_task, updating_task, delete_task
from listtask import listing_options
from utils import exit_tasks

# Stores the main menu options and their respective functions
MENU_OPTIONS = {
    "1": ("Create task", create_task),
    "2": ("Listing options", listing_options),
    "3": ("Updating tasks", updating_task),
    "4": ("Delete task", delete_task),
    "0": ("Exit", exit_tasks)
}

# Displays the main menu on the terminal
def show_menu():
    # Print menu title
    print("\n====== MENU ======")

    # Loop through the menu options and display them
    for key, (descricao, _) in MENU_OPTIONS.items():
        print(f"{key} - {descricao}")

# Executes the selected menu option
def execute_options(option):
    # Get the selected action from the menu options
    action = MENU_OPTIONS.get(option)

    # If the option exists, execute its function
    if action:
        action[1]()
    else:
        # Message for invalid option
        print("Invalid option!")
