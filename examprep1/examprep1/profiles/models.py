from django.core.validators import MinLengthValidator
from django.db import models

from examprep1.profiles.validators import validate_symbols


class Profile(models.Model):
    username = models.CharField(
        max_length=15,
        validators=[
            MinLengthValidator(2),
            validate_symbols,
        ],
    )

    email = models.EmailField(

    )

    age = models.PositiveSmallIntegerField(
        null=True,
        blank=True,
    )