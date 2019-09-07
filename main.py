from flask import Flask,escape,request, render_template

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("index.html")

@app.route("/home")
def home():
    return "This is the Home page"

@app.route("/customer")
def customer():
    return "i love it"

app.run(host="0.0.0.0",port=8000,debug=True)


