"""
GUI implementation using Tkinter.
"""

import tkinter as tk
from tkinter import messagebox
from app.generator import PasswordGenerator

class PasswordGeneratorGUI:
    """
    A class to manage the GUI for the password generator.
    """
    MIN_PASSWORD_LENGTH = 4
    MAX_PASSWORD_LENGTH = 64

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Password Generator")

        # Set minimum size and prevent resizing
        self.root.geometry("300x200")  # Set the initial size (width x height)
        self.root.resizable(False, False)  # Prevent window resizing

        # Length Label and Entry
        self.length_label = tk.Label(self.root, text="Password Length:")
        self.length_label.pack()
        self.length_entry = tk.Entry(self.root)
        self.length_entry.pack()

        # Options for digits and special characters
        self.digits_var = tk.BooleanVar(value=True)
        self.special_var = tk.BooleanVar(value=True)
        self.digits_check = tk.Checkbutton(self.root, text="Include Digits", variable=self.digits_var)
        self.special_check = tk.Checkbutton(self.root, text="Include Special Characters", variable=self.special_var)
        self.digits_check.pack()
        self.special_check.pack()

        # Generate Button
        self.generate_button = tk.Button(self.root, text="Generate Password", command=self.generate_password)
        self.generate_button.pack(pady=(10, 20))  # Add padding before and after the button

        # Result Label
        self.result_label = tk.Label(self.root, text="", font=("Helvetica", 12, "bold"))
        self.result_label.pack()

    def validate_length(self, length):
        """
        Validate the password length to ensure it's within allowed limits.
        """
        if not length.strip().isdigit():
            raise ValueError("Password length must be a valid positive integer.")
        
        length = int(length)
        
        if length < self.MIN_PASSWORD_LENGTH:
            raise ValueError(f"Password length must be at least {self.MIN_PASSWORD_LENGTH} characters.")
        if length > self.MAX_PASSWORD_LENGTH:
            raise ValueError(f"Password length cannot exceed {self.MAX_PASSWORD_LENGTH} characters.")

    def generate_password(self):
        """
        Generate a password and display it in the GUI.
        """
        try:
            length_input = self.length_entry.get()
            self.validate_length(length_input)

            length = int(length_input)
            use_digits = self.digits_var.get()
            use_special = self.special_var.get()
            password = PasswordGenerator.generate(length, use_digits, use_special)
            self.result_label.config(text=password)
        except ValueError as e:
            messagebox.showerror("Invalid Input", str(e))

    def run(self):
        """
        Run the Tkinter main loop.
        """
        self.root.mainloop()