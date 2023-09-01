# Generated by Django 4.2.3 on 2023-08-28 03:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notesapp', '0004_alter_mynotes_created'),
    ]

    operations = [
        migrations.CreateModel(
            name='callback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(blank=True, default=datetime.datetime(2023, 8, 28, 9, 27, 4, 859963))),
                ('fullname', models.CharField(max_length=50)),
                ('mobile', models.BigIntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('msg', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='mynotes',
            name='created',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 8, 28, 9, 27, 4, 858963)),
        ),
    ]