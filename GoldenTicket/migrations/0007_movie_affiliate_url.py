# Generated by Django 4.0.3 on 2022-04-12 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GoldenTicket', '0006_remove_movie_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='affiliate_url',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
