# from werkzeug.security import generate_password_hash, check_password_hash
from app import login, db
# from datetime import datetime
from flask_login import UserMixin



class User_1(UserMixin, db.Model):
    __tablename__ = "user_1"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    message = db.Column(db.String(600))
    # password_hash = db.Column(db.String(128))
    # posts = db.relationship('Post', backref='author', lazy='dynamic')
    # extend_existing = True

    # def set_password(self, password):
    #     self.password_hash = generate_password_hash(password)
    #
    # def check_password(self, password):
    #     return check_password_hash(self.password_hash, password)

    def __init__(self, username, email, message):

        self.username = username
        self.email = email
        self.message = message

    def __repr__(self):
        return '<User {}>'.format(self.username)
#
#
# class Post(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     body = db.Column(db.String(140))
#     timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
#
#     def __repr__(self):
#         return '<Post {}>'.format(self.body)
#
#
# @login.user_loader
# def load_user(id):
#     return User.query.get(int(id))


# CREATE TABLE user_1 (
#     id serial PRIMARY KEY,
#     username            varchar(64),
#     email            varchar(120),
#     message            varchar(600)
# );