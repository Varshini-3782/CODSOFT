from tkinter import *
import tkinter.font as font

# Function to update expression
def press(key):
    entry_text.set(entry_text.get() + str(key))

# Function to evaluate the final expression
def equalpress():
    try:
        total = str(eval(entry_text.get()))
        entry_text.set(total)
    except:
        entry_text.set("Error")

# Function to clear the entry field
def clear():
    entry_text.set("")

# Create main window
root = Tk()
root.title("Calculator")
root.geometry("300x400")
root.resizable(False, False)

# Entry widget to show calculations
entry_text = StringVar()
entry = Entry(root, textvariable=entry_text, font=('Arial', 20), bd=10, insertwidth=2, width=14, borderwidth=4, relief='ridge', justify='right')
entry.grid(row=0, column=0, columnspan=4)

# Font for buttons
myFont = font.Font(size=14)

# Button layout
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
    ('C', 5, 0)
]

for (text, row, col) in buttons:
    if text == '=':
        Button(root, text=text, padx=20, pady=20, bd=5, font=myFont, command=equalpress).grid(row=row, column=col)
    elif text == 'C':
        Button(root, text=text, padx=88, pady=20, bd=5, font=myFont, command=clear).grid(row=row, column=col, columnspan=3)
    else:
        Button(root, text=text, padx=20, pady=20, bd=5, font=myFont, command=lambda t=text: press(t)).grid(row=row, column=col)

# Run the app
root.mainloop()