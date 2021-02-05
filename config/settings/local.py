from .base import *

DEBUG = True

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

Database
https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ["LOCAL_DB_NAME"],
        'USER': os.environ["LOCAL_DB_USER"],
        'PASSWORD': os.environ["LOCAL_DB_PASSWORD"],
        'HOST': os.environ["LOCAL_DB_HOST"],
        'PORT': os.environ["LOCAL_DB_PORT"],
    }
}

SECRET_KEY = os.environ['DJANGO_SECRET_KEY']

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': os.environ["DB_NAME"],
#         'USER': os.environ["DB_USER"],
#         'PASSWORD': os.environ["DB_PASSWORD"],
#         'HOST': os.environ["DB_HOST"],
#         'PORT': os.environ["DB_PORT"],
#     }
# }