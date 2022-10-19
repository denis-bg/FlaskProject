from flask import Flask
from flask_fontawesome import FontAwesome
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
# from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate
# from flask_login import LoginManager
# from flask_moment import Moment

from config import Config

app = Flask(__name__)

app.config.from_object(Config)

fa = FontAwesome(app)
bs = Bootstrap(app)

'''
db = SQLAlchemy(app)
migrate = Migrate(app, db)

login = LoginManager(app)
login.login_view = 'login'

bootstrap = Bootstrap(app)
moment = Moment(app)
'''

from app import routes
