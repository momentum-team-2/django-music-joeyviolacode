# Generated by Django 3.0.7 on 2020-06-26 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('albums', '0002_album_favorite'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='artist_string',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
