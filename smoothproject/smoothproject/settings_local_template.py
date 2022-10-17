ALLOWED_HOSTS = ['*']
DEBUG = True
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': '...',
        'USER': '...',
        'PASSWORD': '...',
        'HOST': '',
        'PORT': ''
    }
}
SECRET_KEY = '...............'
SECRET_KEY_FALLBACKS = []
DEVELOPMENT = True


AWS_ACCESS_KEY_ID = '...............'
AWS_SECRET_ACCESS_KEY = '..............'
AWS_STORAGE_BUCKET_NAME = '............'
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME

MIDDLEWARE_LOCAL = []

EMAIL_BACKEND = "anymail.backends.sendinblue.EmailBackend"
EMAIL_PORT = 587
ANYMAIL = {
    "SENDINBLUE_API_KEY": "-",
}
DEFAULT_FROM_EMAIL = 'noreply@smoothreviews.net'
SERVER_EMAIL = "noreply@smoothreviews.net"
