from tkinter import * 

import sqlite3

from sqlite3 import Error

# Module Imports
import mariadb
import sys

db_file = r"C:\Users\Jessica Reid\Desktop\helllooooob.db"


## uncomment and comment out other def create_connection(db_file)

# def create_connection(db_file)
#     # Connect to MariaDB Platform
#     try:
#         conn = mariadb.connect(
#             user="root",
#             password="root",
#             host="127.0.0.1",
#             port=3306,
#             #database=""

#         )
#     except mariadb.Error as e:
#         print(f"Error connecting to MariaDB Platform: {e}")
#         sys.exit(1)


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



def insert_data():

    conn = create_connection(db_file)
    cur = conn.cursor()
    print("hhhhhhhhhhhhhh")
    s = """SELECT name FROM sqlite_master WHERE type='table';"""
    cur.execute(s)
    i = cur.fetchall()
    print(i)
    print("ddddddddddddd")

    #Only creates tables if they dont already exist
    sql_create_engaged = """ CREATE TABLE engaged(trackID integer PRIMARY KEY NOT NULL, engagement_time double(6,3));"""
    sql_create_primary_table = """ CREATE TABLE primary_table(trackID integer PRIMARY KEY NOT NULL, customerID  integer, area mediumtext);"""
    sql_create_total_areas = """ CREATE TABLE total_areas(customerID integer PRIMARY KEY NOT NULL, all_areas_visited mediumtext);"""

    cur.execute(sql_create_engaged)
    cur.execute(sql_create_primary_table)
    cur.execute(sql_create_total_areas)

    sql_insert_engaged = """INSERT INTO engaged(trackID, engagement_time)
        VALUES
        (
            0,
            0.324
        ),
        (
            1,
            6.803
        ),
        (
            2,
            1.654
        ),
        (
            3,
            12.123
        ),
        (
            4,
            3.122
        ),
        (
            5,
            12.213
        ),
        (
            6,
            0.123
        ),
        (
            7,
            3.322
        ),
        (
            8,
            2.423
        ),
        (
            9,
            123.243
        ),
        (
            10,
            234.234
        ),
        (
            11,
            849.243
        ),
        (
            12,
            32.123
        ),
        (
            13,
            0.234
        ),
        (
            14,
            123.42
        ),
        (
            15,
            2.323
        ),
        (
            16,
            4.567
        ),
        (
            17,
            8.421
        ),
        (
            18,
            7.333
        ),
        (
            19,
            3.527
        ),
        (
            20,
            4.441
        )
        """
    sql_insert_primary_table = """INSERT INTO primary_table(trackID, customerID, area)
         VALUES
        (
            0,
            1,
            '7, 5'

        ),
        (
            1,
            1,
            '7, 6'
        ),
        (
            2, 
            3,
            '7, 7'
        ),
        (
            3,
            3,
            '7, 8'
        ),
        (
            4,
            2,
            '6, 7'
        ),
        (
            5,
            1,
            '6, 8'
        ),
        (
            6,
            3,
            '6, 9'
        ),
        (
            7,  
            4,
            '4, 5'
        ),
        (
            8,
            1,
            '4, 3'
        ),
        (
            9,
            2,
            '2, 3'
        ),
        (
            10,
            3,
            '2, 2'
        ),
        (
            11,
            4,
            '8, 9'
        ),
        (
            12,
            2,
            '7, 3'
        ),
        (
            13,
            1,
            '3, 4'
        ),
        (
            14,
            2,
            '3, 5'
        ),
        (
            15,
            3,
            '9, 2'
        ),
        (
            16,
            4,
            '3, 4'
        ),
        (
            17,
            2,
            '8, 9'
        ),
        (
            18,
            4,
            '2, 3'
        ),
        (
            19,
            3,
            '8, 3'
        ),
        (
            20,
            2,
            '2, 5'
        )
        """
    sql_insert_total_areas =  """INSERT INTO total_areas(customerID, all_areas_visited)
        VALUES
        (
            1,
            '[7, 5] , [7, 6] , [6, 8] , [4, 3] , [3, 4] ,'
        ),
        (
            2,
            '[6, 7] , [2, 3] , [7, 3] , [3, 5] , [8, 9] , [2, 5] ,'
        ),
        (
            3,
            '[7, 7] , [7, 8] , [6, 9] , [2, 2] , [9, 2] , [8, 3] ,'
        ),
        (
            4,
            '[4, 5] , [8, 9] , [3, 4] , [2, 3] , '
        )
        """

    cur.execute(sql_insert_engaged)
    cur.execute(sql_insert_primary_table)
    cur.execute(sql_insert_total_areas)

    d = """SELECT * FROM engaged;"""
    cur.execute(d)
    i = cur.fetchall()
    print(i)
    print("dfffffffffffffffffffffffffffff")

    return ""



