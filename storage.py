import json

# Creates the JSON file if it does not exist and initializes the default structure
def make_data(arquivo):
    # Initial data structure with an empty Tasks list
    dados = {
        "Tasks": []
    }

    # Open (or create) the file and write the JSON structure into it
    with open(arquivo, "w", encoding="utf-8") as f:
        json.dump(dados, f, ensure_ascii=False, indent=4)

    # Return True to indicate the file was created successfully
    return True

# Loads and returns the data from the JSON file
def load_data():
    # Open the JSON file in read mode
    with open("banco.json", "r", encoding="utf-8") as f:
        # Convert JSON content to a Python dictionary
        return json.load(f)

# Saves the updated data back to the JSON file
def save_data(data):
    # Open the JSON file in write mode
    with open("banco.json", "w", encoding="utf-8") as f:
        # Write the Python dictionary to the file in JSON format
        json.dump(data, f, ensure_ascii=False, indent=4)
