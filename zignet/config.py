import os
basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'zignet.db')

SECRET_KEY = 'siesta-har-5-onkler'