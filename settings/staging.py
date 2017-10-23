from base import *
import dj_database_url

DEBUG = False

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': dj_database_url.config('CLEARDB_DATABASE_URL')
}

# Stripe environment variables
STRIPE_PUBLISHABLE = os.getenv('STRIPE_PUBLISHABLE', 'pk_test_WPgPzAQeCfea08WkskzTqxii')
STRIPE_SECRET = os.getenv('STRIPE_SECRET', 'sk_test_6vCTHyEBILOhXzg3gfMd9U8w')

SITE_URL = 'https://wedding-stationery-shop.herokuapp.com/'
ALLOWED_HOSTS.append('wedding-stationery-shop.herokuapp.com')

# Log DEBUG information to the console
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': os.getenv('DJANGO_LOG_LEVEL', 'DEBUG'),
        },
    },
}
