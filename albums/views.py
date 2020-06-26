from django.shortcuts import render, redirect, get_object_or_404
# from django.core.exceptions import ObjectDoesNotExist
from .models import Album, Artist
# from .forms import AlbumForm, ArtistForm

# Create your views here.
def list_albums(request):
    albums = Album.objects.all()
    return render(request, "albums/list_albums.html", { "albums" : albums})


def add_album(request):
    pass

def show_album(request, pk):
    pass

def edit_album(request, pk):
    pass

def delete_album(request, pk):
    pass