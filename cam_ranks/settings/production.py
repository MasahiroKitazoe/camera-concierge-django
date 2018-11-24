from .base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

import dj_database_url
db_from_env = dj_database_url.config(conn_max_age=400)
DATABASES['default'].update(db_from_env)


DEBUG = False
