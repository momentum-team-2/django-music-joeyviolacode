from django import forms
from .models import Album, Artist

class ArtistForm(forms.ModelForm):
    class Meta:
        model = Artist
        fields = [
            'name',
        ]

class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = [
            "title",
            "release_year",
            "favorite",
        ]