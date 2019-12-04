import os
DEBUG = True
# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases
ALLOWED_HOSTS = ["127.0.0.1","localhost","nowpaas.ap-south-1.elasticbeanstalk.com"]
if 'RDS_HOSTNAME' in os.environ:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': os.environ['RDS_DB_NAME'],
            'USER': os.environ['RDS_USERNAME'],
            'PASSWORD': os.environ['RDS_PASSWORD'],
            'HOST': os.environ['RDS_HOSTNAME'],
            'PORT': os.environ['RDS_PORT'],
        }
    }

STATIC_ROOT = 'static'