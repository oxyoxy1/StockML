import tkinter as tk
from tkinter import PhotoImage  # Import PhotoImage for .png support
import subprocess
import os

# Define color and font settings
BACKGROUND_COLOR = "#F0F8FF"  # Light blue color using HEX
BUTTON_COLOR = "#4CAF50"      # Green button color
BUTTON_TEXT_COLOR = "white"   # White text for buttons
TITLE_FONT = ("Helvetica", 16, "bold")  # Font for the title
BUTTON_FONT = ("Arial", 12, "bold")     # Font for the buttons
TEXT_COLOR = "#333333"         # Dark text color for labels

def run_tickers_script():
    """Runs the tickers.py script to allow interactive ticker editing."""
    try:
        subprocess.call(["python", "tickers.py"])
    except Exception as e:
        print(f"Error running tickers.py: {e}")

def purge_tickers():
    """Purges tickers from the helpers.py file."""
    try:
        with open("helpers.py", "r") as file:
            lines = file.readlines()

        # Search for the line that contains the tickers and clear it
        for i, line in enumerate(lines):
            if "return [" in line:
                lines[i] = "    return []\n"  # Clear the tickers list

        # Write the updated lines back to helpers.py
        with open("helpers.py", "w") as file:
            file.writelines(lines)
        
        print("Tickers purged from helpers.py.")
    except FileNotFoundError:
        print("Error: helpers.py not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def run_main_program():
    """Runs the main program from main.py."""
    try:
        import main  # Import main.py to run the program
        main.run_main_program()  # Call the function that runs your main program
    except Exception as e:
        print(f"Error running the main program: {e}")

def create_menu():
    """Creates the main menu GUI using tkinter."""
    root = tk.Tk()
    root.title("Ticker Program Menu")
    
    # Set window size and color
    root.geometry("300x300")
    root.config(bg=BACKGROUND_COLOR)

    # Set the window icon (Make sure you have the icon file in the correct path)
    icon = PhotoImage(file="icon.png")  # Change the path to your icon file
    root.iconphoto(True, icon)

    # Title Label with customized font and color
    title_label = tk.Label(root, text="Welcome to Ticker Program", bg=BACKGROUND_COLOR, font=TITLE_FONT, fg=TEXT_COLOR)
    title_label.pack(pady=20)

    # Button to run tickers.py script
    edit_button = tk.Button(root, text="Edit Tickers", font=BUTTON_FONT, bg=BUTTON_COLOR, fg=BUTTON_TEXT_COLOR, command=run_tickers_script)
    edit_button.pack(pady=10)

    # Button to run the main program
    run_button = tk.Button(root, text="Run Main Program", font=BUTTON_FONT, bg=BUTTON_COLOR, fg=BUTTON_TEXT_COLOR, command=run_main_program)
    run_button.pack(pady=10)

    # Button to purge tickers
    purge_button = tk.Button(root, text="Purge Tickers", font=BUTTON_FONT, bg=BUTTON_COLOR, fg=BUTTON_TEXT_COLOR, command=purge_tickers)
    purge_button.pack(pady=10)

    # Run the GUI loop
    root.mainloop()

if __name__ == "__main__":
    create_menu()
