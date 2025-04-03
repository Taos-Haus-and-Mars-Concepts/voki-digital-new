from pathlib import Path
from dotenv import load_dotenv
import os
import sys
import dj_database_url
from django.contrib.messages import constants as messages

# Set the environment (defaulting to "development")
ENVIRONMENT = str(os.getenv('ENVIRONMENT', 'development'))

# Load .env file for development and staging environments
if ENVIRONMENT in ['development', 'staging']:
    dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
    load_dotenv(dotenv_path)

# Define BASE_DIR using pathlib
BASE_DIR = Path(__file__).resolve().parent.parent

# Set the secret key from environment variables
SECRET_KEY = str(os.getenv('APP_SECRET_KEY'))

# Default settings; these will be overridden below based on the environment
DEBUG = True
DJANGO_ALLOWED_HOSTS = ['.herokuapp.com', 'vokidigital.com', '127.0.0.1']
ALLOWED_HOSTS = DJANGO_ALLOWED_HOSTS

# -------------------------------
# Conditional Settings by Environment
# -------------------------------

if ENVIRONMENT == 'production':
    DEBUG = False
    # Update allowed hosts for production
    ALLOWED_HOSTS = ['.herokuapp.com', 'vokidigital.com']

    # Use the production database URL and configure the database with dj_database_url
    DATABASE_URL = str(os.getenv('DATABASE_URL'))
    DATABASES = {
        'default': dj_database_url.config(
            default=DATABASE_URL,
            conn_max_age=600,
            conn_health_checks=True,
        )
    }
    # Enforce SSL/TLS on the database connection
    DATABASES['default']['OPTIONS'] = {
        'sslmode': 'require',
    }

    # Security settings for production
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    SECURE_HSTS_SECONDS = 3600
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_HSTS_PRELOAD = True
    SECURE_CONTENT_TYPE_NOSNIFF = True
    SECURE_BROWSER_XSS_FILTER = True
    X_FRAME_OPTIONS = 'DENY'
    SECURE_SSL_REDIRECT = True

elif ENVIRONMENT == 'staging':
    DEBUG = True
    # Update allowed hosts for staging
    ALLOWED_HOSTS = ['.herokuapp.com', 'vokidigital.com']

    # Use the development (or staging) database URL
    DATABASE_URL = str(os.getenv('DEV_DATABASE_URL'))
    DATABASES = {
        'default': dj_database_url.config(
            default=DATABASE_URL,
            conn_max_age=600,
            conn_health_checks=True,
        )
    }
    DATABASES['default']['OPTIONS'] = {
        'sslmode': 'require',
    }

    # Staging security settings (less strict than production)
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
    SESSION_COOKIE_SECURE = False
    CSRF_COOKIE_SECURE = False
    SECURE_HSTS_SECONDS = 3600
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_HSTS_PRELOAD = True
    SECURE_CONTENT_TYPE_NOSNIFF = True
    SECURE_BROWSER_XSS_FILTER = True
    SECURE_SSL_REDIRECT = True

else:
    # Development settings
    DEBUG = True
    ALLOWED_HOSTS = ['*']

    # Use a local SQLite database for development
    DATABASE_URL = str(os.getenv('DATABASE_URL'))
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
        }
    }

# -------------------------------
# Application Definition (Shared Across Environments)
# -------------------------------

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

# Define app-specific template directories
APP_TEMPLATE_DIRS = [
    os.path.join(BASE_DIR, 'frontend', 'templates'),
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

# Message tags for Django messages framework
MESSAGE_TAGS = {
    messages.DEBUG: 'alert-secondary',
    messages.INFO: 'alert-info',
    messages.SUCCESS: 'alert-success',
    messages.WARNING: 'alert-warning',
    messages.ERROR: 'alert-danger',
}

# Password validators
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

# Localization and timezone settings
LANGUAGE_CODE = 'en-us'
PHONENUMBER_DEFAULT_REGION = 'US'
TIME_ZONE = 'America/New_York'
USE_I18N = True
USE_TZ = True
DATETIME_FORMAT = "m-d-Y || H:i"
USE_L10N = False

# Static files settings
STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# SMTP email settings (shared across environments)
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_USE_TLS = True
EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')
DEFAULT_FROM_EMAIL = os.getenv('DEFAULT_FROM_EMAIL')
