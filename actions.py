import json
from datetime import date

#Creates the JSON file if it doesn't already exist.
def makeData(arquivo):
    dados = {
    "Tasks" : []
    }

    with open(arquivo, "w", encoding="utf-8") as f:
        json.dump(dados, f, ensure_ascii=False, indent=4)
    return True

#Load the JSON file.
def loadData():
    with open("banco.json", "r", encoding="utf-8") as f:
        return json.load(f)

# Save the commands
def save(data):
    with open("banco.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

#Exit the CLI
def exitCLI():
    print("Shutting down system!")
    exit()

#Create a new task
def createTask():

    current_date = str(date.today())

    dados = loadData()

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
    save(dados)

    print("\nTask added successfully (ID: {})!".format(new_task["id"]))

#Show all registers
def listAllTasks():

    dados = loadData()

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

    print("="*76 + "\n")