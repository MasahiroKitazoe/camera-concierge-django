from .base import *

import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'cam_ranks',
        'USER': 'masahiro',
        'PASSWORD': 'pass',
        'HOST': '127.0.0.1',  # ホスト名はローカルのIPを指定してます
        'PORT': '5432',  # PORTは先の docker ps で表示されていたポートを指定します
    }
}

DEBUG = True

INTERNAL_IPS = ['127.0.0.1']
