from .base import *

DEBUG = False
ALLOWED_HOSTS = ['django-celery-asynx.herokuapp.com']
DATABASES = {
    'default': {
        # 'ENGINE': 'django.db.backends.sqlite3',
        # 'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'd9menh4cu8t4js',
        'USER': 'gcevjfiwyytjke',
        'PASSWORD': '06174c7cb6b62a5ebc6f30b5d4ba24597645e01f15af560af560e006a00ad95d',
        'HOST': 'ec2-23-23-173-30.compute-1.amazonaws.com',
        'PORT': '5432',
    }
}