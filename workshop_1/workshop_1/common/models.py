from django.contrib.auth import get_user_model
from django.db import models
from workshop_1.photos.models import Photo

UserModel = get_user_model()

class Comment(models.Model):
    text = models.TextField(max_length=300)
    date_of_publication = models.DateTimeField(auto_now_add=True)
    to_photo = models.ForeignKey(Photo, on_delete=models.CASCADE)
    user = models.ForeignKey(to=UserModel, null=False, blank=True, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-date_of_publication']

class Like(models.Model):
    to_photo = models.ForeignKey(Photo, on_delete=models.CASCADE)
    user = models.ForeignKey(to=UserModel, null=False, blank=True, on_delete=models.CASCADE)