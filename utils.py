import os
import time
from datetime import date

# Function to exit the CLI application
def exit_tasks():
    # Display a shutdown message
    print("Shutting down system!")
    
    # Create a small delay with dots for visual effect
    time.sleep(0.4)
    print(".")
    time.sleep(0.4)
    print(".")
    time.sleep(0.4)
    print(".")
    
    # Clear the terminal screen (Windows or Linux/Mac)
    os.system('cls' if os.name == 'nt' else 'clear')
    
    # End the program
    exit()

# Function to go back to the previous menu
def back():
    # Clear the terminal screen
    os.system('cls' if os.name == 'nt' else 'clear')
    
    # Return to the caller function
    return

# Function to get the current date
def current_data():
    # Return today's date as a string (YYYY-MM-DD)
    return str(date.today())
