import django.apps

__all__ = []


class AuthUserConfig(django.apps.AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "authUser"
    verbose_name = "authUser"
