# Generated by Django 4.1.2 on 2022-10-07 13:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0021_employeesprojects'),
    ]

    operations = [
        migrations.CreateModel(
            name='AccessCard',
            fields=[
                ('employee', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='web.employee')),
            ],
        ),
    ]
