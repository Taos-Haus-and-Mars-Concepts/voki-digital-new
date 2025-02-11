from pathlib import Path
from dotenv import load_dotenv
import os
import sys
import dj_database_url
from django.contrib.messages import constants as messages


ENVIRONMENT = str(os.getenv('ENVIRONMENT', 'development'))

if ENVIRONMENT in ['development', 'staging']:
    from dotenv import load_dotenv
    dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
    load_dotenv(dotenv_path)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = str(os.getenv('APP_SECRET_KEY'))

DEBUG = True

# DJANGO_ALLOWED_HOSTS = os.environ.get("DJANGO_ALLOWED_HOSTS")
DJANGO_ALLOWED_HOSTS = ['.herokuapp.com', 'taos-haus.com', '.taostechsolutions.com', '127.0.0.1']
ALLOWED_HOSTS = ['.herokuapp.com', 'taos-haus.com', '.taostechsolutions.com', '127.0.0.1']

DEVELOPMENT_MODE = False

if ENVIRONMENT == 'production':
    ADMINS = []
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    SECURE_HSTS_SECONDS = 3600
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_HSTS_PRELOAD = True
    SECURE_CONTENT_TYPE_NOSNIFF = True
    SECURE_BROWSER_XSS_FILTER = True
    X_FRAME_OPTIONS = 'DENY'
    SECURE_SSL_REDIRECT = not DEBUG
# Application definition

SECURE_HSTS_SECONDS = 100000

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'frontend',
    'phonenumber_field',
    'django_htmx',
    'django_ajax',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    "django_htmx.middleware.HtmxMiddleware",
]

ROOT_URLCONF = 'main.urls'



# Define the template directories for each app
APP_TEMPLATE_DIRS = [
    os.path.join(BASE_DIR, 'djapp', 'templates'),
    os.path.join(BASE_DIR, 'frontend', 'templates'),

    # Add more app-specific template directories as needed
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': APP_TEMPLATE_DIRS,
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

WSGI_APPLICATION = 'main.wsgi.application'

#messages
MESSAGE_TAGS = {
    messages.DEBUG: 'alert-secondary',
    messages.INFO: 'alert-info',
    messages.SUCCESS: 'alert-success',
    messages.WARNING: 'alert-warning',
    messages.ERROR: 'alert-danger',
}

if ENVIRONMENT == 'production':
    DATABASE_URL = str(os.getenv('DATABASE_URL'))

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': str(os.getenv('DB_NAME')),
            'USER': str(os.getenv('DB_USER')),
            'PASSWORD': str(os.getenv('DB_PASSWORD')),
            'HOST': str(os.getenv('DB_HOST')),
            'PORT': os.getenv('DB_PORT'),
        },
    }

    DATABASES['default'] = dj_database_url.config(
        default=str(os.getenv('DATABASE_URL')),
        conn_max_age=600,
        conn_health_checks=True,
    )
else:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
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
PHONENUMBER_DEFAULT_REGION = 'US'

TIME_ZONE = 'America/New_York'

USE_I18N = True

USE_TZ = True

DATETIME_FORMAT = "m-d-Y || H:i"
USE_L10N = False



STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# SMTP SETTINGS
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_USE_TLS = True
EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')
DEFAULT_FROM_EMAIL = os.getenv('DEFAULT_FROM_EMAIL')
