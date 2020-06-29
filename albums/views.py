from django.shortcuts import render, redirect, get_object_or_404
# from django.core.exceptions import ObjectDoesNotExist
from .models import Album, Artist
from .forms import AlbumForm, ArtistForm
from django.db.models import Q

# Create your views here.
def list_albums(request):
    albums = Album.objects.order_by("-id")
    return render(request, "albums/list_albums.html", { "albums" : albums})

def list_albums_year(request):
    albums = Album.objects.order_by('release_year', 'artist_string', 'title')
    return render(request, "albums/list_albums.html", { "albums" : albums})

def list_albums_artist(request):
    albums = Album.objects.order_by('artist_string', 'release_year', 'title')
    return render(request, "albums/list_albums.html", { "albums" : albums})

def list_albums_title(request):
    albums = Album.objects.order_by('title', 'artist_string', 'release_year')
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

def delete_album(request, pk):
    album = get_object_or_404(Album, pk=pk)
    if request.method == 'POST':
        album.delete()
        return redirect(to='list_albums')

    return render(request, "albums/delete_album.html", {"album": album})

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
    
def show_album(request, pk):
    album = get_object_or_404(Album, pk=pk)
    artist = album.artist
    return render(request, "albums/show_album.html", { "album" : album, "artist" : artist })

def show_artist(request, pk):
    artist = get_object_or_404(Artist, pk=pk)
    return render(request, "albums/show_artist.html", { "artist" : artist})

def search_albums(request):
    query = request.GET.get('search_string')
    albums = Album.objects.filter(Q(title__icontains=query) | Q(artist_string__icontains=query))
    return render(request, "albums/list_albums.html", {"albums" : albums})

def add_fave_list(request, pk):
    album = get_object_or_404(Album, pk=pk)
    new_fave = album.favorite
    album.favorite = not new_fave
    album.save()
    return redirect(to='list_albums')


def add_fave_album(request, pk):
    album = get_object_or_404(Album, pk=pk)
    new_fave = album.favorite
    album.favorite = not new_fave
    album.save()
    return redirect(to='show_album', pk=pk)

def add_fave_artist(request, album_pk):
    pass