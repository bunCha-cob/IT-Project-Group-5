import Tkinter as tk
import time

def cust_ID:

def cust_location:

def cust_location:

def Draw():
    root = Tk()
    root.geometry("1010x1010")
    frame = Frame(root)
    frame.pack()
    
    label = Label(root,text = "Engagement of Customers")  
    label.pack()  

    listbox = Listbox(root, width=1000)  
    
    listbox.insert(1, cust_ID())  
    listbox.insert(2, cust_time())  
    listbox.insert(3, cust_location())  
    listbox.pack()
    root.mainloop()  
    
def Refresher():
    global text
    text.configure(text=time.asctime())
    root.after(1000, Refresher) # every second...

root=tk.Tk()
Draw()
Refresher()
root.mainloop()








