# Generated by Django 5.1.2 on 2024-10-23 17:15

import django.core.validators
import profiles.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='age',
            field=models.PositiveSmallIntegerField(validators=[profiles.validators.AgeValidator()]),
        ),
        migrations.AlterField(
            model_name='profile',
            name='username',
            field=models.CharField(max_length=15, unique=True, validators=[django.core.validators.MinLengthValidator(3, message='Username must be at least 3 chars long!'), profiles.validators.CharactersValidator()]),
        ),
    ]
