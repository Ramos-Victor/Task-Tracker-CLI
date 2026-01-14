from actions import createTask, exitCLI

MENU_OPTIONS = {
    "1": ("Create task", createTask),
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
        print("Opção inválida!")