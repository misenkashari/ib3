# Generated by Django 3.2.8 on 2021-10-29 14:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0002_alter_question_author'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='body',
            new_name='question',
        ),
    ]
