from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager


app = Flask(__name__, template_folder='/Users/laptop/PycharmProjects/untitled2/templates',
            static_folder='/Users/laptop/PycharmProjects/untitled2/static')
app.config['SQLALCHEMY_DATABASE_URI']= 'postgresql://localhost:5432/site'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db = SQLAlchemy(app)
login = LoginManager(app)
login.login_view = 'login'

from app import routes, models