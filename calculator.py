import tkinter as tk
from tkinter import font

# --- Functions for calculator logic ---
def button_click(number):
    # Handles number button clicks, updates the entry field
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, str(current) + str(number))

def button_clear():
    # Clears the entry field
    entry.delete(0, tk.END)

def button_operation(op):
    # Stores the first number and the operation (+, -, *, /)
    global first_num, operation
    operation = op
    first_num = float(entry.get())
    entry.delete(0, tk.END)

def button_equal():
    # Calculates the result based on the selected operation
    second_num = float(entry.get())
    entry.delete(0, tk.END)
    if operation == "+":
        entry.insert(0, first_num + second_num)
    elif operation == "-":
        entry.insert(0, first_num - second_num)
    elif operation == "*":
        entry.insert(0, first_num * second_num)
    elif operation == "/":
        if second_num != 0:
            entry.insert(0, first_num / second_num)
        else:
            entry.insert(0, "Error! Division by zero")

# --- Main window setup ---
root = tk.Tk()
root.title("simple calculator")  # Sets window title
root.geometry("300x400")       # Sets window size
root.configure(bg="#f0f0f0")   # Sets background color

# --- Entry widget (display screen) ---
entry = tk.Entry(root, width=15, borderwidth=5, font=("Arial", 20), justify="right")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10, ipady=10)

# --- Button definitions (text, row, column) ---
buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), ("C", 4, 1), ("=", 4, 2), ("+", 4, 3)
]

# --- Create buttons and assign their commands ---
for (text, row, col) in buttons:
    if text == "C":
        # Clear button
        btn = tk.Button(root, text=text, padx=20, pady=20, font=("Arial", 12), command=button_clear, bg="#ff5555", fg="white")
    elif text == "=":
        # Equal button
        btn = tk.Button(root, text=text, padx=20, pady=20, font=("Arial", 12), command=button_equal, bg="#4CAF50", fg="white")
    elif text in "+-*/":
        # Operation buttons
        btn = tk.Button(root, text=text, padx=20, pady=20, font=("Arial", 12), command=lambda op=text: button_operation(op), bg="#5555ff", fg="white")
    else:
        # Number buttons
        btn = tk.Button(root, text=text, padx=20, pady=20, font=("Arial", 12), command=lambda num=text: button_click(num), bg="#333333", fg="white")
    
    btn.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")

# --- Make buttons expand to fill available space ---
for i in range(5):
    root.grid_rowconfigure(i, weight=1)
for i in range(4):
    root.grid_columnconfigure(i, weight=1)

# --- Start the Tkinter event