from flask import Flask,escape,request, render_template

app = Flask(__name__)

@app.route("/")
def loginPage():
    return render_template("login.html")

@app.route("/home")
def home():
    return "This is the Home page"

@app.route("/registration")
def registration():
    return render_template("registration.html")

app.run(host="0.0.0.0",port=8000,debug=True)


