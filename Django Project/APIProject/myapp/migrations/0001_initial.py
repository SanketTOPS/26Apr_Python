# Generated by Django 4.2.3 on 2023-09-25 04:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='studinfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=20)),
                ('sub', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('city', models.CharField(max_length=20)),
            ],
        ),
    ]