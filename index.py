from tkinter import *
from tkinter import ttk

cor1 = "#1e1f1e" #black
cor2 = "#F8F8FF" #white
cor3 = "#38576b" #blue
cor4 = "#68838B" #grey
cor5 = "#FFAB40" #orange
window = Tk()
window.title("Calculadora")
window.geometry("320x430")
window.config(bg=cor2)
window.resizable(width=False, height=False)


frameresult = Frame(window, width=320, height=75, bg=cor4)
frameresult.grid(row=0, column=0)

framebuttons = Frame(window, width=320,  height=350, bg="white")
framebuttons.grid(row=1, column=0)

#create buttons 

b_1 = Button(framebuttons, text="C", width=20, height=3, overrelief=RIDGE)
b_1.grid(row=0, column=0)

b_2 = Button(framebuttons, text="%", width=10, height=3, overrelief=RIDGE)
b_2.grid(row=0, column=1)

b_3 = Button(framebuttons, text="/", width=10, height=3, overrelief=RIDGE, bg=cor5, fg=cor2)
b_3.grid(row=0, column=2)

b_4 = Button(framebuttons, text="7", width=10, height=3, overrelief=RIDGE)
b_4.grid(row=1, column=0)

b_5 = Button(framebuttons, text="8", width=10, height=3, overrelief=RIDGE)
b_5.grid(row=1, column=1)

b_6 = Button(framebuttons, text="9", width=10, height=3, overrelief=RIDGE)
b_6.grid(row=1, column=2)

b_7 = Button(framebuttons, text="X", width=10, height=3, overrelief=RIDGE, bg=cor5, fg=cor2)
b_7.grid(row=1, column=3)





window.mainloop() 
