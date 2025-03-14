import tkinter as tk
import subprocess
import os

def run_tickers_script():
    """Runs the tickers.py script to allow interactive ticker editing."""
    try:
        # Run tickers.py as a Python script
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
    root.config(bg="lightblue")

    # Title Label
    title_label = tk.Label(root, text="Welcome to Ticker Program", bg="lightblue", font=("Arial", 16, "bold"))
    title_label.pack(pady=20)

    # Button to run tickers.py script
    edit_button = tk.Button(root, text="Edit Tickers", font=("Arial", 12), command=run_tickers_script)
    edit_button.pack(pady=10)

    # Button to run the main program
    run_button = tk.Button(root, text="Run Main Program", font=("Arial", 12), command=run_main_program)
    run_button.pack(pady=10)

    # Button to purge tickers
    purge_button = tk.Button(root, text="Purge Tickers", font=("Arial", 12), command=purge_tickers)
    purge_button.pack(pady=10)

    # Run the GUI loop
    root.mainloop()

if __name__ == "__main__":
    create_menu()
