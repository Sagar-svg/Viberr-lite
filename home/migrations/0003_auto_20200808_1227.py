# Generated by Django 3.0.8 on 2020-08-08 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20200808_1224'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='album_cover',
            field=models.ImageField(upload_to='pics'),
        ),
        migrations.AlterField(
            model_name='song',
            name='song_cover',
            field=models.ImageField(upload_to='pics'),
        ),
    ]
