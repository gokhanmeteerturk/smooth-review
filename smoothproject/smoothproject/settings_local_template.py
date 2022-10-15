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

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'email-smtp.us-east-1.amazonaws.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = 'noreply@smoothreviews.net'
