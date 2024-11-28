import django.contrib.admin
import django.contrib.auth.admin
import django.utils.safestring
from django.utils.translation import gettext as _
import users.models

__all__ = []


@django.contrib.admin.register(users.models.User)
class UserAdmin(django.contrib.auth.admin.UserAdmin):
    list_display = (
        users.models.User.id.field.name,
        users.models.User.username.field.name,
    )

