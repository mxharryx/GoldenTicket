# Generated by Django 4.0.3 on 2022-04-12 05:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('GoldenTicket', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movies',
            old_name='movie_rate',
            new_name='movie_rating',
        ),
    ]
