# Generated by Django 4.1.1 on 2022-10-11 12:22

from django.db import migrations, models
import petstagram.photos.models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0004_alter_photo_tagged_pets'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='photo',
            field=models.ImageField(blank=True, upload_to='mediafiles/pet_photos/', validators=[petstagram.photos.models.validate_file_less_than_5]),
        ),
    ]
