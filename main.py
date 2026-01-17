#IMPORT JSON AND OS LIBRARY
import os

from actions import make_data
from menu import show_menu, execute_options

FILEPATH = "banco.json"

if not os.path.exists(FILEPATH):
    make_data(FILEPATH)

def main():
    while True:
        show_menu()
        option = input("Choose one option: ")
        execute_options(option)

if __name__ == "__main__":
    main()
