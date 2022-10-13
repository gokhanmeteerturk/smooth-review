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
SECRET_KEY_FALLBACKS = ['django-insecure-pxl)3hru*t)3$+6(=l)e0y0rdfa@zfmeduk@d8f--dmfx53oaa']
DEVELOPMENT = True


AWS_ACCESS_KEY_ID = '...............'
AWS_SECRET_ACCESS_KEY = '..............'
AWS_STORAGE_BUCKET_NAME = '............'
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
