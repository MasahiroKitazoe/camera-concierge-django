from .base import *

DATABASES = env("DATABASES")
HOST = env("HOST")
DB_PASSWORD = env("DB_PASSWORD")
DB_USER = env("DB_USER")

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'cam_ranks_production',
        "DATABASES": DATABASES,
        "HOST": HOST,
        "PASSWORD": DB_PASSWORD,
        "USER": DB_USER,
        "PORT": "5432",
    }
}

import dj_database_url
db_from_env = dj_database_url.config(conn_max_age=400)
DATABASES['default'].update(db_from_env)

DEBUG = False
