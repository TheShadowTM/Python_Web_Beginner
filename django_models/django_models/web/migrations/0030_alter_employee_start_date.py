# Generated by Django 4.1.2 on 2022-10-09 13:28

from django.db import migrations, models
import django_models.web.validators


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0029_alter_department_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='start_date',
            field=models.DateField(validators=[django_models.web.validators.validate_before_today]),
        ),
    ]
