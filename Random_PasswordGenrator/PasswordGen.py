import tkinter as tk
from tkinter import messagebox
import random
import string

# Function to generate password
def generate_password():
    try:
        length = int(length_entry.get())
        if length <= 0:
            raise ValueError("Length must be positive")

        chars = string.ascii_lowercase
        if uppercase_var.get():
            chars += string.ascii_uppercase
        if digits_var.get():
            chars += string.digits
        if special_var.get():
            chars += string.punctuation

        if not chars:
            raise ValueError("No character types selected")

        password = ''.join(random.choice(chars) for _ in range(length))
        result_var.set(password)

    except ValueError as e:
        messagebox.showerror("Error", str(e))
        result_var.set("")

# GUI Setup
root = tk.Tk()
root.title("Random Password Generator")
root.geometry("400x300")
root.resizable(False, False)

# Variables
result_var = tk.StringVar()
uppercase_var = tk.BooleanVar()
digits_var = tk.BooleanVar()
special_var = tk.BooleanVar()

# Widgets
tk.Label(root, text="Password Length:", font="Arial 12").pack(pady=5)
length_entry = tk.Entry(root, font="Arial 12", justify="center")
length_entry.pack(pady=5)

tk.Checkbutton(root, text="Include Uppercase Letters", variable=uppercase_var, font="Arial 10").pack(anchor="w", padx=20)
tk.Checkbutton(root, text="Include Numbers", variable=digits_var, font="Arial 10").pack(anchor="w", padx=20)
tk.Checkbutton(root, text="Include Special Characters", variable=special_var, font="Arial 10").pack(anchor="w", padx=20)

tk.Button(root, text="Generate Password", command=generate_password, font="Arial 12 bold", bg="#007BFF", fg="white").pack(pady=15)

tk.Entry(root, textvariable=result_var, font="Arial 12", justify="center", bd=3).pack(ipady=5, padx=20)

# Start loop
root.mainloop()
