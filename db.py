import sqlite3
from flask import g

DATABASE = sqlite3.connect('OpenMEMEs.db')

# def get_db():
#     db = getattr(g, '_database', None)
#     if db is None:
#         db = g._database = DATABASE
#     return db

cur=DATABASE.cursor()

sql_command = """CREATE TABLE users (  
            id INTEGER PRIMARY KEY,  
            first_name VARCHAR(20),  
            last_name VARCHAR(30),  
            gender CHAR(1),  
            email VARCHAR(20)
            phone_no INTEGER(10));"""
            
