from recipe_manager.settings import *


DEBUG = False
ALLOWED_HOSTS = [os.environ.get('ALLOWED_HOSTS', '*')]

STATIC_ROOT = os.environ['STATIC_ROOT']

SECRET_KEY = os.environ['SECRET_KEY']
