from apps.settings.base import *


IS_TEST = True


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": "memory",
    }
}

# make it less secure, but faster
PASSWORD_HASHERS = (
    "django.contrib.auth.hashers.MD5PasswordHasher",
)