# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'npdb',
        'USER': 'nishant',
        'PASSWORD': '12345678',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}