import tkinter as tk


def clear():
    result_var.set("")


def clear_entry():
    result_var.set(result_var.get()[:-1])


def toggle_sign():
    value = result_var.get()
    if len(value) > 0 and value[0] == "-":
        result_var.set(value[1:])
    else:
        result_var.set("-" + value)


def calculate():
    expression = history_var.get() + result_var.get()
    try:
        result = eval(expression)
    except:
        result = "Error"
    result_var.set(str(result))
    history_var.set("")


def add_number(number):
    result_var.set(result_var.get() + number)


def add_operator(operator):
    if result_var.get() == "":
        return
    if history_var.get() != "" and history_var.get()[-1] in "+-*/":
        history_var.set(history_var.get()[:-1] + operator)
        return
    history_var.set(history_var.get() + result_var.get() + operator)
    result_var.set("")


def create_button(text, x, y, command):
    button = tk.Button(root, text=text, font=('Arial', 16), width=3, height=1, bd=3, bg="#DDDDDD", command=command)
    button.place(x=x, y=y)


root = tk.Tk()
root.title("Calculator")
root.geometry("370x300")
root.resizable()

result_var = tk.StringVar()
result_var.set("")
history_var = tk.StringVar()
history_var.set("")

entry = tk.Entry(root, width=28, font=('Arial', 16), textvariable=result_var, bd=5, bg="#EEEEEE", justify=tk.RIGHT)
entry.place(x=10, y=10)

history_label = tk.Label(root, width=27, font=('Arial', 10), textvariable=history_var, bd=1, bg="#FFFFFF",
                         justify=tk.RIGHT)
history_label.place(x=10, y=50)

# create buttons
create_button("C", 10, 90, clear)
create_button("CE", 70, 90, clear_entry)
create_button("+/-", 130, 90, toggle_sign)
create_button("/", 190, 90, lambda: add_operator('/'))

create_button("7", 10, 130, lambda: add_number('7'))
create_button("8", 70, 130, lambda: add_number('8'))
create_button("9", 130, 130, lambda: add_number('9'))
create_button("*", 190, 130, lambda: add_operator('*'))

create_button("4", 10, 170, lambda: add_number('4'))
create_button("5", 70, 170, lambda: add_number('5'))
create_button("6", 130, 170, lambda: add_number('6'))
create_button("-", 190, 170, lambda: add_operator('-'))

create_button("1", 10, 210, lambda: add_number('1'))
create_button("2", 70, 210, lambda: add_number('2'))
create_button("3", 130, 210, lambda: add_number('3'))
create_button("+", 190, 210, lambda: add_operator('+'))

create_button("0", 10, 250, lambda: add_number('0'))
create_button(".", 70, 250, lambda: add_number('.'))
create_button("=", 130, 250, calculate)

root.mainloop()
