# Generated by Django 3.2.8 on 2021-10-29 20:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0008_auto_20211029_1951'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='likes',
        ),
    ]
