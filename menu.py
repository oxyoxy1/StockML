import os
import subprocess

def main_menu():
    print("1. Edit Tickers")
    print("2. Run Main Program")
    choice = input("Choose an option: ")

    if choice == "1":
        # Open helpers.py in Notepad (or any text editor)
        subprocess.call(["notepad.exe", "helpers.py"])  # Windows
    elif choice == "2":
        # Run main program
        main_program()

def main_program():
    # Code for your main program
    pass

if __name__ == "__main__":
    main_menu()
