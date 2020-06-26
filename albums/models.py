from django.db import models

# Create your models here.
class Album(models.Model):

    title = models.CharField()
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name="albums")
    release_year = models.IntegerField()

class Artist(models.Model):

    name = models.CharField()