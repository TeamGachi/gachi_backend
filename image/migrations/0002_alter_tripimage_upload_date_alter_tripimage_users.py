# Generated by Django 4.2 on 2023-09-26 06:34

import datetime
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('image', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tripimage',
            name='upload_date',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='tripimage',
            name='users',
            field=models.ManyToManyField(null=True, to=settings.AUTH_USER_MODEL),
        ),
    ]