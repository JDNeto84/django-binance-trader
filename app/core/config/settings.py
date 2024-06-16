import os, ast
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

DEBUG = os.getenv('DJANGO_DEBUG', 'False').lower() in ['true', '1', 't']

SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY')

ALLOWED_HOSTS = ast.literal_eval(os.environ.get('DJANGO_ALLOWED_HOSTS', '[]')) 

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
 
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

ROOT_URLCONF = 'core.interface.urls'
LOGIN_REDIRECT_URL = '/'
DIR_TEMPLATES = os.path.join(BASE_DIR, 'interface/templates')
STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'interface/static/')]

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
