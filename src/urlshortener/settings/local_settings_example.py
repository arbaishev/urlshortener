from .base import *

SECRET_KEY = 'Input Your Secret key here'

DEBUG = False

ALLOWED_HOSTS = ['localhost', '127.0.0.1', '[::1]']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'DB name',
        'USER': 'DB user',
        'PASSWORD': 'DB user password',
        'HOST': 'localhost',
        'PORT': '',
        'TEST': {
            'NAME': 'Test DB name',
        },
    }
}
