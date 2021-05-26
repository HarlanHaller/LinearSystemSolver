import tkinter as tk
from tkinter.constants import RIGHT;
import tkinter.font as tkFont
from errors import *

window = tk.Tk();

window.title("System Solver");
window.geometry("500x500")

tk.Label(text="Enter systems below", font=tkFont.Font(size=30)).pack(pady=(20,0));

tk.Label(text="Enter equations in the outline below", font=tkFont.Font(size=15)).pack(pady=(5,30));

def gen_equation_temps(Frame):
    Ref_contianer = {}

    a = tk.Entry(width=3, master=Frame, justify=RIGHT)
    a.grid(column=0, row=0)
    Ref_contianer["X"] = a
    tk.Label(text="x +", master=Frame).grid(column=1, row=0)

    b = tk.Entry(width=3, master=Frame, justify=RIGHT)
    b.grid(column=2, row=0)
    Ref_contianer["Y"] = b
    tk.Label(text="y =", master=Frame).grid(column=3, row=0)

    e = tk.Entry(width=3, master=Frame, justify=RIGHT)
    e.grid(column=4, row=0)
    Ref_contianer["C"] = e

    return Ref_contianer

System1container = tk.Frame(master=window, width=500, height=20)
System1container.pack()
System1 = gen_equation_temps(System1container)
System2container = tk.Frame(master=window, width=500, height=20)
System2container.pack()
System2 = gen_equation_temps(System2container)

output = tk.Label(text="")

def log(message):
    output["text"]=message

def getValues():
    Values={"S1":{}, "S2":{}}

    for value in System1:
        Values["S1"][value] = float(System1[value].get())

    for value in System2:
        Values["S2"][value] = float(System2[value].get())
        
    return Values

def errorChecks():
    try:
        for i in System1:
            if System1[i].get() == "":
                raise noInput
        for i in System2:
            if System2[i].get() == "": 
                raise noInput
    except noInput:
        log("Error: all input fealds require a value (put 1 if you wanted the variable on its own)")
        return 1

    try:
        for i in System1:
            float(System1[i].get())
        for i in System2:
            float(System2[i].get())
    except ValueError:
        log("Error: all imputs must be numbers")
        return 1
    
    v = getValues()

    print(v["S1"]["X"])

    if v["S1"]["X"] == 0 or v["S1"]["Y"] == 0 or v["S2"]["X"] == 0 or v["S2"]["Y"] == 0:
        log("Error: '0's cann't be provided as arguments for A or B")
        return 1

def compute():
    if errorChecks() == 1:
        return
    v = getValues()
    print ("all good")
    
    


submit = tk.Button(window, text="submit", width=10, height=2, highlightbackground='lightgray', fg='black', activeforeground='darkgray', command=compute).pack(pady=(10,20))
output.pack()

window.mainloop();
