# Generated by Django 4.2.3 on 2023-08-21 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notesapp', '0002_mynotes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mynotes',
            name='myfiles',
            field=models.FileField(upload_to='Files'),
        ),
    ]