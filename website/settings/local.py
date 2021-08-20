from website.settings.base import *
from website.settings import SECRET_KEY_LOCAL

# For local env
SECRET_KEY = SECRET_KEY_LOCAL

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

INSTALLED_APPS += [
    'livereload',
]

MIDDLEWARE += [
    'livereload.middleware.LiveReloadScript',
]

ALLOWED_HOSTS = [
    'localhost',
]