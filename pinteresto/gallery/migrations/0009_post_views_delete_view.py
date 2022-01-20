# Generated by Django 4.0.1 on 2022-01-20 20:42

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('gallery', '0008_remove_view_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='views',
            field=models.ManyToManyField(related_name='view_posts', to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='View',
        ),
    ]
