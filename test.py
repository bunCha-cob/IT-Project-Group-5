from tkinter import *
import tkinter as tk

window = tk.Tk()

window.geometry('150x500')

label = tk.Label(text="Name") 
entry = tk.Entry()
label.grid(row=0,column=0,sticky=W)
entry.grid(row=0,column=1,sticky=W)
entry.insert(0, "Python")

label2 = tk.Label(text="Name2") 
entry2 = tk.Entry()
label2.grid(row=1,column=0,sticky=W)
entry2.grid(row=1,column=1,sticky=W)
entry2.insert(0, "Python2")

window.mainloop()