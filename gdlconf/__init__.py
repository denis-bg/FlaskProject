import os

from flask import Flask
from flask_fontawesome import FontAwesome
from flask_bootstrap import Bootstrap
from flask_uploads import UploadSet, configure_uploads
from flask_wtf import FlaskForm

# from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate
# from flask_login import LoginManager
# from flask_moment import Moment

# from config import Config

app = Flask(__name__, instance_relative_config=True)

app.config.from_object('config')
print(app.config['MAX_CONTENT_SIZE'])
# app.config.from_pyfile('config.py')
# print(app.config['MAX_CONTENT_SIZE'])

if os.environ.get('ENV') == 'DEV':
    app.config.from_object('configs.dev')
else:
    app.config.from_object('configs.prod')

print(app.config['CONFIG'])

# fa = FontAwesome(app)
bs = Bootstrap(app)
fa = FontAwesome(app)

fichiers = UploadSet('files', ('LCF', 'lcf'))
configure_uploads(app, fichiers)

print(app.instance_path)
lttdir = app.root_path + '/public/lttfiles/'
print(lttdir)
from gdlconf import routes
