import tkinter as tk
from tkinter.constants import RIGHT;
import tkinter.font as tkFont

window = tk.Tk();

window.title("System Solver");
window.geometry("500x500")

tk.Label(text="Enter systems below", font=tkFont.Font(size=30)).pack(pady=(20,0));

tk.Label(text="Enter equations in the outline below", font=tkFont.Font(size=15)).pack(pady=(5,30));

def gen_equation_temps(Frame):
    Ref_contianer = {}

    Ref_contianer["X"] = tk.Entry(width=3, master=Frame, justify=RIGHT).grid(column=0, row=0)
    tk.Label(text="x +", master=Frame).grid(column=1, row=0)

    Ref_contianer["Y"] = tk.Entry(width=3, master=Frame, justify=RIGHT).grid(column=2, row=0)
    tk.Label(text="y =", master=Frame).grid(column=3, row=0)

    Ref_contianer["C"] = tk.Entry(width=3, master=Frame, justify=RIGHT).grid(column=4, row=0)

    return Ref_contianer

System1container = tk.Frame(master=window, width=500, height=20)
System1container.pack()
System1 = gen_equation_temps(System1container)
System2container = tk.Frame(master=window, width=500, height=20)
System2container.pack()
System2 = gen_equation_temps(System2container)

output = tk.Label(text="")

def compute(event):
    print (event)
    output["text"]="(3, 5)";

submit = tk.Button(window, text="submit", width=10, height=2, highlightbackground='lightgray', fg='black', activeforeground='darkgray')
submit.bind("<Button-1>", compute)
submit.pack(pady=(10,20))

output.pack()

window.mainloop();
