from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import (StringField, PasswordField, TextAreaField, IntegerField, BooleanField,
                     RadioField, SubmitField)
from wtforms.validators import DataRequired, Email, InputRequired, Length
from flask_bootstrap import Bootstrap


class LoginForm(FlaskForm):
    email = StringField(label="Email:", validators=[DataRequired(), Email()])
    password = PasswordField(label="Password:", validators=[DataRequired(), Length(min=8)])
    submit = SubmitField(label="Login")


app = Flask(__name__)
Bootstrap(app)
app.secret_key = 'flasksecretkey'


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login", methods=["GET", "POST"])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        if login_form.email.data == "admin@email.com" and login_form.password.data == "12345678":
            return render_template("success.html")
        else:
            return render_template("denied.html")
    return render_template("login.html", form=login_form)

@app.route("/quickform", methods=["GET", "POST"])
def quick_form():
    form = LoginForm()
    return render_template("quick_form.html", form=form)


if __name__ == '__main__':
    app.run(debug=True, port=5007)
