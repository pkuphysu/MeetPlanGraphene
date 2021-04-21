"""
Django settings for MeetPlan project.

Generated by 'django-admin startproject' using Django 3.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""
from datetime import timedelta
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-wly73vff5=3vza%+sq!!z_@=ca^$g@$y1nzn=zp(ddvaf@4m9t"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "graphene_django",
    "django_filters",
    "graphql_jwt.refresh_token",
    "guardian",
    "apps.user",
    "apps.pku_auth",
    "apps.meet_plan",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "MeetPlan.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "MeetPlan.wsgi.application"

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = "zh-Hans"

LANGUAGES = [
    ("zh-hans", "Simplified Chinese"),
    ("en", "English"),
]

LOCALE_PATHS = [
    BASE_DIR / "translation" / "locale",
    BASE_DIR / "translation" / "django_celery_beat",
    BASE_DIR / "translation" / "django_celery_results",
]

TIME_ZONE = "Asia/Shanghai"

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = "/static/"

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# the schema location for Graphene
# https://docs.graphene-python.org/projects/django/en/latest/installation/
GRAPHENE = {
    "SCHEMA": "MeetPlan.schema.schema",
    "ATOMIC_MUTATIONS": True,
    "MIDDLEWARE": [
        "graphql_jwt.middleware.JSONWebTokenMiddleware",
    ],
}
if DEBUG:
    GRAPHENE["MIDDLEWARE"].append("graphene_django.debug.DjangoDebugMiddleware")

AUTH_USER_MODEL = "user.User"

AUTHENTICATION_BACKENDS = [
    "apps.pku_auth.backends.OpenIDClientBackend",
    "graphql_jwt.backends.JSONWebTokenBackend",
    "guardian.backends.ObjectPermissionBackend",
    "django.contrib.auth.backends.ModelBackend",
]

GRAPHQL_JWT = {
    "JWT_VERIFY_EXPIRATION": True,
    "JWT_LONG_RUNNING_REFRESH_TOKEN": True,
    "JWT_REUSE_REFRESH_TOKENS": True,
    "JWT_EXPIRATION_DELTA": timedelta(hours=1),
    "JWT_REFRESH_EXPIRATION_DELTA": timedelta(days=7),
    "JWT_ALLOW_ANY_CLASSES": [
        "apps.pku_auth.schema.ObtainJSONWebToken",
        "apps.pku_auth.schema.Verify",
        "apps.pku_auth.schema.Refresh",
        "apps.pku_auth.schema.Revoke",
        "apps.pku_auth.schema.RevokeAll",
    ],
}

GRAPHENE_DJANGO_PLUS = {"MUTATIONS_INCLUDE_REVERSE_RELATIONS": False}

# Django Guardian
# https://django-guardian.readthedocs.io/en/stable/configuration.html#anonymous-user-name
ANONYMOUS_USER_NAME = "0000000000"
