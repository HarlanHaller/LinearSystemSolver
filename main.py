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
    """logs message to output box"""
    output["text"]=message

def getValues():
    """get the values and puts them in the format {S1:{X, Y, C}, S2:{X, Y, C}, S3} S3 is for manipulation"""
    Values={"S1":{}, "S2":{}, "S3":{}}

    for value in System1:
        Values["S1"][value] = float(System1[value].get())

    for value in System2:
        Values["S2"][value] = float(System2[value].get())
        
    return Values

def errorChecks():
    """checks for errors"""
    try:
        for i in System1:
            if System1[i].get() == "":
                raise noInput
        for i in System2:
            if System2[i].get() == "": 
                raise noInput
    except noInput:
        log("Error: all input fealds require a value")
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

    if v["S1"]["X"] == 0 or v["S1"]["Y"] == 0 or v["S2"]["X"] == 0 or v["S2"]["Y"] == 0:
        log("Error: '0's cann't be provided as arguments for A or B")
        return 1

def checkEoP(x1, x2, y1, y2, c1, c2):
    """returns 2 if P, 1 if E, and 0 if nethier"""
    if x1 == x2 and y1 == y2:
        if c1 != c2:
            return 2;
        return 1;
    return 0;


def compute():
    if errorChecks() == 1:
        return
    v = getValues()
    if (checkEoP(v["S1"]["X"], v["S2"]["X"], v["S1"]["Y"], v["S2"]["Y"], v["S1"]["C"], v["S2"]["C"]) == 1): 
        log("equations are equal")
        return
    if (checkEoP(v["S1"]["X"], v["S2"]["X"], v["S1"]["Y"], v["S2"]["Y"], v["S1"]["C"], v["S2"]["C"]) == 2): 
        log("equations are parallel")
        return
    if abs(v["S1"]["X"]) == abs(v["S2"]["X"]):
        #'y's are the same without parity
        if v["S1"]["X"] == v["S2"]["X"]:
            #subtract case
            v["S3"]["Y"] = v["S1"]["Y"] - v["S2"]["Y"]
            v["S3"]["X"] = 0
            v["S3"]["C"] =  v["S1"]["C"] - v["S2"]["C"]
        else: 
            v["S3"]["Y"] = v["S1"]["Y"] + v["S2"]["Y"]
            v["S3"]["X"] = 0
            v["S3"]["C"] =  v["S1"]["C"] + v["S2"]["C"]
            
    elif abs(v["S1"]["Y"]) == abs(v["S2"]["Y"]):
        #'y's are the same without parity
        if v["S1"]["Y"] == v["S2"]["Y"]:
            #subtract case
            v["S3"]["Y"] = 0
            v["S3"]["X"] = v["S1"]["X"] - v["S2"]["X"]
            v["S3"]["C"] =  v["S1"]["C"] - v["S2"]["C"]
        else:
            #add case
            v["S3"]["X"] = v["S1"]["X"] + v["S2"]["X"]
            v["S3"]["Y"] = 0
            v["S3"]["C"] =  v["S1"]["C"] + v["S2"]["C"]
    else:
        #X's nor 'Y's not the same without parity
        highXS = ""
        if v["S1"]["X"] > v["S2"]["X"]:
            highXS = "S1"
            lowXS = "S2"
        else:
            highXS = "S2"
            lowXS = "S1"
        change = max(v["S1"]["X"],v["S2"]["X"]) / min(v["S1"]["X"],v["S2"]["X"])
        v["S3"]["X"] = 0
        v["S3"]["Y"] = v[lowXS]["Y"]-v[lowXS]["Y"]
        v["S3"]["C"] = v[lowXS]["C"]-v[lowXS]["C"]
        

submit = tk.Button(window, text="submit", width=10, height=2, highlightbackground='lightgray', fg='black', activeforeground='darkgray', command=compute).pack(pady=(10,20))
output.pack()

window.mainloop();
