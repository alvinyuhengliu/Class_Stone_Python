import tkinter as tk

def on_click(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + value)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def clear_entry():
    entry.delete(0, tk.END)

# Create the main window
window = tk.Tk()
window.title("Basic Calculator")

# Create an entry widget for input
entry = tk.Entry(window, width=20, font=('Arial', 14))
entry.grid(row=0, column=0, columnspan=4)

# Define the calculator buttons
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '+', '10'
]

# Add buttons to the grid
row_val = 1
col_val = 0

for button in buttons:
    tk.Button(window, text=button, width=5, height=2, command=lambda b=button: on_click(b)).grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Additional buttons
tk.Button(window, text='Clear', width=5, height=2, command=clear_entry).grid(row=row_val, column=0)
tk.Button(window, text='Quit', width=5, height=2, command=window.destroy).grid(row=row_val, column=1)

# '=' button
tk.Button(window, text='=', width=5, height=2, command=calculate).grid(row=row_val, column=2, columnspan=2)

# Run the Tkinter event loop
window.mainloop()
