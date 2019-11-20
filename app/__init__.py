from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_script import Manager


app = Flask(__name__,
            # template_folder='/Users/laptop/PycharmProjects/untitled2/templates',
            # static_folder='/Users/laptop/PycharmProjects/untitled2/static'
            template_folder='/app/templates',
            static_folder='/app/static'
            )
app.config['SQLALCHEMY_DATABASE_URI']= 'postgres://yqcqbqkysnwyeh:f58a9fd562c92aee6888146df19218f63b2315ca37db27718d3c422bbdae8855@ec2-107-21-226-44.compute-1.amazonaws.com:5432/df55cgfitgbcpv'
    # 'postgresql://localhost:5432/site'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db = SQLAlchemy(app)
login = LoginManager(app)
login.login_view = 'login'
manager = Manager(app)


from app import routes, models

if __name__ == "__main__":
    manager.run()
