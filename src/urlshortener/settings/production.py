from .base import *

import dj_database_url

SECRET_KEY = os.environ.get('SECRET_KEY')

DEBUG = False

ALLOWED_HOSTS = ['localhost', '127.0.0.1', '[::1]', '.herokuapp.com']

DATABASES = {}
db_from_env = dj_database_url.config(conn_max_age=600)
DATABASES['default'] = db_from_env
