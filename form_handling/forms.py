from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length

class RegistrationForm(FlaskForm):
    name = StringField("Full Name", validators=[DataRequired(message="We need your name, it can not be empty")])
    email =  StringField("Email", validators=[DataRequired(message = "Email message is required"), Email(message="That doesn't look like a valid email")])
    password = PasswordField("Password", validators=[DataRequired(message="Password is required"), Length(min=6, message="Password must be of 6 character long")])
    submit = SubmitField("Register")


