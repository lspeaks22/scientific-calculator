import tkinter as tk
import math

def evaluate_expression(expr):
    try:
        result = eval(expr, {
            "__builtins__": None,
            "sqrt": math.sqrt,
            "log": math.log10,
            "sin": lambda x: math.sin(math.radians(x)),
            "cos": lambda x: math.cos(math.radians(x)),
            "tan": lambda x: math.tan(math.radians(x)),
            "fact": math.factorial,
            "pow": math.pow
        })
        return result
    except Exception as e:
        return "Error."

# Button 
def click(symbol):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + symbol)

# Clear input
def clear():
    entry.delete(0, tk.END)

# Calculate result
def calculate():
    expr = entry.get()
    result = evaluate_expression(expr)
    entry.delete(0, tk.END)
    entry.insert(0, str(result))

root = tk.Tk()
root.title("Scientific Calculator")
root.configure(bg="#75bc72")

entry = tk.Entry(root, width=30, font=('Courier', 18), borderwidth=3, relief=tk.SUNKEN, justify='right')
entry.grid(row=0, column=0, columnspan=5, padx=10, pady=10)

# Buttons
buttons = [
    ['(', ')', '.', '/', 'sqrt('],
    ['7', '8', '9', '*', 'log('],
    ['4', '5', '6', '-', 'pow('],
    ['1', '2', '3', '+', 'cos('],
    ['sin(', '0', 'tan(', 'C', 'fact('],
    ['=']
]

for r, row in enumerate(buttons, start=1):
    for c, char in enumerate(row):
        if char == '=':
            tk.Button(root, text=char, width=32, height=2, font=('Courier', 14),
                      command=calculate).grid(row=r, column=0, columnspan=5, pady=5)
        elif char == 'C':
            tk.Button(root, text=char, width=6, height=2, font=('Courier', 14),
                      command=clear).grid(row=r, column=c)
        else:
            tk.Button(root, text=char, width=6, height=2, font=('Courier', 14),
                      command=lambda ch=char: click(ch)).grid(row=r, column=c)

root.mainloop()
