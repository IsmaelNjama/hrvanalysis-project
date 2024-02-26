"""
Production Settings for Heroku
"""

import environ

from hrvscihub.settings.base import *


env = environ.Env(
    # set casting, default value
    SECRET_KEY=(str, 'django-insecure-se2z18-w4%9kc(%y-r8*ghu=nrt$_odm@@%wkd69@i&hx*4paz'),
    EMAIL_HOST=(str, 'smtp-relay.sendinblue.com'),
    EMAIL_PORT=(str, '587'),
    EMAIL_HOST_USER=(str, 'ifeelhrv@gmail.com'),
    EMAIL_HOST_PASSWORD=(str, 'CSpWNK4vcbyIBA8G'),
    CELERY_BROKER_URL = (str, '127.0.0.1'),
)

# Raises django's ImproperlyConfigured exception if SECRET_KEY not in os.environ
SECRET_KEY = env('SECRET_KEY')

# Cloudinary stuff
CLOUDINARY_STORAGE = None

DEFAULT_FILE_STORAGE = 'django.core.files.storage.FileSystemStorage'

EMAIL_HOST = env('EMAIL_HOST')
EMAIL_PORT = env('EMAIL_PORT')
EMAIL_HOST_USER = env('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD =  env('EMAIL_HOST_PASSWORD')


CELERY_BROKER_URL =  env('CELERY_BROKER_URL')