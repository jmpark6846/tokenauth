# Generated by Django 2.1.3 on 2018-11-19 03:43

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tokenauth', '0002_auto_20181119_0338'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='custompermission',
            name='user',
        ),
        migrations.AddField(
            model_name='custompermission',
            name='users',
            field=models.ManyToManyField(related_name='permissions', to=settings.AUTH_USER_MODEL),
        ),
    ]
