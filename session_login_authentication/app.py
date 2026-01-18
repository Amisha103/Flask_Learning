from flask import Flask, request, redirect, url_for, session, Response
#this line is telling please create a website for us
app = Flask(__name__)#created an object of name app __name__ it tell the file that this is the main file
app.secret_key = "supersecret"
#route decorator tells that whenever someone visis the home page you have to run the below code
#homepage login page
@app.route("/", methods = ['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get("username")
        password = request.form.get("password")

        if username == "admin" and password == "123":
            session["user"] = username #store in session
            return redirect(url_for("welcome"))
        else:
            return Response("In-valid credentials. Try again", mimetype="text/plain")#mimetype means what kind of response you are going to send wither plain text or an html by default it is html'text/HTML'
    return'''
<h2>LOGIN PAGE</h2>
<form method="POST">
Username:<input type="text" name="username"><br>
Password:<input type= "text" name ="password"><br>
<input type = "submit" value="Login">
</form>

'''   

#welcome page(after login)
@app.route("/welcome")
def welcome():
    if "user" in session:
        return f'''
<h2> Welcome, {session["user"]} !</h2>
<a href={url_for('logout')}>Logout</a>
'''
    return redirect(url_for('login'))

#logout route
@app.route("/logout")
def logout():
    session.pop("user", None)#if user is not in the session than none will prevent us from any error
    return redirect(url_for("login"))