def getCustomer():
    x1 = e.get()

    conn = create_connection(db_file)
    cur = conn.cursor()

    #checks if tables/data exists
    #if no populate with dummy data
    check = table_checker(cur)
    
    if check:
        insert_data()

    x2 = """SELECT all_areas_visited FROM total_areas WHERE customerID ="""+x1+""";"""
    
    cur.execute(x2)
    customer_info =  cur.fetchall() 

    label = Label(root, text= customer_info)
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
 
    if e == 1:

        return False

    elif t == 1:

        return False

    elif p == 1:

        return False

    else:

        return True




def top_10():
    conn = create_connection(db_file)
    cur = conn.cursor()

    #checks if tables/data exists
    #if no populate with dummy data
    check = table_checker(cur)

    if check == True:
        insert_data()


    select_top_10 = """SELECT engagement_time FROM engaged ORDER BY engagement_time DESC LIMIT 10;"""

    cur.execute(select_top_10)
    i = cur.fetchall() 
    j = "top 10 customers times: "+str(i)

    return j


def bottom_10():
    conn = create_connection(db_file)
    cur = conn.cursor()

    #checks if tables/data exists
    #if no populate with dummy data
    check = table_checker(cur)

    if check:
        insert_data()


    select_bottom_10 = """SELECT engagement_time FROM engaged ORDER BY engagement_time ASC LIMIT 10;"""

    cur.execute(select_bottom_10)
    i = cur.fetchall() 
    return "bottom 10 customers times: " +str(i)

def top_1():
    conn = create_connection(db_file)
    cur = conn.cursor()

    #checks if tables/data exists
    #if no populate with dummy data
    check = table_checker(cur)

    if check:
        insert_data()


    select_top_1 = """SELECT MAX(engagement_time) FROM engaged;"""

    cur.execute(select_top_1)
    i = cur.fetchall() 
    return "top customer time: " +str(i)

def bottom_1():
    conn = create_connection(db_file)
    cur = conn.cursor()

    #checks if tables/data exists
    #if no populate with dummy data
    check = table_checker(cur)

    if check:
        insert_data()


    select_bottom_1 = """SELECT MIN(engagement_time) FROM engaged;"""

    cur.execute(select_bottom_1)
    i = cur.fetchall() 
    return "bottom customer time: " +str(i)

def avg_time():
    conn = create_connection(db_file)
    cur = conn.cursor()

    #checks if tables/data exists
    #if no populate with dummy data
    check = table_checker(cur)

    if check:
        insert_data()


    select_avg_time = """SELECT AVG(engagement_time) FROM engaged;"""

    cur.execute(select_avg_time)
    i = cur.fetchall() 
    return "average time: " + str(i)


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

#     return "top area: "+str(i)

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
    
#     return "bottom area: " +str(i)

def areas_visited():
    conn = create_connection(db_file)
    cur = conn.cursor()

    #checks if tables/data exists
    #if no populate with dummy data
    check = table_checker(cur)

    if check:
        insert_data()

    distinct_areas = """SELECT all_areas_visited FROM total_areas;"""

    cur.execute(distinct_areas)
    i = cur.fetchall()
    return "areas visited: " +str(i)

def medium_time():
    conn = create_connection(db_file)
    cur = conn.cursor()

    #checks if tables/data exists
    #if no populate with dummy data
    check = table_checker(cur)

    if check:
        insert_data()

    
    medium="""SELECT AVG(engagement_time) FROM engaged;"""
    # medium = """SELECT engagement_time FROM 
    #     (SELECT a1.trackID, a1.engagement_time, COUNT(a1.engagement_time) Rank
    #     FROM  engaged a1, engaged a2
    #     WHERE a1.engagement_time < a2.engagement_time OR (a1.engagement_time=a2.engagement_time AND a1.trackID <= a2.trackID)
    #     group by a1.trackID, a1.engagement_time
    #     order by a1.engagement_time desc) a3
    #     WHERE Rank = (SELECT (COUNT(*)+1) DIV 2 FROM engaged);""")
    # medium = """SELECT AVG(engagement_time) FROM (SELECT engagement_time FROM engaged ORDER BY x LIMIT 2 - (SELECT COUNT(*) FROM engaged) % 2    -- odd 1, even 2 OFFSET (SELECT (COUNT(*) - 1) / 2 FROM engaged));"""
    cur.execute(medium)
    i = cur.fetchall()

    return "medium time: " +str(i)







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
 
listbox.insert(6, areas_visited())  

listbox.insert(7, medium_time()) 

# listbox.insert(8, top_area())  

# listbox.insert(9, bottom_area()) 
 

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

