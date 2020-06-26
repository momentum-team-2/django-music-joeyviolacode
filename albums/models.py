from django.db import models

# Create your models here.

class Artist(models.Model):

    name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name}"

class Album(models.Model):

    title = models.CharField(max_length=255)
    artist_string =  models.CharField(max_length=255)
    release_year = models.IntegerField()
    favorite = models.BooleanField(default=False)

    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name="albums")

    def __str__(self):
        return f"{self.title} - {self.artist}"