from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models
from car.validators import YearValidator
from profiles.models import Profile


class Car(models.Model):
    CHOICES = (
        ("Rally", "Rally"),
        ("Open-wheel", "Open-wheel"),
        ("Kart", "Kart"),
        ("Drag", "Drag"),
        ("Other", "Other"),
    )

    type = models.CharField(
        max_length=10,
        choices=CHOICES,
    )

    model = models.CharField(
        max_length=15,
        validators=[
            MinLengthValidator(1),
        ],
    )

    year = models.PositiveSmallIntegerField(
        validators=[YearValidator(),]
    )

    image_url = models.URLField(
        unique=True,
        error_messages={'unique':"This image URL is already in use! Provide a new one."}
    )

    price = models.FloatField(
        validators=[MinValueValidator(1.0),],
    )

    owner = models.ForeignKey(
        to=Profile,
        on_delete=models.CASCADE,
        related_name='cars',
    )