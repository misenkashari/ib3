# Generated by Django 3.2.8 on 2021-10-29 19:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0006_question_is_liked'),
    ]

    operations = [
        migrations.RenameField(
            model_name='answer',
            old_name='body',
            new_name='answer',
        ),
    ]
