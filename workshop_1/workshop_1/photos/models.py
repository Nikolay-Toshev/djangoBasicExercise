from django.db import models
from django.core.validators import MinValueValidator, MinLengthValidator
from workshop_1.pets.models import Pet
from workshop_1.photos.validators import validate_file_size

class Photo(models.Model):
    photo = models.ImageField(validators=(validate_file_size, ), upload_to='img')
    description = models.TextField(max_length=300, validators=[MinLengthValidator(10)], blank=True, null=True)
    location = models.CharField(max_length=30, blank=True, null=True)
    tagged_pets = models.ManyToManyField(Pet, blank=True)
    date_of_publication = models.DateField(auto_now=True)
