# Generated by Django 3.2.8 on 2021-10-29 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0005_alter_question_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='is_liked',
            field=models.BooleanField(default=False),
        ),
    ]
