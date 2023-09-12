"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 4.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

import os
from pathlib import Path
from urllib.parse import urlparse

from dotenv import load_dotenv

load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True if os.getenv("DEBUG") == "True" else False

HOST_URL = os.getenv("HOST_URL", "127.0.0.1, localhost")
ALLOWED_HOSTS = HOST_URL.replace(" ", "").split(",")

# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "mozilla_django_oidc",
    "oidc_provider",
    "dsfr",
    "sso",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "csp.middleware.CSPMiddleware",
    "django_referrer_policy.middleware.ReferrerPolicyMiddleware",
]

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            os.path.join(BASE_DIR, "dsfr/templates"),
            os.path.join(BASE_DIR, "templates"),
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "dsfr.context_processors.site_config",
            ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

postgres_url = urlparse(os.getenv("DATABASE_URL"))
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": postgres_url.path[1:] or os.getenv("DATABASE_NAME"),
        "USER": postgres_url.username or os.getenv("DATABASE_USER"),
        "PASSWORD": postgres_url.password or os.getenv("DATABASE_PASSWORD"),
        "HOST": postgres_url.hostname or os.getenv("DATABASE_HOST"),
        "PORT": postgres_url.port or os.getenv("DATABASE_PORT"),
    }
}
AUTH_USER_MODEL = "sso.User"

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = "static/"
STATIC_ROOT = "staticfiles"

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# FORM_RENDERER = "django.forms.renderers.TemplatesSetting"

# CSP-related options
SECURE_HSTS_SECONDS = 2592000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True

SECURE_CONTENT_TYPE_NOSNIFF = True

X_FRAME_OPTIONS = "DENY"

CSP_DEFAULT_SRC = "'self'"
CSP_STYLE_SRC = "'self' 'sha256-Eyt3MCqJJqqqUJzUlVq9BLYX+kVGQZVLpJ4toZz4mb8=' 'sha256-d//Lck7pNf/OY9MPfGYaIOTmqjEzvwlSukK3UObI08A=' 'sha256-28J4mQEy4Sqd0R+nZ89dOl9euh+Y3XvT+VfXD5pOiOE='"
CSP_IMG_SRC = "'self' data:"
CSP_SCRIPT_SRC = [
    "'self'",
    "'sha256-a28Komkyw2vnuwMdBLFFY3y1uJCXIFk2nAOcCqEWkf4='",  # sso/templates/sso/oidc/multi-login.html
]
REFERRER_POLICY = "same-origin"

ADMIN_URL = os.getenv("ADMIN_URL", "admin/")

# LOGIN and OIDC provider options
AUTHENTICATION_BACKENDS = (
    "django.contrib.auth.backends.ModelBackend",
    "sso.auth.OpiOidcAuthenticationBackend",
)
OIDC_RP_CLIENT_ID = os.environ["OIDC_RP_CLIENT_ID"]
OIDC_RP_CLIENT_SECRET = os.environ["OIDC_RP_CLIENT_SECRET"]
OIDC_OP_AUTHORIZATION_ENDPOINT = os.environ["OIDC_OP_AUTHORIZATION_ENDPOINT"]
OIDC_OP_TOKEN_ENDPOINT = os.environ["OIDC_OP_TOKEN_ENDPOINT"]
OIDC_OP_USER_ENDPOINT = os.environ["OIDC_OP_USER_ENDPOINT"]
OIDC_RP_SIGN_ALGO = "RS256"
OIDC_OP_JWKS_ENDPOINT = os.environ["OIDC_OP_JWKS_ENDPOINT"]
OIDC_RP_SCOPES = os.environ["OIDC_RP_SCOPES"]

LOGIN_URL = "/accounts/login/"
LOGIN_REDIRECT_URL = "/oidc/multi-login/"
LOGOUT_REDIRECT_URL = "/"

OIDC_AFTER_USERLOGIN_HOOK = "sso.hooks.do_autologin_after_successful_login"
OIDC_USERINFO = "config.oidc_provider_settings.userinfo"
