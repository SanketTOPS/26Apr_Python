# Generated by Django 4.2.3 on 2023-08-21 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notesapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='mynotes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('query', models.CharField(max_length=100)),
                ('opt', models.CharField(max_length=100)),
                ('myfiles', models.FileField(upload_to='MyNOTES')),
                ('comments', models.TextField()),
            ],
        ),
    ]