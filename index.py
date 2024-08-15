from tkinter import *
from tkinter import ttk



window = Tk()
window.title("Calculadora")
window.geometry("350x300")

resultframe = Frame(window,width=330, height=80, bg="black" )
framebuttons = Frame(window, width=350,  height=200, bg="black")

resultframe.pack(side=TOP, padx=10, pady=10)
framebuttons.pack(side=LEFT, padx=10, pady=10)

buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
    ('C', 5, 0)
]

for (text, row, col) in buttons:
    button = ttk.Button(framebuttons, text=text, width=15, height=2)
    button.grid(row=row, column=col)

window.mainloop() 


    