import os
basedir = os.path.abspath(os.path.dirname(__file__))
print('>> config : %s' % basedir)

'''
class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    ALLOWED_EXTENSIONS = ['LCF']
    UPLOADED_FILES_DEST = 'gdlconf/public/lttfiles/'
    MAX_CONTENT_SIZE = 10000
'''

SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
                          'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_TRACK_MODIFICATIONS = False
ALLOWED_EXTENSIONS = ['LCF']
UPLOADED_FILES_DEST = 'gdlconf/public/lttfiles/'
MAX_CONTENT_SIZE = 10000

