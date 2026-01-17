import json
from datetime import date

#Creates the JSON file if it doesn't already exist.
def make_data(arquivo):
    dados = {
    "Tasks" : []
    }

    with open(arquivo, "w", encoding="utf-8") as f:
        json.dump(dados, f, ensure_ascii=False, indent=4)
    return True

#Load the JSON file.
def load_data():
    with open("banco.json", "r", encoding="utf-8") as f:
        return json.load(f)

# Save the commands
def save_data(data):
    with open("banco.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

#Exit the CLI
def exit_tasks():
    print("Shutting down system!")
    exit()

#Create a new task
def create_task():

    current_date = current_data()

    dados = load_data()

    print("====== ADDING A NEW TASK ======\n")

    description = str(input("Enter your new task: ")).strip()

    new_task = {
        "id": len(dados["Tasks"]) + 1,
        "description": description,
        "status": 'todo',
        "createdAt": current_date,
        "updateAt": ""
    }

    dados["Tasks"].append(new_task)
    save_data(dados)

    print("\nTask added successfully (ID: {})!".format(new_task["id"]))

#Updating the task description 
def update_description(index):

    data = load_data()

    try:
        data["Tasks"][index]["description"] = str(input("Type a new description: "))

        data["Tasks"][index]["updateAt"] = current_data()

        save_data(data)
        
        print(f"\033[32mTask updated successfully!\033[0m")

    except ValueError:
        print("\033[31mThe task could not be updated.\033[0m")
        return

#Updating the task status
def update_status(index):
    data = load_data()

    try:
        status_options = {
                "2": "todo",
                "1": "in-progress",
                "0": "Done"
        }

        print("\n====== MENU ======")
        for key, descricao in status_options.items():
            print(f"{key} - {descricao}")

        option = input("Choose one option: ")

        action = status_options.get(option)
        if action:
            data["Tasks"][index]["status"] = action

            data["Tasks"][index]["updateAt"] = current_data()

            save_data(data)
        
            print(f"\033[32mTask updated successfully!\033[0m")
        else:
            print("Invalid option!")

    except ValueError:
        print("\033[31mThe task could not be updated.\033[0m")
        return

#Back from update option
def back_update():
    return

#Get the current date
def current_data():
    return str(date.today())

#Updating task
def updating_task():
    try:
        id_task = int(input("Enter the ID of the task you want to update: \n"))
    except ValueError:
        print("ID inválido")
        return

    data = load_data()

    for index, task in enumerate(data["Tasks"]):
        if task["id"] == id_task:
            print(
                f"Task selected:\n"
                f"\033[32mID\033[0m: {task['id']}\n"
                f"\033[32mDescription\033[0m: {task['description']}\n"
                f"\033[32mStatus\033[0m: {task['status']}"
            )

            sub_options = {
                "1": ("Update description", lambda: update_description(index)),
                "2": ("Update status",      lambda: update_status(index)),
                "0": ("Voltar", back_update)
            }

            print("\n====== MENU ======")
            for key, (descricao, _) in sub_options.items():
                print(f"{key} - {descricao}")

            option = input("Choose one option: ")

            action = sub_options.get(option)
            if action:
                action[1]()
            else:
                print("Invalid option!")

            return

    print("\033[31mTask não encontrada!\033[0m")

#Show all registers
def list_all_tasks():

    dados = load_data()

    print("\n" + "="*76)
    print(" "*30 + "TO-DO LIST")
    print("="*76)

    if not dados["Tasks"]:
        print("No tasks were found")
        return
    
    print(f'{"id":<5} {"description": <30} {"status": <10} {"CreatedAt": <10} {"updateAt": <10}')
    print("-"*76)

    for i in dados["Tasks"]:
        print(f'{i['id']:<5} {i['description']:<30} {i['status']: <10} {i['createdAt']: <10} {i['updateAt']: <10}')
        print("-"*76)

    print("="*76 + "\n")