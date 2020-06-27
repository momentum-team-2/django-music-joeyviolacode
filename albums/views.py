from django.shortcuts import render, redirect, get_object_or_404
# from django.core.exceptions import ObjectDoesNotExist
from .models import Album, Artist
from .forms import AlbumForm, ArtistForm

# Create your views here.
def list_albums(request):
    albums = Album.objects.all()
    return render(request, "albums/list_albums.html", { "albums" : albums})


def add_album(request):
    if request.method == 'GET':
        form = AlbumForm()
    else:
        form = AlbumForm(data=request.POST)
        if form.is_valid():
            album = form.save(commit=False)
            artist_text = album.artist_string
            artist = None
            try:
                artist = Artist.objects.get(name=artist_text)
            except(Artist.DoesNotExist):
                artist = Artist(name=artist_text)
                artist.save()
            album.artist = artist
            album.save()
            return redirect(to='list_albums')
    return render(request, 'albums/add_album.html', { "form" : form })

def show_album(request, pk):
    album = get_object_or_404(Album, pk=pk)
    artist = album.artist
    return render(request, "albums/show_album.html", { "album" : album, "artist" : artist})

def edit_album(request, pk):
    album = get_object_or_404(Album, pk=pk)
    if request.method == 'GET':
        form = AlbumForm(instance=album)
    else:
        form = AlbumForm(data=request.POST, instance=album)
        if form.is_valid():
            album = form.save(commit=False)
            artist_text = album.artist_string
            artist = None
            try:
                artist = Artist.objects.get(name=artist_text)
            except(Artist.DoesNotExist):
                artist = Artist(name=artist_text)
                artist.save()
            album.artist = artist
            album.save()
            return redirect(to='list_albums')
    return render(request, 'albums/edit_album.html', { "form" : form , "album" : album })
    

def delete_album(request, pk):
    album = get_object_or_404(Album, pk=pk)
    if request.method == 'POST':
        album.delete()
        return redirect(to='list_albums')

    return render(request, "albums/delete_album.html", {"album": album})


def show_artist(request, pk):
    pass