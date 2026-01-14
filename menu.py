from actions import createTask, exitCLI, listAllTasks

MENU_OPTIONS = {
    "1": ("Create task", createTask),
    "2": ("List all tasks", listAllTasks),
    "0": ("Exit", exitCLI)
}

def show_menu():
    print("\n====== MENU ======")
    for key, (descricao, _) in MENU_OPTIONS.items():
        print(f"{key} - {descricao}")

def execute_options(opcao):
    action = MENU_OPTIONS.get(opcao)
    if action:
        action[1]()
    else:
        print("Invalid option!")