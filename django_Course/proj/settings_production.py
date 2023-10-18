from .settings import *
DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'sidia',
        'USER': 'postgres',
        'PASSWORD': 'root',
        'HOST': 'sidia-db',
        'PORT': '5432',
    }
}
