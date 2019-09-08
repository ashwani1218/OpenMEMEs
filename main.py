from flask import Flask,escape,request,redirect,url_for,render_template, Response
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
        db.insertUser(name,email)
        return redirect(url_for('home'))

@app.route("/home")
def home():
    rows = db.get_posts(posts=20)
    return render_template("home.html", rows=rows)

@app.route("/registration")
def registration():
    return render_template("registration.html")

@app.errorhandler(401)
def custom_401(error):
    return Response('You tried to access something that shouldn\'t be accessed', 401, {'WWW-Authenticate':'Basic realm="Login Required"'})

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

app.run(host="0.0.0.0",port=8000,debug=True)


