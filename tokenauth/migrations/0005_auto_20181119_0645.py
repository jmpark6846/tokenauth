# Generated by Django 2.1.3 on 2018-11-19 06:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tokenauth', '0004_auto_20181119_0643'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userhaspermission',
            old_name='permissions',
            new_name='permission',
        ),
    ]
