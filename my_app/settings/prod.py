from .common import *

# 本番環境用settings
DEBUG = False

ALLOWED_HOSTS = []

INSTALLED_APPS += (
    'gunicorn',
)