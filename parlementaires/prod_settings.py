import dj_database_url
from .settings import *


DEBUG = True
# TEMPLATES_DEBUG = False

DATABASES['default'] = dj_database_url.config()


ALLOWED_HOSTS = ['parlementaires.herokuapp.com']
