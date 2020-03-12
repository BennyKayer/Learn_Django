from .base import *  # noqa
from .base import env


DEBUG = True
SECRET_KEY = env('SECRET_KEY')
ALLOWED_HOSTS = ['localhost', '0.0.0.0', '127.0.0.1']
CORS_ORIGIN_ALLOW_ALL = True
EMAIL_BACKEND = env(
    "EMAIL_BACKEND",
    default="django.core.mail.backends.console.EmailBackend"
)

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': env('DB_NAME'),
        'USER': env('DB_USER'),
        'PASSWORD': env('DB_PASSWORD'),
        'TEST': {
            'NAME': env('DB_TEST_NAME')
        }
    }
}

LOGGING = {
    "version": 1,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler'
        }
    },
    "loggers": {
        "django.db.backends": {
            'handlers': ['console'],
            "level": "DEBUG",
        },
    },
}