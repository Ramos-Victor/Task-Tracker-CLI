import os
from storage import make_data
from menu import show_menu, execute_options

# Path to the JSON file used as storage
FILEPATH = "banco.json"

# Create the JSON file if it does not exist
if not os.path.exists(FILEPATH):
    make_data(FILEPATH)

# Main function that runs the application loop
def main():
    while True:
        # Show the main menu
        show_menu()

        # Get the user option
        option = input("Choose one option: ")

        # Execute the selected option
        execute_options(option)

# Entry point of the application
if __name__ == "__main__":
    main()
