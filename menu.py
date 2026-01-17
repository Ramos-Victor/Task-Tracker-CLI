from actions import create_task, exit_tasks, list_all_tasks, updating_task


#MENU OPTIONS STORED IN TUPLES
MENU_OPTIONS = {
    "1": ("Create task", create_task),
    "2": ("List all tasks", list_all_tasks),
    "3": ("Updating tasks", updating_task),
    "0": ("Exit", exit_tasks)
}

#FUNCTION THAT PERFORMS THE READING OF TUPLES
def show_menu():
    print("\n====== MENU ======")
    for key, (descricao, _) in MENU_OPTIONS.items():
        print(f"{key} - {descricao}")

#A function that executes some option.
def execute_options(option):
    action = MENU_OPTIONS.get(option)
    if action:
        action[1]()
    else:
        print("Invalid option!")