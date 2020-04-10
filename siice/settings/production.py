from .base import *

DEBUG = False

_hosts = os.environ.get('SIICE_ALLOWED_HOSTS')

ALLOWED_HOSTS.extend(_hosts.split(','))

SECRET_KEY = os.environ['SIICE_SECRET_KEY']

SPA_DIR = os.environ.get('SIICE_SPA_DIR', '')

if SPA_DIR:
    SPA_DIR = os.path.realpath(SPA_DIR)
    TEMPLATES[0]['DIRS'] = [SPA_DIR]

    STATICFILES_DIRS = [
        os.path.realpath(os.path.join(SPA_DIR, 'static'))
    ]

MIDDLEWARE.remove('corsheaders.middleware.CorsMiddleware')

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ['SIICE_DB_NAME'],
        'USER': os.environ['SIICE_DB_USER'],
        'PASSWORD': os.environ['SIICE_DB_PASSWORD'],
        'HOST': os.environ['SIICE_DB_HOST'],
        'PORT': '',
    }
}

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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

# Django rest framework
REST_FRAMEWORK.update({
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'users.backends.JWTAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ]
})

