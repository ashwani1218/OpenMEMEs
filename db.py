import sqlite3
from flask import g

def createDB():
    DATABASE = sqlite3.connect('OpenMEMEs.db')
    cur=DATABASE.cursor()
    sql_command = """CREATE TABLE IF NOT EXISTS  users (  
                id INTEGER PRIMARY KEY,  
                name VARCHAR(20),  
                email VARCHAR(20),
                password VARCHAR(20));"""
    cur.execute(sql_command)
    
    
    
    DATABASE.commit()

def insertUser(name,email):
    with sqlite3.connect("OpenMEMEs.db") as con:  
        cur = con.cursor()
        cur.execute("SELECT email FROM users WHERE email = ?", (email,))  
        row = cur.fetchone()
        if not row:
            cur.execute("INSERT into users (name, email) values (?,?)",(name,email))  
            con.commit()  

