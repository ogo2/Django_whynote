# Generated by Django 3.2.11 on 2022-01-27 18:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profile_user', '0002_auto_20220127_2132'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='followers',
        ),
        migrations.RemoveField(
            model_name='users',
            name='sub',
        ),
    ]