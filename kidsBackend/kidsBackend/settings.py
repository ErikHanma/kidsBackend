import os
import pathlib


import django.urls
from django.utils.translation import gettext_lazy as _
import dotenv


dotenv.load_dotenv()


def true_load(value: str, defoult: bool) -> bool:
    env_value = os.getenv(value, str(defoult)).lower()
    return env_value in ("", "true", "yes", "1", "y")


BASE_DIR = pathlib.Path(__file__).resolve().parent.parent

SECRET_KEY = os.getenv("DJANGO_SECRET_KEY", "ABOBA")

DEBUG = true_load("DJANGO_DEBUG", False)

AUTH_USER_MODEL = "authUser.CustomUser"

DEFAULT_USER_IS_ACTIVE = true_load("DJANGO_DEFAULT_USER_IS_ACTIVE", DEBUG)

ALLOWED_HOSTS = list(
    map(str.strip, os.getenv("DJANGO_ALLOWED_HOSTS", "*").split(",")),
)

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "authUser.apps.AuthUserConfig",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

if DEBUG:
    INSTALLED_APPS.append("debug_toolbar")
    MIDDLEWARE.insert(0, "debug_toolbar.middleware.DebugToolbarMiddleware")
    INTERNAL_IPS = os.getenv("DJANGO_INTERNAL_IPS", "127.0.0.1").split(",")

ROOT_URLCONF = "kidsBackend.urls"

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

WSGI_APPLICATION = "kidsBackend.wsgi.application"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth."
        "password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth."
        "password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth."
        "password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth."
        "password_validation.NumericPasswordValidator",
    },
]

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

STATIC_URL = "static/"

LANGUAGES = [
    ("ru", _("Russian")),
    ("en", _("English")),
]

LOGIN_URL = django.urls.reverse_lazy("users:login")
LOGIN_REDIRECT_URL = django.urls.reverse_lazy("homepage:main")
LOGOUT_REDIRECT_URL = django.urls.reverse_lazy("homepage:main")

STATIC_ROOT = BASE_DIR.parent / "static"

MEDIA_ROOT = BASE_DIR / "media"
MEDIA_URL = "/media/"


DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
