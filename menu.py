from actions import createTask, exitCLI, listAllTasks


#MENU OPTIONS STORED IN TUPLES
MENU_OPTIONS = {
    "1": ("Create task", createTask),
    "2": ("List all tasks", listAllTasks),
    "0": ("Exit", exitCLI)
}

#FUNCTION THAT PERFORMS THE READING OF TUPLES
def show_menu():
    print("\n====== MENU ======")
    for key, (descricao, _) in MENU_OPTIONS.items():
        print(f"{key} - {descricao}")

#A function that executes some option.
def execute_options(opcao):
    action = MENU_OPTIONS.get(opcao)
    if action:
        action[1]()
    else:
        print("Invalid option!")