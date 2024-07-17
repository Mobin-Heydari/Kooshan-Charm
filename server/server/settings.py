from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-ol1f=^g^$3+g@p1_*oyp)xl3yw+je#0ks2w=no9zqaxc=p4(!9'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition
INSTALLED_APPS = [
    # Admin Panel Third Party
    'jazzmin',
    
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    # Custome apps
    'products.apps.ProductsConfig',
    'cart.apps.CartConfig',
    'account.apps.AccountConfig',
    'profiles.apps.ProfilesConfig',
    'addreses.apps.AddresesConfig',
    'orders.apps.OrdersConfig',
    'payment.apps.PaymentConfig',
    'home.apps.HomeConfig',
    'contactus.apps.ContactusConfig',
    
    # PWA
    'pwa'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'server.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'APP_DIRS': True,
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'server.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'
MEDIA_URL = 'media/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# Auth User 
AUTH_USER_MODEL = "account.User"


#   Zarinpal --api--merchand
# SANDBOX MODE
MERCHANT = "00000000-0000-0000-0000-000000000000"
SANDBOX = True


# Service worker path
PWA_SERVICE_WORKER_PATH = os.path.join(BASE_DIR, 'static/assets/js', 'serviceworker.js')


# PWA manifest settings
PWA_APP_NAME = "Hendrix Shop"
PWA_APP_DESCRIPTION = "هندریکس شاپ فروشگاه لوازم خانگی"
PWA_APP_THEME_COLOR = "5, 150, 105"
PWA_APP_BACKGROUND_COLOR = "5, 150, 105"
PWA_APP_DISPLAY = 'standalone'
PWA_APP_SCOPE = '/'
PWA_APP_ORIENTATION = 'portrait'
PWA_APP_START_URL = '/'
PWA_APP_ICONS = [
    {
        'src': '/static/assets/images/logo.png',
        'sizes': '160x160'
    }
]
PWA_APP_ICONS_APPLE = [
    {
        'src': '/static/assets/images/logo.png',
        'sizes': '160x160'
    }
]


# Service worker path
PWA_SERVICE_WORKER_PATH = os.path.join(BASE_DIR, 'static/assets/js', 'serviceworker.js')


# PWA manifest settings
PWA_APP_NAME = "Kooshan Charm"
PWA_APP_DESCRIPTION = "فروشگاه اینترنتی لوازم چرمی"
PWA_APP_THEME_COLOR = '#000000'
PWA_APP_BACKGROUND_COLOR = '#ffffff'
PWA_APP_DISPLAY = 'standalone'
PWA_APP_SCOPE = '/'
PWA_APP_ORIENTATION = 'any'
PWA_APP_START_URL = '/'
PWA_APP_STATUS_BAR_COLOR = 'default'
PWA_APP_ICONS = [
    {
        'src': '/static/assets/images/pwa/logos/win/192x192.png',
        'sizes': '192x192'
    },
    {
        'src': '/static/assets/images/pwa/logos/win/256x256.png',
        'sizes': '256x256'
    },
    {
        'src': '/static/assets/images/pwa/logos/win/384x384.png',
        'sizes': '384x384'
    },
    {
        'src': '/static/assets/images/pwa/logos/win/512x512.png',
        'sizes': '512x512'
    },
    
    # Androids
    {
        'src': '/static/assets/images/pwa/logos/android/72x72.png',
        'sizes': '72x72'
    },
    {
        'src': '/static/assets/images/pwa/logos/android/96x96.png',
        'sizes': '96x96'
    },
    
    {
        'src': '/static/assets/images/pwa/logos/android/128x128.png',
        'sizes': '128x128'
    },
    
    {
        'src': '/static/assets/images/pwa/logos/android/144x144.png',
        'sizes': '144x144'
    },
    
    {
        'src': '/static/assets/images/pwa/logos/android/152x152.png',
        'sizes': '152x152'
    },
    
    {
        'src': '/static/assets/images/pwa/logos/android/192x192.png',
        'sizes': '192x192'
    },
    
    {
        'src': '/static/assets/images/pwa/logos/android/384x384.png',
        'sizes': '384x384'
    },
    
    {
        'src': '/static/assets/images/pwa/logos/android/512x512.png',
        'sizes': '512x512'
    },
]

PWA_APP_ICONS_APPLE = [
    {
        'src': '/static/assets/images/pwa/logos/ios/120x120.png',
        'sizes': '120x120'
    }
]

PWA_APP_SPLASH_SCREEN = [
    {
        'src': '/static/assets/images/pwa/logos/ios/120x120.png',
        'media': '(device-width: 120px) and (device-height: 120px) and (-webkit-device-pixel-ratio: 2)'
    }
]

PWA_APP_DIR = 'rtl'
PWA_APP_LANG = 'fa-IR'