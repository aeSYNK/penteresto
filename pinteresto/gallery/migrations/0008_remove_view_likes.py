# Generated by Django 4.0.1 on 2022-01-20 19:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0007_post_likes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='view',
            name='likes',
        ),
    ]
