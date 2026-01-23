from flask import Flask, render_template, request, redirect, url_for, flash
from forms import RegistrationForm


app = Flask(__name__)
app.secret_key = "my_secret_key"

@app.route("/", methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        flash(f"Welcome, {name}!You registered successfully")
        return redirect(url_for("success"))
    return render_template("register.html", form=form)\
    
@app.route("/success")
def success():
    return render_template("success.html")








# @app.route("/", methods=["GET", "POST"])
# def form():
#     if request.method == "POST":
#         name = request.form.get("name")
#         if not name:
#             flash("Name can not be empty")
#             return redirect(url_for("form"))
#         flash(f"Thanks {name}, your feedback was saved")
#         return redirect(url_for("thankyou"))
#     return render_template("form.html")

# @app.route("/thankyou")
# def thankyou():
#     return render_template("thankyou.html")
    
# @app.route("/feedback", methods = ["POST", "GET"])
# def feedback():
#     if request.method == "POST":
#         name = request.form.get("username")
#         message = request.form.get("message")

#         return render_template("thankyou.html", user = name, message = message)
#     return render_template("feedback.html")