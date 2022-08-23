from django.shortcuts import render
from .models import Album

# Create your views here.
def album_list(request):
    albums = Album.objects.all()
    return render(request, 'albums/album_list.html', {'albums': albums})