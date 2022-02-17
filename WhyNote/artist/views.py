from django.shortcuts import render

from .models import Artist

def artist_list(request):
    artist_info = Artist.objects.all()

    return render(request, 'artist/artist_list.html', {'artist': artist_info})

def artist_page(request, artist_name):
    artist_info = Artist.objects.get(name_artist=artist_name)

    return render(request, 'artist/artist_page.html', {'artist_info': artist_info})