#IMPORT JSON AND OS LIBRARY
import os

from actions import makeData
from menu import show_menu, execute_options

ARQUIVO = "banco.json"

if not os.path.exists(ARQUIVO):
    makeData(ARQUIVO)

def main():
    while True:
        show_menu()
        escolha = input("Choose one option: ")
        execute_options(escolha)

if __name__ == "__main__":
    main()
