# Generated by Django 2.1.2 on 2019-01-15 12:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('formprocessor', '0009_savedoptionsdata'),
    ]

    operations = [
        migrations.RenameField(
            model_name='savedoptionsdata',
            old_name='option_name',
            new_name='options_name',
        ),
    ]