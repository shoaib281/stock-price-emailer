# Generated by Django 4.1 on 2022-09-03 17:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stocks', '0006_rename_emailconfirmation_emailconfirmations_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='stocks',
            old_name='day',
            new_name='percentage',
        ),
        migrations.RemoveField(
            model_name='stocks',
            name='month',
        ),
        migrations.RemoveField(
            model_name='stocks',
            name='week',
        ),
    ]
