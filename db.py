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
                name TEXT,  
                email TEXT,
                password TEXT);"""
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
    """
    This method inserts user into the db when user does a Google Oauth login
    """
    with sqlite3.connect(DB_FILE) as con:  
        cur = con.cursor()
        cur.execute("SELECT email FROM users WHERE email = ?", (email,))  
        row = cur.fetchone()
        if not row:
            cur.execute("INSERT into users (name, email) values (?,?)",(name,email))  
            con.commit() 


def insertOnRegistration(name,email,password):
    """
    This method inserts user into db when user registers.
    Returns True if user is already registered, False otherwise.
    """
    with sqlite3.connect(DB_FILE) as con:  
        cur = con.cursor()
        cur.execute("SELECT email FROM users WHERE email = ?", (email,))  
        row = cur.fetchone()
        if not row:
            cur.execute("INSERT into users (name, email,password) values (?,?,?)",(name,email,password))  
            con.commit() 
            return False
        return True




def get_posts(posts=10):
    with sqlite3.connect(DB_FILE) as con:
        cur = con.cursor()
        cur.execute("SELECT * FROM posts LIMIT ?", (posts,))
        return cur.fetchall()