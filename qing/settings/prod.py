from .common import *

DEBUG = False
ALLOWED_HOSTS = ['52.79.161.35', 'qing.kr', 'www.qing.kr']



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': 'localhost',
        'NAME': 'qing',
        'USER': 'rocketdan',
        'PASSWORD': 'rocketdan',
    },
}