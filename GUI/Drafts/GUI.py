import sqlite3
from sqlite3 import Error


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




if __name__ == "__main__":

    database = r"C:\Users\Jessica Reid\Downloads\trackingdb.db"
    # print("dHELLLLLLLLLLLLO")
    conn = create_connection(database)

    #Only creates tables if they dont already exist
    sql_create_engaged = """ CREATE TABLE IF NOT EXISTS engaged(trackID integer PRIMARY KEY NOT NULL, engagement_time double(6,3));"""
    sql_create_primary_table = """ CREATE TABLE IF NOT EXISTS primary_table(trackID integer PRIMARY KEY NOT NULL, customerID  integer, area mediumtext);"""
    sql_create_total_areas = """ CREATE TABLE IF NOT EXISTS total_areas(customerID integer PRIMARY KEY NOT NULL, all_areas_visited mediumtext);"""

    # print("D")

    # #dummy data 
    # #replace by calling tracker project and put in database
    # sql_insert_engaged_cust1 = """INSERT INTO engaged(1, 21.12)"""
    # sql_insert_primary_table_cust1 = """INSERT INTO primary_table()"""
    # sql_insert_total_areas_cust1 =  """INSERT INTO total_areas()"""


    if conn is not None:
        # print("Ds")
        create_table(conn, sql_create_engaged)
        # create_table(conn, sql_create_primary_table)
        # create_table(conn, sql_create_total_areas)

        cur = conn.cursor()
        stat = """SELECT name FROM sqlite_master WHERE type='table' ORDER BY name;"""
        cur.execute(stat)
        available_table=(cur.fetchall())
        print(available_table)
        # cur.execute(sql_insert_engaged_cust1)
        # cur.execute(sql_insert_primary_table_cust1)
        # cur.execute(sql_insert_total_areas_cust1)
        # cur.execute(sql_insert_engaged_cust2)
        # cur.execute(sql_insert_primary_table_cust2)
        # cur.execute(sql_insert_total_areas_cust2)

        print(top_10)
        print(bottom_10)
        print(top_1)
        print(bottom_1)
        print(average)
        print(total_areas)
        print(area_visited)
        print(area_most)
    
    else:
        print("Error! cannot connect to database")