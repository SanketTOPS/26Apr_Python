# Generated by Django 4.2.3 on 2023-08-21 04:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notesapp', '0003_alter_mynotes_myfiles'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mynotes',
            name='created',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 8, 21, 9, 39, 57, 740875)),
        ),
    ]
