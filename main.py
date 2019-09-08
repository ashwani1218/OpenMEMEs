from flask import Flask,escape,request,redirect,url_for, render_template
import db


app = Flask(__name__)
db.createDB()

@app.route("/",methods=['GET','POST'])
def loginPage():
    if(request.method=='GET'):
        return render_template("login.html")
    else:
        name=request.form['name']
        email=request.form['email']
        print(name,email,"bro")
        db.insertUser(name,email)
        return redirect(url_for('home'))

@app.route("/home")
def home():
    return "This is the Home page"

@app.route("/registration")
def registration():
    return render_template("registration.html")

app.run(host="0.0.0.0",port=8000,debug=True)


