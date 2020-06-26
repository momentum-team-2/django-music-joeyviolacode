from django.db import models

# Create your models here.

class Artist(models.Model):

    name = models.CharField(max_length=255)

class Album(models.Model):

    title = models.CharField(max_length=255)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name="albums")
    release_year = models.IntegerField()
