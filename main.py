from flask import Flask,escape,request,redirect
from flask import url_for,render_template, Response, session
import hashlib

import db


app = Flask(__name__)
"""
Creates a Database is already not present
"""
db.createDB()

@app.route("/",methods=['GET','POST'])
def loginPage():
    '''
    This Method returns login page on a GET Request and registers user into the database if 
    Google Oauth is used to login into the System
    '''
    if(request.method=='GET'):
        return render_template("login.html")
    else:
        name=request.form['name']
        email=request.form['email']
        db.insertUser(name,email)
        return "OK"

@app.route("/login",methods=['POST'])
def customLogin():
    '''
    This Method is the Custom Login implementation.
    The users email address is matched in the DataBase and passwords are matched.
    '''
    email=request.form["inputEmail"]
    password=request.form["inputPassword"]
    pwd=str(hashlib.sha256(password.encode()).digest())
    user=db.getUserByEmail(email)
    if(pwd==user):
        return redirect("/home") #If passwords match redirect to the home page
    return redirect("/")         #Else redirect back to the login page. Change this return method to alert invalid Credentials

    


@app.route("/home")
def home():
    '''
    This method is used to diplay the home page.
    '''
    rows = db.get_posts(posts=20)
    return render_template("home.html", rows=rows)

@app.route("/registration", methods=['GET','POST'])
def registration():
    if (request.method=='POST'):
        try:
            name = request.form["name"]
            email = request.form["email"]
            password = request.form["password"]
            pwd=str(hashlib.sha256(password.encode()).digest())
            print(pwd)
            already_registered = db.insertOnRegistration(name,email,pwd)
            if(already_registered):
                return render_template("AlreadyRegistered.html")
            return redirect("/")
        except Exception as e:
            print(e)
            return "something went Wrong!!!"
    else:
        return render_template("registration.html")

@app.errorhandler(401)
def custom_401(error):
    return Response('You tried to access something that shouldn\'t be accessed', 401, {'WWW-Authenticate':'Basic realm="Login Required"'})

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

app.run(host="0.0.0.0",port=8000,debug=True)


