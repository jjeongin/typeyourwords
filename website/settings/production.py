from website.settings.base import *

# For production env
SECRET_KEY = os.environ.get('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True

ALLOWED_HOSTS = [
    'www.typeyourwords.com',
]

STATIC_URL = '/static/'

STATICFILES_DIRS = ( 
    os.path.join(BASE_DIR, 'static'),
)

STATIC_ROOT = os.path.join(BASE_DIR, 'typeyourwords/project0/static/') # pythonanywhere virtualenv

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'typeyourwords/project0/media/') # pythonanywhere virtualenv

IMAGEFIT_ROOT = os.path.join(BASE_DIR, 'typeyourwords/project0/') # pythonanywhere virtualenv