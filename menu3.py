import tkinter as tk
import subprocess

def open_edit_tickers():
    subprocess.call(["notepad.exe", "helpers.py"])  # Windows

def run_main_program():
    # Code for the main program goes here
    print("Running main program...")

def create_menu():
    root = tk.Tk()
    root.title("Stock Trend AI - oxy")
    
    # Set window size and color
    root.geometry("300x200")
    root.config(bg="lightblue")

    # Title Label
    title_label = tk.Label(root, text="Welcome!", bg="lightblue", font=("Arial", 16, "bold"))
    title_label.pack(pady=20)

    # Button to open helpers.py editor
    edit_button = tk.Button(root, text="Edit Tickers", font=("Arial", 12), command=open_edit_tickers)
    edit_button.pack(pady=10)

    # Button to run the main program
    run_button = tk.Button(root, text="Run", font=("Arial", 12), command=run_main_program)
    run_button.pack(pady=10)

    # Run the GUI loop
    root.mainloop()

if __name__ == "__main__":
    create_menu()
