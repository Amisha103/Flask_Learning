from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")
# def student_profile():
#     return render_template("profile.html", name = "amisha", is_topper = True, subjects = ["DSA", "DBMS", "Networking"])

