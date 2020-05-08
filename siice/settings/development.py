from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

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
        'CONN_MAX_AGE': 0
    }
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }

# Django rest framework
REST_FRAMEWORK.update({
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'users.backends.JWTAuthentication',
    ),
    # 'DEFAULT_PERMISSION_CLASSES': [
    #     'rest_framework.permissions.IsAuthenticated',
    # ]
})

# Enable CORS for all domains
CORS_ORIGIN_ALLOW_ALL = True



