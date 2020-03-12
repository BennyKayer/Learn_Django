from .base import *  # noqa
from .base import env
import django_heroku

CORS_ORIGIN_WHITELIST = env.list(
    'CORS_ORIGIN_WHITELIST',
    default=[]
)
SECURE_SSL_REDIRECT = True

# Disables the browseable API
REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
    )
}

EMAIL_HOST = env.str('EMAIL_HOST', "or empty")
EMAIL_PORT = env.int('EMAIL_PORT', 587)
EMAIL_HOST_USER = env.str('EMAIL_HOST_USER', "or empty")
EMAIL_HOST_PASSWORD = env.str('EMAIL_HOST_PASSWORD', "or empty")
EMAIL_USE_SSL = True

django_heroku.settings(locals())