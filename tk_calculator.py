import tkinter as tk
import math

def press(key):
    entry_var.set(entry_var.get() + str(key))

def evaluate():
    try:
        result = str(eval(entry_var.get()))
        entry_var.set(result)
    except Exception:
        entry_var.set("Error")

def clear():
    entry_var.set("")

def square():
    try:
        value = float(entry_var.get())
        entry_var.set(str(value ** 2))
    except:
        entry_var.set("Error")

def square_root():
    try:
        value = float(entry_var.get())
        entry_var.set(str(math.sqrt(value)))
    except:
        entry_var.set("Error")

root = tk.Tk()
root.title("Cool Calculator with Square & Root")
root.configure(bg="#1e1e2f")

entry_var = tk.StringVar()
entry = tk.Entry(root, textvariable=entry_var, font=("Consolas", 24), bd=0, width=18,
                 justify='right', bg="#2e2e3e", fg="#00f7ff", insertbackground="#00f7ff")
entry.grid(row=0, column=0, columnspan=4, padx=16, pady=20, ipady=10)

buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('C', 4, 2), ('+', 4, 3),
    ('x²', 5, 0), ('√', 5, 1), ('=', 5, 2, 2)
]

btn_bg = "#3b3e59"
btn_fg = "#f5f6fa"
btn_active = "#00f7ff"
btn_equal_bg = "#00f7ff"
btn_equal_fg = "#1e1e2f"

for btn in buttons:
    text = btn[0]
    row = btn[1]
    col = btn[2]
    colspan = btn[3] if len(btn) == 4 else 1

    if text == '=':
        action = evaluate
    elif text == 'C':
        action = clear
    elif text == 'x²':
        action = square
    elif text == '√':
        action = square_root
    else:
        action = lambda x=text: press(x)

    bg_color = btn_equal_bg if text == '=' else btn_bg
    fg_color = btn_equal_fg if text == '=' else btn_fg

    tk.Button(root, text=text, command=action,
              font=("Consolas", 18, 'bold'), bg=bg_color, fg=fg_color,
              activebackground=btn_active, activeforeground="#1e1e2f",
              bd=0, padx=20, pady=20).grid(row=row, column=col, columnspan=colspan,
                                           sticky="nsew", padx=6, pady=6)

for i in range(6):
    root.grid_rowconfigure(i, weight=1)
for i in range(4):
    root.grid_columnconfigure(i, weight=1)

root.mainloop()
