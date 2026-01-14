import json
from datetime import date

def makeData():
    dados = {
    "Tasks" : []
    }

    with open("banco.json", "w", encoding="utf-8") as f:
        json.dump(dados, f, ensure_ascii=False, indent=4)
    return True

def loadData():
    with open("banco.json", "r", encoding="utf-8") as f:
        return json.load(f)
    
def save(data):
    with open("banco.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def exitCLI():
    print("Shutting down system!")
    exit()
    
def createTask():

    current_date = str(date.today())

    dados = loadData()

    print("====== CREATING TASK ======")

    description = str(input("Typing Enter description: "))

    new_task = {
        "id": len(dados["Tasks"]) + 1,
        "description": description,
        "status": 'todo',
        "createdAt": current_date,
        "updateAt":None
    }

    dados["Tasks"].append(new_task)
    save(dados)

    print("\nUsuário cadastrado com sucesso!\n")