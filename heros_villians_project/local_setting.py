# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-gldakih@(@q-zt^wj=^4v9#_&eqdkc5^oao)+^#6nzb@#fni7='

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'h&v_database',
        'USER': 'root',
        'PASSWORD': 'flyhigh20',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'OPTIONS': {
            'autocommit': True
        }
        
    }
}
