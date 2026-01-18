import os
import time
from datetime import date

#Exit the CLI
def exit_tasks():
    print("Shutting down system!")
    time.sleep(0.4)
    print(".")
    time.sleep(0.4)
    print(".")
    time.sleep(0.4)
    print(".")
    os.system('cls' if os.name == 'nt' else 'clear')
    exit()

#Back from update option
def back():
    os.system('cls' if os.name == 'nt' else 'clear')
    return

#Get the current date
def current_data():
    return str(date.today())