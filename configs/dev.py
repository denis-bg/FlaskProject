import os
basedir = os.path.abspath(os.path.dirname(__file__))
print('>> configs/dev : %s' % basedir)

'''
SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
    'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_TRACK_MODIFICATIONS = False
ALLOWED_EXTENSIONS = ['LCF']
UPLOADED_FILES_DEST = 'app/public/lttfiles/'
MAX_CONTENT_SIZE = 30000
'''
CONFIG = "DEV"


