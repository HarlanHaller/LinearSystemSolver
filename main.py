import tkinter as tk
from tkinter.constants import RIGHT;
import tkinter.font as tkFont

window = tk.Tk();

window.title("System Solver");
window.geometry("500x500")

tk.Label(text="Enter systems below", font=tkFont.Font(size=30)).pack(pady=(20,0));

tk.Label(text="Enter equations in the outline below", font=tkFont.Font(size=15)).pack(pady=(5,30));

System1container = tk.Frame(master=window, width=500, height=20)
System1container.pack()

S1A = tk.Entry(width=3, master=System1container, justify=RIGHT).grid(column=0, row=0)
tk.Label(text="x +", master=System1container).grid(column=1, row=0)

S1B = tk.Entry(width=3, master=System1container, justify=RIGHT).grid(column=2, row=0)
tk.Label(text="y =", master=System1container).grid(column=3, row=0)

S1C = tk.Entry(width=3, master=System1container, justify=RIGHT).grid(column=4, row=0)

System2container = tk.Frame(master=window, width=500, height=20)
System2container.pack()

S2A = tk.Entry(width=3, master=System2container, justify=RIGHT).grid(column=0, row=0)
tk.Label(text="x +", master=System2container).grid(column=1, row=0)

S2B = tk.Entry(width=3, master=System2container, justify=RIGHT).grid(column=2, row=0)
tk.Label(text="y =", master=System2container).grid(column=3, row=0)

S2C = tk.Entry(width=3, master=System2container, justify=RIGHT).grid(column=4, row=0)

output = tk.Label(text="")

def compute(event):
    print (event)
    output["text"]="(3, 5)";

submit = tk.Button(window, text="submit", width=10, height=2, highlightbackground='lightgray', fg='black', activeforeground='darkgray')
submit.bind("<Button-1>", compute)
submit.pack(pady=(10,20))

output.pack()

window.mainloop();