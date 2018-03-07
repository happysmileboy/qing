from .common import *

DEBUG = False
ALLOWED_HOSTS = ['qing.kr', ]


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': 'localhost',
        'NAME': 'qing',
        'USER': 'rocketdan',
        'PASSWORD': 'rocketdan',
    },
}