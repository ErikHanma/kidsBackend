import re

import django.core.exceptions
import django.core.validators
import django.utils.deconstruct
import django.utils.timezone
from django.utils.translation import gettext as _


@django.utils.deconstruct.deconstructible
class UsernameValidator(django.core.validators.RegexValidator):
    regex = r"^[\w_]{5,32}"
    message = _("username_validation_error")
    flags = re.ASCII


def birthday_validator(value):
    max_date = django.utils.timezone.now().date()
    if value > max_date:
        raise django.core.exceptions.ValidationError(
            _("birthday_validation_error"),
        )
    
def email_validator(value):
    if not re.match(r"[^@]+@[^@]+\.[^@]+", value):
        raise ValidationError(
            _('Enter a valid email address.'),
            params={'value': value},
        )
