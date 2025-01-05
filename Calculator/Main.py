import tkinter as tk  # We are using a tool called tkinter to make a simple app.

# This function adds a number or symbol to the calculator screen.
def append_value(value):
    current = entry.get()  # Take what's already on the screen.
    entry.delete(0, tk.END)  # Clear the screen.
    entry.insert(0, current + value)  # Add the new number or symbol to the old one.

# This function clears everything on the calculator screen.
def clear_display():
    entry.delete(0, tk.END)  # Wipe the screen clean.

# This function does the math for us!
def calculate():
    try:
        result = eval(entry.get())  # Solve the math problem written on the screen.
        entry.delete(0, tk.END)  # Clear the screen.
        entry.insert(0, str(result))  # Show the answer.
    except:  # If something goes wrong...
        entry.delete(0, tk.END)  # Clear the screen.
        entry.insert(0, "Error")  # Show "Error" on the screen.

# We are making the main calculator window here.
window = tk.Tk()  # Create a new window.
window.title("Calculator")  # Name the window "Calculator."
window.geometry("300x400")  # Set the size of the window.
window.resizable(False, False)  # Stop the window from being resized.

# This is the calculator screen where we see numbers and answers.
entry = tk.Entry(
    window, width=16, font=('Arial', 24), bd=10, insertwidth=2, 
    bg="lightgrey", justify='right'
)  # Make the screen look nice and put numbers to the right side.
entry.grid(row=0, column=0, columnspan=4)  # Put the screen at the top of the calculator.

# Here we define all the calculator buttons and what they do.
buttons = [
    ('C', 1, 0, clear_display),  # Clear button to erase everything.
    ('/', 1, 1, lambda: append_value('/')),  # Button to divide numbers.
    ('*', 1, 2, lambda: append_value('*')),  # Button to multiply numbers.
    ('-', 1, 3, lambda: append_value('-')),  # Button to subtract numbers.
    ('7', 2, 0, lambda: append_value('7')),  # Button for the number 7.
    ('8', 2, 1, lambda: append_value('8')),  # Button for the number 8.
    ('9', 2, 2, lambda: append_value('9')),  # Button for the number 9.
    ('+', 2, 3, lambda: append_value('+')),  # Button to add numbers.
    ('4', 3, 0, lambda: append_value('4')),  # Button for the number 4.
    ('5', 3, 1, lambda: append_value('5')),  # Button for the number 5.
    ('6', 3, 2, lambda: append_value('6')),  # Button for the number 6.
    ('=', 3, 3, calculate),  # Button to calculate the answer.
    ('1', 4, 0, lambda: append_value('1')),  # Button for the number 1.
    ('2', 4, 1, lambda: append_value('2')),  # Button for the number 2.
    ('3', 4, 2, lambda: append_value('3')),  # Button for the number 3.
    ('0', 4, 3, lambda: append_value('0'))   # Button for the number 0.
]

# Now, we create the buttons and add them to the window.
for (text, row, col, command) in buttons:
    tk.Button(
        window, text=text, padx=20, pady=20, font=('Arial', 18), bg="white", 
        command=command
    ).grid(row=row, column=col, sticky="nsew")  # Make the button look good and put it in the right spot.

# This is like flipping the "on" switch for our calculator.
window.mainloop()  # Keep the calculator window open so we can use it.
