
from tkinter import *
adarsh = Tk()
adarsh.title("Simple Calculatror")
e = Entry(adarsh, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)


def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))


def button_clear():
    e.delete(0, END)


def button_add():
    first_number = e.get()
    global f_num
    f_num = int(first_number)
    e.delete(0, END)


def button_sub():
    first_number = e.get()
    global f_num
    f_num = int(first_number)
    e.delete(0, END)


def button_mul():
    first_number = e.get()
    global f_num
    f_num = int(first_number)
    e.delete(0, END)


def button_div():
    first_number = e.get()
    global f_num
    f_num = int(first_number)
    e.delete(0, END)


def button_equal():
    second_number = e.get()
    e.delete(0, END)
    e.insert(0, f_num + int(second_number))


def button_equal():
    second_number = e.get()
    e.delete(0, END)
    e.insert(0, f_num - int(second_number))


def button_equal():
    second_number = e.get()
    e.delete(0, END)
    e.insert(0, f_num / int(second_number))


def button_equal():
    second_number = e.get()
    e.delete(0, END)
    e.insert(0, f_num * int(second_number))

# Defining the buttons


button_1 = Button(adarsh, text="1", padx=40, pady=20,
                  command=lambda: button_click(1))
button_2 = Button(adarsh, text="2", padx=40, pady=20,
                  command=lambda: button_click(2))
button_3 = Button(adarsh, text="3", padx=40, pady=20,
                  command=lambda: button_click(3))
button_4 = Button(adarsh, text="4", padx=40, pady=20,
                  command=lambda: button_click(4))
button_5 = Button(adarsh, text="5", padx=40, pady=20,
                  command=lambda: button_click(5))
button_6 = Button(adarsh, text="6", padx=40, pady=20,
                  command=lambda: button_click(6))
button_7 = Button(adarsh, text="7", padx=40, pady=20,
                  command=lambda: button_click(7))
button_8 = Button(adarsh, text="8", padx=40, pady=20,
                  command=lambda: button_click(8))
button_9 = Button(adarsh, text="9", padx=40, pady=20,
                  command=lambda: button_click(9))
button_0 = Button(adarsh, text="0", padx=40, pady=20,
                  command=lambda: button_click(0))
button_add = Button(adarsh, text="+", padx=39, pady=20, command=button_add)
button_sub = Button(adarsh, text="-", padx=40, pady=20, command=button_sub)
button_mul = Button(adarsh, text="X", padx=40, pady=20, command=button_mul)
button_div = Button(adarsh, text="/", padx=40, pady=20, command=button_div)
button_equal = Button(adarsh, text="=", padx=40, pady=20, command=button_equal)
button_clear = Button(adarsh, text="Clear", padx=30,
                      pady=20, command=button_clear)

# putting button on the sadarsheen

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=1)
button_clear.grid(row=6, column=2)
button_equal.grid(row=6, column=1)
button_sub.grid(row=4, column=2)
button_add.grid(row=4, column=0)
button_mul.grid(row=5, column=2)
button_div.grid(row=5, column=1)

adarsh.mainloop()
