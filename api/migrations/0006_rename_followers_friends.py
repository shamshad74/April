# Generated by Django 4.1.1 on 2023-01-05 20:16

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0005_remove_userprofile_followings_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Followers',
            new_name='Friends',
        ),
    ]
