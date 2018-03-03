from .common import *

DEBUG = False
ALLOWED_HOSTS = ['18.220.12.176', ]


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': 'localhost',
        'NAME': 'qing',
        'USER': 'rocketdan',
        'PASSWORD': 'rocketdan',
    },
}