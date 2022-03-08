#library to connect to postgresql
import psycopg2
import os
from dotenv import load_dotenv
load_dotenv()

try :
    conn = psycopg2.connect(
        host="localhost",
        user=os.environ.get('db_user'),
        password=os.environ.get('db_password'),
    
    )
except Exception:
    print('Database not connected ', type(Exception))
else:
    print("Database connected")
    conn.autocommit = True
    
    cur = conn.cursor()
    #listing all the database that already exist
    cur.execute("SELECT datname FROM pg_Database;")
    list_database = cur.fetchall()
    #checking if the database that we want to create already exists
    if ("barona",) in list_database:
        print("barona database already exists")
    else:
        sql = '''CREATE database barona'''
        cur.execute(sql)
        print("successfully created")
finally:
    conn.close()

#creating schema
try:
    conn = psycopg2.connect(
        host="localhost",
        dbname="barona",
        user=os.environ.get('db_user'),
        password=os.environ.get('db_password'),
    
    )
except Exception as e:
    print("Database not connected")
else:
    print("Database connected")
    cur=conn.cursor()
    cur.execute("DROP TABLE IF EXISTS CONTACTS")
    sql = ''' CREATE TABLE CONTACTS(
        index INTEGER PRIMARY KEY,
        name VARCHAR(50),
        phone VARCHAR(25),
        email VARCHAR(75),
        id VARCHAR(20),
        country VARCHAR(50) )'''
    try:
        cur.execute(sql)
    except Exception:
        print("please check sql query")
    else:
        conn.commit()
        print("table created")
finally:
    conn.close()