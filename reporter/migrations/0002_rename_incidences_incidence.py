# Generated by Django 4.1.3 on 2022-12-04 16:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reporter', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Incidences',
            new_name='Incidence',
        ),
    ]