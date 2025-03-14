import subprocess
import os
import tkinter as tk
from tkinter import PhotoImage  # Import PhotoImage for .png support

# Define color and font settings
BACKGROUND_COLOR = "#F0F8FF"
BUTTON_COLOR = "#4CAF50"
BUTTON_TEXT_COLOR = "white"
TITLE_FONT = ("Helvetica", 16, "bold")
BUTTON_FONT = ("Arial", 12, "bold")
TEXT_COLOR = "#333333"

def create_menu():
    """Creates the main menu GUI using tkinter."""
    root = tk.Tk()
    root.title("Stock Market Machine Learning")
    
    # Set window size and color
    root.geometry("300x300")
    root.config(bg=BACKGROUND_COLOR)

    # Set the window icon (Make sure you have the icon file in the correct path)
    icon = PhotoImage(file="icon.png")  # Change the path to your icon file
    root.iconphoto(True, icon)

    # Title Label with customized font and color
    title_label = tk.Label(root, text="Welcome!", bg=BACKGROUND_COLOR, font=TITLE_FONT, fg=TEXT_COLOR)
    title_label.pack(pady=20)

    # Button to run the main program
    run_button = tk.Button(root, text="Run", font=BUTTON_FONT, bg=BUTTON_COLOR, fg=BUTTON_TEXT_COLOR)
    run_button.pack(pady=10)

    # Button to run tickers.py script
    edit_button = tk.Button(root, text="Add Tickers", font=BUTTON_FONT, bg=BUTTON_COLOR, fg=BUTTON_TEXT_COLOR)
    edit_button.pack(pady=10)

    # Button to purge tickers
    purge_button = tk.Button(root, text="Purge Tickers", font=BUTTON_FONT, bg=BUTTON_COLOR, fg=BUTTON_TEXT_COLOR)
    purge_button.pack(pady=10)

    # Run the GUI loop
    root.mainloop()

if __name__ == "__main__":
    create_menu()
