import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DEBUG = os.getenv('DJANGO_DEBUG', 'False').lower() in ['true', '1', 't']
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY')
# ALLOWED_HOSTS = os.getenv('DJANGO_ALLOWED_HOSTS', '').split(',') // Disabled to not initially use an EBS in AWS
ALLOWED_HOSTS = ['*']
ROOT_URLCONF = 'core.interface.urls'
AUTH_USER_MODEL = 'core.CustomUser'
LOGIN_REDIRECT_URL = '/profile/'
LOGIN_URL = '/login/'
STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
DIR_TEMPLATES = os.path.join(BASE_DIR, 'templates')

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'core',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [DIR_TEMPLATES],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                
            ],
        },
    },
]

WSGI_APPLICATION = 'core.config.wsgi.application'

DB_ENGINE = os.getenv('DJANGO_DB_ENGINE')
DB_USER = os.getenv('MYSQL_DB_USER')
DB_PASS = os.getenv('MYSQL_DB_PASS')
DB_HOST = os.getenv('MYSQL_DB_HOST')
DB_PORT = os.getenv('MYSQL_DB_PORT')
DB_NAME = os.getenv('MYSQL_DB_NAME')

if DB_ENGINE == 'mysql' and all([DB_USER, DB_PASS, DB_HOST, DB_PORT, DB_NAME]):
    DATABASES = {
        'default': {
            'ENGINE': f'django.db.backends.{DB_ENGINE}',
            'NAME': DB_NAME,
            'USER': DB_USER,
            'PASSWORD': DB_PASS,
            'HOST': DB_HOST,
            'PORT': DB_PORT,
        },
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True
USE_TZ = True

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

DJANGO_SECURITY_PASSWORD_FAILURE_LIMIT = 5
DJANGO_SECURITY_PASSWORD_FAILURE_TIMEOUT = 900  
DJANGO_SECURITY_REPLAY_PROTECTION_ENABLED = True
DJANGO_SECURITY_SESSION_EXPIRATION = 1800  
DJANGO_SECURITY_SESSION_AGE = 86400  

