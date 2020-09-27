from tkinter import * 

import sqlite3

from sqlite3 import Error


db_file = r"C:\Users\Jessica Reid\Downloads\trackingdb.db"



#Change to sql database later 
def create_connection(db_file):
    """create a connection to a sqlite database"""

    conn = None

    try:
        conn = sqlite3.connect(db_file)

        print(sqlite3.version)

        return conn

    except Error as e:

        print(e)
    
    return conn



def create_table(conn, create_table_sql):
    try:

        c = conn.cursor()

        c.execute(create_table_sql)

    except Error as e:
        print(e)



def insert_data(conn):
    return "x"



def getCustomer():
    x1 = e.get()

    x2 = """SELECT all_areas_visited FROM total_areas WHERE customerID ="""+x1+""";"""

    label = Label(root, text= x2)
    label.pack()
    



def retrieve():
    print("No new data")




def table_checker(cur):

    engage_exists = """SELECT name FROM sqlite_master WHERE type='table' AND name='engaged';"""

    total_areas_exists = """SELECT name FROM sqlite_master WHERE type='table' AND name='total_areas';"""

    primary_table_exists = """SELECT name FROM sqlite_master WHERE type='table' AND name='primary_table';"""
    



    e = cur.execute(engage_exists)

    t = cur.execute(total_areas_exists)

    p = cur.execute(primary_table_exists)



    if e == 0:

        return True

    elif t == 0:

        return True

    elif p == 0:

        return True

    else:

        return False




def top_10():
    conn = create_connection(db_file)
    cur = conn.cursor()

    #checks if tables/data exists
    #if no populate with dummy data
    check = table_checker(cur)

    if check:
        insert_data(cur)


    select_top_10 = """SELECT engagement_time FROM engaged ORDER BY engagement_time DESC LIMIT 10;"""

    i = cur.execute(select_top_10)
    
    j = "top 10 customers times: "+i

    return j


def bottom_10():
    conn = create_connection(db_file)
    cur = conn.cursor()

    #checks if tables/data exists
    #if no populate with dummy data
    check = table_checker(cur)

    if check:
        insert_data(cur)


    select_bottom_10 = """SELECT engagement_time FROM engaged ORDER BY engagement_time ASC LIMIT 10;"""

    i = cur.execute(select_bottom_10)
    return "bottom 10 customers times: " + i

def top_1():
    conn = create_connection(db_file)
    cur = conn.cursor()

    #checks if tables/data exists
    #if no populate with dummy data
    check = table_checker(cur)

    if check:
        insert_data(cur)


    select_top_1 = """SELECT MAX(engagement_time);"""

    i = cur.execute(select_top_1)
    return "top customer time: " + i

def bottom_1():
    conn = create_connection(db_file)
    cur = conn.cursor()

    #checks if tables/data exists
    #if no populate with dummy data
    check = table_checker(cur)

    if check:
        insert_data(cur)


    select_bottom_1 = """SELECT MIN(engagement_time);"""

    i = cur.execute(select_bottom_1)
    return "bottom customer time: " + i

def avg_time():
    conn = create_connection(db_file)
    cur = conn.cursor()

    #checks if tables/data exists
    #if no populate with dummy data
    check = table_checker(cur)

    if check:
        insert_data(cur)


    select_avg_time = """SELECT AVG(engagement_time) FROM engaged;"""

    i = cur.execute(select_avg_time)
    return "average time: " + i


### Works with 4 area space rather than categorical area space

# def top_area():
#         conn = create_connection(db_file)
#     cur = conn.cursor()

#     #checks if tables/data exists
#     #if no populate with dummy data
#     check = table_checker(cur)

#     if check:
#         insert_data(cur)

#     statement1 = """"SELECT DISTINCT all_areas_visited FROM  total_areas;""""
#     statement2 = """SELECT COUNT("""+areas+""") FROM total_areas WHERE all_areas_visited="""+areas+""";"""
    
#     distinct_areas = curr.execute(statement1)
#     for areas in distinct_areas:
# 	    area_count = curr.execute(statement2)
#     select_top_area = max(area_count)

#     i = select_top_area

#     return "top area: " + i 

# def bottom_area():
#         conn = create_connection(db_file)
#     cur = conn.cursor()

#     #checks if tables/data exists
#     #if no populate with dummy data
#     check = table_checker(cur)

#     if check:
#         insert_data(cur)

#     statement1 = """"SELECT DISTINCT all_areas_visited FROM  total_areas;""""
#     statement2 = """SELECT COUNT("""+areas+""") FROM total_areas WHERE all_areas_visited="""+areas+""";"""
    
#     distinct_areas = curr.execute(statement1)
#     for areas in distinct_areas:
# 	    area_count = curr.execute(statement2)
#     select_bottom_area = min(area_count)

#     i = select_bottom_area
    
#     return "bottom area: " + i

def areas_visited():
    conn = create_connection(db_file)
    cur = conn.cursor()

    #checks if tables/data exists
    #if no populate with dummy data
    check = table_checker(cur)

    if check:
        insert_data(cur)

    distinct_areas = """"SELECT DISTINCT all_areas_visited FROM  total_areas;""""
    
    i = cur.execute(distinct_areas)
    return "areas visited: " + i

def medium_time():
    conn = create_connection(db_file)
    cur = conn.cursor()

    #checks if tables/data exists
    #if no populate with dummy data
    check = table_checker(cur)

    if check:
        insert_data(cur)

    SELECT engagement_time FROM 
    
    medium = ("""(SELECT a1.trackID, a1.engagement_time, COUNT(a1.engagement_time) Rank
        FROM  engaged a1, engaged a2
        WHERE a1.engagement_time < a2.engagement_time OR (a1.engagement_time=a2.engagement_time AND a1.trackID <= a2.trackID)
        group by a1.trackID, a1.engagement_time
        order by a1.engagement_time desc) a3
        WHERE Rank = (SELECT (COUNT(*)+1) DIV 2 FROM engaged);""")
    
    i = curr.excute(medimu)

    return "medium time: " + i 







root = Tk()
root.geometry("1010x1010")
frame = Frame(root)
frame.pack()
 


label = Label(root,text = "Big Data Anaylys: Engagement of Customers")  
label.pack()  

listbox = Listbox(root, width=1000)  
   



listbox.insert(1, top_10())  

listbox.insert(2, bottom_10())  

listbox.insert(3, top_1())  

listbox.insert(4, bottom_1())

listbox.insert(5, avg_time())

listbox.insert(6, top_area())  

listbox.insert(7, bottom_area()) 
 
listbox.insert(8, areas_visited())  

listbox.insert(9, medium_time()) 
 

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

