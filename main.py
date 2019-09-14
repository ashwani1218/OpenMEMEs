from flask import *
import hashlib

import db

app = Flask(__name__)
app.config['SECRET_KEY'] = '30ea67d46f46a8ca1e9a9d82'
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
        session['email']=email
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
    user=db.getPasswordByEmail(email)
    if(pwd==user):
        session['email']=email
        return redirect("/home") #If passwords match redirect to the home page
    return redirect("/")         #Else redirect back to the login page. Change this return method to alert invalid Credentials

@app.route("/logout")
def logout():
    print("Session",session)
    if "email" in session:
        session.pop("email")
    return "OK"

@app.route("/home")
def home():
    '''
    This method is used to diplay the home page.
    '''
    rows = db.get_posts(posts=20)
    return render_template("home.html", rows=rows)

@app.route("/registration", methods=['GET','POST'])
def registration():
    '''
    This method registers user into db and hashes the password for security.
    If the user is already registered then user is redirected to AlreadyRegistered page
    and then redirected to the login page after 5 seconds.
    '''

    if (request.method=='POST'):
        try:
            name = request.form["name"]
            email = request.form["email"]
            password = request.form["password"]
            pwd=str(hashlib.sha256(password.encode()).digest())
            already_registered = db.insertOnRegistration(name,email,pwd)
            if(already_registered):
                return render_template("AlreadyRegistered.html")
            return redirect("/")
        except Exception as e:
            print(e)
            return render_template("error.html")
    else:
        return render_template("registration.html")

@app.route("/userProfile")
def userProfile():
    try:
        if 'email' in session:
            email=session['email']
            # name=db.getNameByEmail(email)
            user=db.getUserByEmail(email)
            print(user)
            return render_template("userProfile.html", user=user)
        else:
            return redirect("/")
    except Exception as e:
        print(e)



@app.route("/newpost",methods=["GET","POST"])
def newPost():
    '''
    This method on a GET request returns new post page to update a post.
    On a POST request the method checks if the user is in session then gets the userId,
    postText from the form and enters it into db.
    If the post is successfully inserted into the db user is redirected to the home page else
    redirected to a error page and then to the home page.
    '''
    if(request.method=="GET"):
        if 'email' in session:  
            return render_template("newPost.html")
        else:
            return redirect("/")
    elif(request.method=="POST"):
        # try:
        if 'email' in session:  
            email=session['email'] 
            print(email)
            userId=db.getIdByEmail(email)
            postText=request.form["postText"]
            post = db.new_post(userId,postText)
            if(post):
                return redirect("/home")
            return render_template("error.html")
        else:
            return redirect("/")
        # except Exception as e:
        #     print(e)
            # redirect("/")

            
@app.errorhandler(401)
def custom_401(error):
    return Response('You tried to access something that shouldn\'t be accessed', 401, {'WWW-Authenticate':'Basic realm="Login Required"'})

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

# app.run(host="0.0.0.0",port=8000,debug=True)


