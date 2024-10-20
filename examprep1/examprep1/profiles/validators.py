import string

from django.core.exceptions import ValidationError


def validate_symbols(value):
    allowed_characters = string.ascii_letters + string.digits + '_'
    for i in range(len(value)):
        if value[i] not in allowed_characters:
            raise ValidationError("Ensure this value contains only letters, numbers, and underscore.")