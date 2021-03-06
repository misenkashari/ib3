# Generated by Django 3.2.8 on 2021-10-29 19:51

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('questions', '0007_rename_body_answer_answer'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='is_liked',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='answer',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='answers', to=settings.AUTH_USER_MODEL),
        ),
    ]
