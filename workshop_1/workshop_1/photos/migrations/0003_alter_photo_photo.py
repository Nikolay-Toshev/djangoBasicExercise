# Generated by Django 5.1.1 on 2024-10-13 16:47

import workshop_1.photos.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0002_alter_photo_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='photo',
            field=models.ImageField(upload_to='img', validators=[workshop_1.photos.validators.validate_file_size]),
        ),
    ]
