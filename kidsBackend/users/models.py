from pathlib import Path
import uuid
import sys
import uuid

from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
import django.db
from django.db import models

import users.validators


class UserManager(django.contrib.auth.models.UserManager):
    pass


# Роли пользователей
class Role(models.Model):
    name = models.CharField(max_length=255, unique=True)  # Название роли
    description = models.TextField(blank=True, null=True)  # Описание роли
    user = models.OneToOneField('User', on_delete=models.CASCADE, related_name='role')  # ID пользователя

    def __str__(self):
        return self.name


# Пользовательская модель
class User(AbstractUser):
    username = models.CharField(
        _("username"),
        max_length=32,
        unique=True,
        help_text=_("username_field_help"),
        validators=[
            users.validators.UsernameValidator(),
        ],
        error_messages={
            "unique": _("A user with that username already exists."),
        },
    )
    email = models.EmailField(
        _("email address"),
        blank=True,
        unique=True,
    )
    birthday = models.DateField(
        _("birthday"),
        help_text=_("birthday_field_help"),
        validators=[users.validators.birthday_validator],
        null=True,
        blank=True,
    )

    def __str__(self):
        return f"Профиль пользователя {self.username}"

    class Meta:
        verbose_name = "пользователь"
        verbose_name_plural = "пользователи"
