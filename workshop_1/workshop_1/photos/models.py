from django.contrib.auth import get_user_model
from django.db import models
from django.core.validators import MinValueValidator, MinLengthValidator
from workshop_1.pets.models import Pet
from workshop_1.photos.validators import validate_file_size

UserModel = get_user_model()

class Photo(models.Model):
    photo = models.ImageField(validators=(validate_file_size, ), upload_to='img')
    description = models.TextField(max_length=300, validators=[MinLengthValidator(10)], blank=True, null=True)
    location = models.CharField(max_length=30, blank=True, null=True)
    tagged_pets = models.ManyToManyField(Pet, blank=True)
    date_of_publication = models.DateField(auto_now=True)
    user = models.ForeignKey(UserModel, null=False, blank=True, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-date_of_publication']