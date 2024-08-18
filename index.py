from tkinter import *
from tkinter import ttk

cor1 = "#1e1f1e" #black
cor2 = "#F8F8FF" #white
cor3 = "#38576b" #blue
cor4 = "#68838B" #grey
cor5 = "#FFAB40" #orange
window = Tk()
window.title("Calculadora")
window.geometry("320x355")
window.config(bg=cor2)
window.resizable(width=False, height=False)


frameresult = Frame(window, width=320, height=75, bg=cor4)
frameresult.grid(row=0, column=0)

framebuttons = Frame(window, width=320,  height=350, bg="BLACK")
framebuttons.grid(row=1, column=0)

#create buttons 

b_1 = Button(framebuttons, text="C", width=22, height=3, overrelief=RIDGE, bg=cor5, fg=cor2)
b_1.place(x=0, y=0)

b_2 = Button(framebuttons, text="%", width=10, height=3, overrelief=RIDGE)
b_2.place(x=162, y=0)

b_3 = Button(framebuttons, text="/", width=10, height=3, overrelief=RIDGE, bg=cor5, fg=cor2)
b_3.place(x=240, y=0)

b_4 = Button(framebuttons, text="7", width=10, height=3, overrelief=RIDGE)
b_4.place(x=0, y=56)

b_5 = Button(framebuttons, text="8", width=10, height=3, overrelief=RIDGE)
b_5.place(x=80, y=56)

b_6 = Button(framebuttons, text="9", width=10, height=3, overrelief=RIDGE)
b_6.place(x=160, y=56)

b_7 = Button(framebuttons, text="X", width=10, height=3, overrelief=RIDGE, bg=cor5, fg=cor2)
b_7.place(x=240, y=56)

b_8 = Button(framebuttons, text="4", width=10, height=3, overrelief=RIDGE)
b_8.place(x=0, y=112)

b_9 = Button(framebuttons, text="5", width=10, height=3, overrelief=RIDGE)
b_9.place(x=80, y=112)

b_10 = Button(framebuttons, text="6", width=10, height=3, overrelief=RIDGE)
b_10.place(x=160, y=112)

b_11 = Button(framebuttons, text="-", width=10, height=3, overrelief=RIDGE, bg=cor5, fg=cor2)
b_11.place(x=240, y=112)

b_12 = Button(framebuttons, text="1", width=10, height=3, overrelief=RIDGE)
b_12.place(x=0, y=168)

b_13 = Button(framebuttons, text="2", width=10, height=3, overrelief=RIDGE)
b_13.place(x=80, y=168)

b_14 = Button(framebuttons, text="3", width=10, height=3, overrelief=RIDGE)
b_14.place(x=160, y=168)

b_15 = Button(framebuttons, text="+", width=10, height=3, overrelief=RIDGE, bg=cor5, fg=cor2)
b_15.place(x=240, y=168)

b_16 = Button(framebuttons, text="0", width=22, height=3, overrelief=RIDGE, bg=cor5, fg=cor2)
b_16.place(x=0, y=224)

b_17 = Button(framebuttons, text=".", width=10, height=3, overrelief=RIDGE)
b_17.place(x=162, y=224)

b_18 = Button(framebuttons, text="=", width=10, height=3, overrelief=RIDGE, bg=cor5, fg=cor2)
b_18.place(x=240, y=224)




window.mainloop() 
