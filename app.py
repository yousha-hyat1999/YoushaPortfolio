from flask import Flask, render_template, request
import smtplib
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, PasswordField, BooleanField
from wtforms.fields.html5 import EmailField
from wtforms.validators import InputRequired, Email, Length
from flask_sqlalchemy import SQLAlchemy
import _sqlite3
import csv

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Thisissupposedtobesecret!'
bootstrap = Bootstrap(app)
subscribers = []
line_1 = ''


class LoginForm(FlaskForm):
    username = StringField('username', validators=[InputRequired(), Length(min=4, max=15)])
    password = PasswordField('password', validators=[InputRequired(), Length(min=4, max=20)])


@app.route("/Base")
def base():
     return render_template("Base.html")


@app.route("/", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return render_template("login.html", form=form)
    return render_template("login.html", form=form)


@app.route("/games")
def games():
    return render_template("games.html")


@app.route("/sports")
def sports():
    return render_template("sports.html")


@app.route("/Home")
def home():
    return render_template("Home.html")


@app.route("/AboutMe")
def about():
    return render_template("AboutMe.html")


@app.route("/Portfolio")
def portfolio():
    return render_template("Portfolio.html")


@app.route("/Hobbies")
def hobbies():
    return render_template("Hobbies.html")


@app.route("/tv")
def tv():
    return render_template("tv.html")


@app.route('/subscribe')
def subscribe():
    return render_template("subscribe.html")


@app.route('/thanks', methods=["POST"])
def thanks():
    first_name = request.form.get("first_name")
    last_name = request.form.get("last_name")
    email = request.form.get("email")

    message = "You have been suscribe to my email newsLetter"
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login("yousha.soen287@gmail.com", "Hyatoolla23")
    server.sendmail("yousha.soen287@gmail.com", email, message)

    if not first_name or not last_name or not email:
        error_statement = "All Form Fields Required..."
        return render_template("subscribe.html",
                               error_statement=error_statement,
                               first_name=first_name,
                               last_name=last_name, email=email)

    subscribers.append(f" {first_name} {last_name} || {email}")
    with open('/Users/yoush/PycharmProjects/untitled1/templates/family.csv', 'w', newline='') as f:
        thewriter = csv.writer(f)
        thewriter.writerow(subscribers)

    message = "You have been suscribe to my email newsLetter"
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login("yousha.soen287@gmail.com", "Hyatoolla23")
    server.sendmail("yousha.soen287@gmail.com", email, message)
    title = "Thank You!"

    return render_template("thanks.html", subscribers=subscribers)


@app.route('/table')
def table():
    csv_file = open('/Users/yoush/PycharmProjects/untitled1/templates/family.csv', 'r')
    line_1 = csv_file.readline()
    return render_template('table.html', line_1=line_1)


if __name__ == '__main__':
    app.run()
