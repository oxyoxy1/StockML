import os
import subprocess
from colorama import init, Fore, Back, Style

# Initialize colorama
init(autoreset=True)

def main_menu():
    print(f"{Back.GREEN}{Fore.BLACK}{Style.BRIGHT}Welcome to the Ticker Program{Style.RESET_ALL}")
    print(f"{Fore.CYAN}--------------------------------------------------")
    print(f"{Fore.YELLOW}{Style.BRIGHT}1. Edit Tickers")
    print(f"{Fore.YELLOW}{Style.BRIGHT}2. Run Main Program")
    print(f"{Fore.CYAN}--------------------------------------------------")
    
    choice = input(f"{Fore.MAGENTA}{Style.BRIGHT}Choose an option (1 or 2): {Style.RESET_ALL}")
    
    if choice == "1":
        # Open helpers.py in Notepad (or any text editor)
        subprocess.call(["notepad.exe", "helpers.py"])  # Windows
    elif choice == "2":
        # Run main program
        main_program()
    else:
        print(f"{Fore.RED}{Style.BRIGHT}Invalid choice. Please enter 1 or 2.")
        main_menu()

def main_program():
    # Code for your main program goes here
    print(f"{Fore.GREEN}Running main program...")

if __name__ == "__main__":
    main_menu()
