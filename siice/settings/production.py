from .base import *

DEBUG = False

SPA_DIR = '/home/ronin/Projects/active/dnfas-ui/dist/'

MIDDLEWARE.remove('corsheaders.middleware.CorsMiddleware')

TEMPLATES[0]['DIRS'] = [SPA_DIR]

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'dnfas',
        'USER': 'dnfas',
        'PASSWORD': '123',
        'HOST': 'localhost',
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

STATICFILES_DIRS = [
    os.path.realpath(os.path.join(SPA_DIR, 'static')),
]

# Enable CORS for specified domains:
CORS_ORIGIN_ALLOW_ALL = True
#
# CORS_ORIGIN_WHITELIST = (
#     'http://localhost',
# )
