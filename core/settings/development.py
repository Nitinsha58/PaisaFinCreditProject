from core.settings.shared import *
from dotenv import load_dotenv
import os

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path)

OTP_AUTHORIZATION_KEY = os.getenv('OTP_AUTHORIZATION_KEY')

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "VerySecretDevelopmentKey"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["127.0.0.1", "localhost", "192.168.1.3"]

# If something needs to be at exact place, use insert instead
INSTALLED_APPS.insert(0, "whitenoise.runserver_nostatic")

# Add apps only for development mode as shown
INSTALLED_APPS += ["debug_toolbar"]

# Add middlewares only for development mode as shown
MIDDLEWARE += ["debug_toolbar.middleware.DebugToolbarMiddleware"]

# Iternal IPS required by django_debug_toolbar
INTERNAL_IPS = ["127.0.0.1"]

# Database
# https://docs.djangoproject.com/en/dev/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}
