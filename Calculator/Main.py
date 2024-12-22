import tkinter as tk

def append_value(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + value)

def clear_display():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Create the main window
window = tk.Tk()
window.title("Calculator")
window.geometry("300x400")
window.resizable(False, False)

# Entry widget to display numbers and results
entry = tk.Entry(window, width=16, font=('Arial', 24), bd=10, insertwidth=2, bg="lightgrey", justify='right')
entry.grid(row=0, column=0, columnspan=4)

# Button layout
buttons = [
    ('C', 1, 0, clear_display), ('/', 1, 1, lambda: append_value('/')),
    ('*', 1, 2, lambda: append_value('*')), ('-', 1, 3, lambda: append_value('-')),
    ('7', 2, 0, lambda: append_value('7')), ('8', 2, 1, lambda: append_value('8')),
    ('9', 2, 2, lambda: append_value('9')), ('+', 2, 3, lambda: append_value('+')),
    ('4', 3, 0, lambda: append_value('4')), ('5', 3, 1, lambda: append_value('5')),
    ('6', 3, 2, lambda: append_value('6')), ('=', 3, 3, calculate),
    ('1', 4, 0, lambda: append_value('1')), ('2', 4, 1, lambda: append_value('2')),
    ('3', 4, 2, lambda: append_value('3')), ('0', 4, 3, lambda: append_value('0'))
]

# Add buttons to the window
for (text, row, col, command) in buttons:
    tk.Button(
        window, text=text, padx=20, pady=20, font=('Arial', 18), bg="white", command=command
    ).grid(row=row, column=col, sticky="nsew")


# Run the application
window.mainloop()
