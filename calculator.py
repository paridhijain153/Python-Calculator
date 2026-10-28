
import tkinter as tk
import re

# Create the main application window
root = tk.Tk()
root.title("Python Calculator")
root.geometry("320x380")
root.resizable(False, False)

# Variable connected to the display
display = tk.StringVar()

# Create the display area
screen = tk.Entry(
    root,
    textvariable=display,
    font=("Arial", 20),
    justify="right",
    bd=8,
    relief="sunken"
)
screen.grid(row=0, column=0, columnspan=4,
            padx=10, pady=15, sticky="nsew")


# Function to handle number and operator buttons
def press(value):
    current = display.get()

    if current == "Error":
        current = ""

    display.set(current + str(value))


# Function to clear the display
def clear():
    display.set("")


# Function to calculate the expression
def calculate():
    expression = display.get().strip()

    if not expression:
        return

    # Allow only digits, decimal points, spaces,
    # parentheses, and basic arithmetic operators
    if not re.fullmatch(r"[0-9+\-*/(). ]+", expression):
        display.set("Error")
        return

    try:
        result = eval(
            expression,
            {"__builtins__": None},
            {}
        )
        display.set(str(result))

    except (ArithmeticError, SyntaxError, TypeError, ValueError):
        display.set("Error")


# Calculator button layout
buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("+", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("-", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("*", 3, 3),
    ("C", 4, 0), ("0", 4, 1), ("=", 4, 2), ("/", 4, 3)
]

# Create buttons dynamically
for (text, row, column) in buttons:
    if text == "C":
        action = clear
    elif text == "=":
        action = calculate
    else:
        action = lambda value=text: press(value)

    button = tk.Button(
        root,
        text=text,
        font=("Arial", 16),
        command=action
    )
    button.grid(
        row=row,
        column=column,
        padx=2,
        pady=2,
        sticky="nsew"
    )

# Make rows and columns expand evenly
for i in range(5):
    root.grid_rowconfigure(i, weight=1)

for i in range(4):
    root.grid_columnconfigure(i, weight=1)

# Start the application's event loop
root.mainloop()
