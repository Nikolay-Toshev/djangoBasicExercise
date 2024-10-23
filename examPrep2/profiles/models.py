from django.core.validators import MinLengthValidator
from django.db import models

from profiles.validators import CharactersValidator, AgeValidator


class Profile(models.Model):
    username = models.CharField(
        max_length=15,
        unique=True,
        validators=[
            MinLengthValidator(3, message="Username must be at least 3 chars long!"),
            CharactersValidator(),
        ],
    )

    email = models.EmailField()

    age = models.PositiveSmallIntegerField(
        validators=[
            AgeValidator(),
        ],
    )

    password = models.CharField(
        max_length=20,
    )

    first_name = models.CharField(
        max_length=25,
        null=True,
        blank=True,
    )

    last_name = models.CharField(
        max_length=25,
        null=True,
        blank=True,
    )

    profile_picture = models.URLField(
        null=True,
        blank=True,
    )