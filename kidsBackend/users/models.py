from pathlib import Path
import uuid
import sys
import uuid

from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
import django.db

import users.validators


class UserManager(django.contrib.auth.models.UserManager):
    pass


class User(AbstractUser):
    def get_path_image(self, filename):
        ext = Path(filename).suffix
        return f"users/{self.id}/avatar{ext}"

    objects = UserManager()

    username = django.db.models.CharField(
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

    email = django.db.models.EmailField(
        _("email address"),
        blank=True,
        unique=True,
    )

    bio = django.db.models.TextField(
        _("biography"),
        max_length=4000,
        help_text=_("bio_field_help"),
        blank=True,
        null=True,
    )

    birthday = django.db.models.DateField(
        _("birthday"),
        help_text=_("birthday_field_help"),
        validators=[users.validators.birthday_validator],
        null=True,
        blank=True,
    )

    # avatar = sorl.thumbnail.ImageField(
    #     _("avatar"),
    #     help_text=_("avatar_field_help"),
    #     upload_to=get_path_image,
    #     null=True,
    #     blank=True,
    # )

    def __str__(self):
        return f"Профиль пользователя {self.username}"

    class Meta:
        verbose_name = "пользователя"
        verbose_name_plural = "пользователи"

