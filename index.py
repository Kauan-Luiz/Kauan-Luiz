from tkinter import *
from tkinter import ttk

cor1 = "#1e1f1e" #black
cor2 = "#fefff" #white
cor3 = "#38576b" #blue
cor4 = "#ECEFF1" #grey
cor5 = "#FFAB40" #orange
window = Tk()
window.title("Calculadora")
window.geometry("235x318")
window.config(bg=cor1)

frameresult = Frame(window, width=235, height=50, bg=cor4)
framebuttons = Frame(window, width=235,  height=200, bg="black")

frameresult.grid(row=0, column=0, pady="10")
framebuttons.grid(row=1, column=0)


window.mainloop() 


    