import django.contrib.auth.models
import django.db

__all__ = []


class CustomUser(django.contrib.auth.models.AbstractUser):
    pass
