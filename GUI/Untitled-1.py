from tkinter import * 

def getCustomer():
    x1 = e.get()
    label = Label(root, text= float(x1)**0.5)
    label.pack()
    
def retrieve():
    print(listbox.curselection())

def top_10():

def bottom_10():

def top_1():

def bottom_1():

def avg_time():

def top_area():

def bottom_area():

def areas_visited():

def medium_time():


root = Tk()
root.geometry("1000x1000")
frame = Frame(root)
frame.pack()
 
label = Label(root,text = "Big Data Anaylys: Engagement of Customers")  
label.pack()  

listbox = Listbox(root)  
   
# listbox.insert(1, top_10())  
# listbox.insert(2, bottom_10())  
# listbox.insert(3, top_1())  
# listbox.insert(4, bottom_1())
# listbox.insert(5, avg_time())
# listbox.insert(6, top_area())  
# listbox.insert(7, bottom_area())  
# listbox.insert(8, areas_visited())  
# listbox.insert(9, medium_time()) 
 

listbox.pack()

 
bttn1 = Button(frame, text = "Submit", command = retrieve)
bttn1.pack(side= "bottom")


e = Entry(root)
e.pack()

e.focus_set()

def callback():
    print(e.get())

b = Button(root, text = "Customer", width = 100, command = getCustomer)
b.pack()


root.mainloop()  

