# from app.forms import LoginForm
from flask import render_template, Flask, redirect, url_for, flash, request
# from flask_login import current_user, login_user, logout_user, login_required
# from app.models import User
# from flask import request
# from werkzeug.urls import url_parse
# from app import db
# from app.forms import RegistrationForm
from app import app, db
import requests
from bs4 import BeautifulSoup
from app.models import User_1
import smtplib, os
from email.message import EmailMessage


MEDIUM_URL = 'https://medium.com/search?q=обучение'
SENDER_EMAIL = 'routinewriter@gmail.com'
SENDER_PASSWORD = os.environ.get('SENDER_PASSWORD')


@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")


@app.route('/success', methods = ['POST'])
def success():
    if (request.method == 'POST'):
        username_ = request.form["username"]
        email_ = request.form["email"]
        message_ = request.form["message"]

        msg = EmailMessage()
        msg.set_content('From {0} , email {1} , message {2} '.format(username_, email_, message_))
        msg['From'] = SENDER_EMAIL
        msg['To'] = email_
        msg['Subject'] = 'form data{}'.format(username_)

        smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
        smtpObj.starttls()
        my_email = os.environ.get('MY_EMAIL')
        my_email_password = os.environ.get('MY_EMAIL_PASSWORD')
        smtpObj.login(my_email, my_email_password)
        smtpObj.sendmail(my_email, "istudykg@gmail.com", msg.as_string())
        smtpObj.quit()

        data = User_1(username_, email_, message_)
        db.session.add(data)
        db.session.commit()
        firstarticle = h3article(MEDIUM_URL)
        h3nameslist = h3article(MEDIUM_URL)
        return render_template("articles.html", firstarticle=firstarticle, names=h3nameslist)


@app.route('/courses')
def courses():
    return render_template("courses.html")



@app.route('/programming')
def programming():
    return render_template("сourses/programming.html")


@app.route('/english')
def english():
    return render_template("сourses/english.html")


@app.route('/crewtivewriting')
def creativewriting():
    return render_template("сourses/creative_writing.html")

@app.route('/preschool')
def preschool():
    return render_template("сourses/preschool.html")


def h3article(url):
    source = requests.get(url)
    main_text = source.text
    soup = BeautifulSoup(main_text, 'html.parser')
    name = soup.find('h3')
    return name

def h3articles(url):
    source = requests.get(url)
    main_text = source.text
    soup = BeautifulSoup(main_text, 'html.parser')
    names = soup.find_all('h3')
    name_dict = []

    for name in names:
        name_dict.append(name.text)
    return name_dict


@app.route('/articles')
def articles():
    firstarticle = h3article(MEDIUM_URL)
    h3nameslist = h3article(MEDIUM_URL)
    return render_template("articles.html", firstarticle=firstarticle, names=h3nameslist)


# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     form = LoginForm()
#     if form.validate_on_submit():
#         user = User.query.filter_by(username=form.username.data).first()
#         if user is None or not user.check_password(form.password.data):
#             flash('Invalid username or password')
#             return redirect(url_for('login'))
#         login_user(user, remember=form.remember_me.data)
#         next_page = request.args.get('next')
#         if not next_page or url_parse(next_page).netloc != '':
#             next_page = url_for('index')
#         return redirect(next_page)
#     if current_user.is_authenticated:
#         return redirect(url_for('index'))
#     return render_template('login.html', title='Sign In', form=form)
#
#
# @app.route('/logout')
# def logout():
#     logout_user()
#     return redirect(url_for('login'))
#
#
# @app.route('/register', methods=['GET', 'POST'])
# def register():
#     if current_user.is_authenticated:
#         return redirect(url_for('index'))
#     form = RegistrationForm()
#     if form.validate_on_submit():
#         user = User(username=form.username.data, email=form.email.data)
#         user.set_password(form.password.data)
#         db.session.add(user)
#         db.session.commit()
#         flash('Congratulations, you are now a registered user!')
#         return redirect(url_for('login'))
#     return render_template('register.html', title='Register', form=form)