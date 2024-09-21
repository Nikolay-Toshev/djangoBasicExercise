from django.db import models
from workshop_1.photos.models import Photo

class Comment(models.Model):
    text = models.TextField(max_length=300)
    date_of_publication = models.DateTimeField(auto_now_add=True)
    to_photo = models.ForeignKey(Photo, on_delete=models.CASCADE)