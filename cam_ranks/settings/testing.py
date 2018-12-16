from .base import *


IS_TEST = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# make it less secure, but faster
PASSWORD_HASHERS = (
    "django.contrib.auth.hashers.MD5PasswordHasher",
)
