import os

DEBUG = True

SITE_ID = 1

TEST_ROOT = os.path.normcase(os.path.dirname(os.path.abspath(__file__)))
FIXTURES_ROOT = os.path.join(TEST_ROOT, 'fixtures')

MEDIA_ROOT = os.path.join(os.path.normcase(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), 'media')
MEDIA_URL = '/media/'

STATIC_ROOT = os.path.join(os.path.normcase(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), 'static')
STATIC_URL = '/static/'

DATABASE_ENGINE = 'sqlite3'
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth'
            ],
        }
    },
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(TEST_ROOT, 'db.sqlite3'),
    }
}

INSTALLED_APPS = [
    'django.contrib.contenttypes',
    'django.contrib.sites',
    'django.contrib.auth',
    'django.contrib.admin',
    'django.contrib.sessions',
    'django.contrib.staticfiles',
    'django.contrib.messages',

    'easy_thumbnails_admin',
    'easy_thumbnails',
    'tests',
    'django_extensions',
]

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

# This is only needed for the 1.4.X test environment
USE_TZ = True
ROOT_URLCONF = 'tests.urls'

SECRET_KEY = 'easy'

THUMBNAIL_ALIASES = {
    'tests.Example.image': {
        'catalog': {
            'size': (100, 100), 'crop': 'smart',
            'admin': {
                'help_text': 'Example help_text',
            }
        },
        'catalog_large': {'size': (300, 300), 'crop': 'smart'},
        'front': {'size': (300, 100), 'crop': 'smart'},
        'mobile': {'size': (125, 85), 'crop': 'smart'},
        'preview': {'size': (400, 400), 'crop': 'smart'},
    }
}

THUMBNAIL_PROCESSORS = (
    'easy_thumbnails.processors.colorspace',
    'easy_thumbnails.processors.autocrop',
    'easy_thumbnails_admin.processors.scale_and_crop',
    'easy_thumbnails.processors.filters',
    'easy_thumbnails.processors.background',
)
# THUMBNAIL_NAMER = 'easy_thumbnails_admin.namers.default'
