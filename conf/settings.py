# -*- coding: utf-8 -*-
"""
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '91-5-@qz#n4e(6c_ott-pqps^&fqpw&_vehsrxuadm1srh0$ek'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'main_app'
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

ROOT_URLCONF = 'conf.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
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

WSGI_APPLICATION = 'conf.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'yyb',
        'USER': 'root',
        'PASSWORD': 'Jn8-$',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'





# MAIL_SERVER = 'smtp.qq.com'
# MAIL_POR = 465
# MAIL_USERNAME = ''
# MAIL_PASSWORD = ''
# MAIL_DEFAULT_SENDER = ''
# MAIL_RECEIVER = ['']


SECURITY_PASSWORD_SALT = 'grEARsdKEdwa'
RANDOM_SALT = 'awYw3jIEjeMv'


tonghuashun_api = 'http://q.10jqka.com.cn/api.php?t=indexflash&'
tonghuashun_post_search_api = 'http://www.iwencai.com/data-robot/get-fusion-data'
global_api = 'http://q.10jqka.com.cn/global/index/ajax/1/'
longhu = 'http://data.10jqka.com.cn/market/longhu/'
url_actvite = 'http://data.10jqka.com.cn/ifmarket/lhbyyb/type/1/tab/sbcs/field/sbcs/sort/desc/page/{pages}/'  # 活动次数最多
url_power = 'http://data.10jqka.com.cn/ifmarket/lhbyyb/type/1/tab/zjsl/field/zgczje/sort/desc/page/{pages}/'  # 资金实力最强
url_team = 'http://data.10jqka.com.cn/ifmarket/lhbyyb/type/1/tab/btcz/field/xsjs/sort/desc/page/{pages}/'  # 抱团能力最强

level = [u'知名游资', u'一线游资', u'毒瘤', u'跟风高手', u'新股专家']