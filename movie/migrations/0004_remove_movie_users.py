# Generated by Django 4.1.7 on 2023-03-10 16:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0003_alter_movie_duration_alter_movie_year'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='users',
        ),
    ]
