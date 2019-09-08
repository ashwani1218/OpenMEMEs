import sqlite3
DB_FILE = 'OpenMEMEs.db'

def createDB():
    """ This function creates the necessary tables in the db.
    UPDATE THIS WHEN YOU CREATE NEW TABLES
    TABLES: 
    users -> This table has all the registered users.
    posts -> This table contains all the posts posted by registered users. 
             Contains the foreign key of user.id.
    """
    DATABASE = sqlite3.connect(DB_FILE)
    cur=DATABASE.cursor()

    #USERS TABLE
    sql_command = """CREATE TABLE IF NOT EXISTS  users (  
                id INTEGER PRIMARY KEY,  
                name VARCHAR(20),  
                email VARCHAR(20),
                password VARCHAR(20));"""
    cur.execute(sql_command)

    #POSTS TABLE
    sql_command = """ CREATE TABLE IF NOT EXISTS posts (
        id INTEGER PRIMARY KEY,
        user_id INTEGER NOT NULL,
        post TEXT,
        post_image BLOB,
        post_video BLOB
    )
    """
    cur.execute(sql_command)

    DATABASE.commit()

def insertUser(name,email):
    with sqlite3.connect(DB_FILE) as con:  
        cur = con.cursor()
        cur.execute("SELECT email FROM users WHERE email = ?", (email,))  
        row = cur.fetchone()
        if not row:
            cur.execute("INSERT into users (name, email) values (?,?)",(name,email))  
            con.commit()  

def insertUserFromRegistration(name,email,password):
    with sqlite3.connect(DB_FILE) as con:  
        cur = con.cursor()
        cur.execute("SELECT email FROM users WHERE email = ?", (email,))  
        row = cur.fetchone()
        if not row:
            cur.execute("INSERT into users (name, email,password) values (?,?,?)",(name,email,password))  
            con.commit()

def get_posts(posts=10):
    with sqlite3.connect(DB_FILE) as con:
        cur = con.cursor()
        cur.execute("SELECT * FROM posts LIMIT ?", (posts,))
        return cur.fetchall()