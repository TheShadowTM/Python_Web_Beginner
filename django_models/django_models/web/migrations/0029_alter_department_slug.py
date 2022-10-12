# Generated by Django 4.1.2 on 2022-10-09 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0028_fill_slug_for_existing_department'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='slug',
            field=models.SlugField(default='none', unique=True),
            preserve_default=False,
        ),
    ]