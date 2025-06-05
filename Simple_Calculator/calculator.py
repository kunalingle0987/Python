import tkinter as tk
from tkinter import messagebox

# Function to evaluate the expression
def click(event):
    global expression
    text = event.widget.cget("text")

    if text == "=":
        try:
            result = eval(expression)
            entry_var.set(result)
            expression = str(result)
        except Exception as e:
            messagebox.showerror("Error", "Invalid Expression")
            expression = ""
            entry_var.set("")
    elif text == "C":
        expression = ""
        entry_var.set("")
    else:
        expression += text
        entry_var.set(expression)

# Initialize main window
root = tk.Tk()
root.geometry("350x500")
root.title("Simple Calculator")

expression = ""
entry_var = tk.StringVar()

# Entry field
entry = tk.Entry(root, textvar=entry_var, font="Arial 20", bd=10, relief=tk.RIDGE, justify="right")
entry.pack(fill="both", ipadx=8, pady=10, padx=10)

# Button layout
button_texts = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["C", "0", "=", "+"]
]

for row_values in button_texts:
    frame = tk.Frame(root)
    frame.pack(expand=True, fill="both")

    for btn_text in row_values:
        button = tk.Button(frame, text=btn_text, font="Arial 18", relief=tk.RAISED, bd=5)
        button.pack(side="left", expand=True, fill="both", padx=5, pady=5)
        button.bind("<Button-1>", click)

# Start the GUI loop
root.mainloop()
