from django.shortcuts import render, redirect
from django.http import HttpResponse, request
from .models import Album, Song

from pygame import mixer

from django.urls import reverse
from urllib.parse import urlencode
# Create your views here.

albums = Album.objects.all()
songs = Song.objects.all()


def home(request):
    id = request.GET.get('id')
    current = request.GET.get('current')

    return render(request, "home.html", {'id': id, 'current': current, 'albums': albums, 'songs': songs})


def play(request, song_id):

    if(mixer.get_init() == None):
        mixer.init()

    song = Song.objects.filter(id=song_id)[0]
    song_path = song.song_file.url[1:]
    mixer.music.load(song_path)
    mixer.music.play()
    print("playing "+str(song.song_name))
    current = "play"
    base_url = reverse('home')
    query_string = urlencode({'id': song_id, 'current': current})
    url = '{}?{}'.format(base_url, query_string)
    return redirect(url)


def pause(request, song_id):

    if (mixer.get_init() != None):
        mixer.music.pause()
        current = "pause"
        base_url = reverse('home')
        query_string = urlencode({'id': song_id, 'current': current})
        url = '{}?{}'.format(base_url, query_string)
        return redirect(url)

    current = play
    base_url = reverse('home')
    query_string = urlencode({'id': song_id, 'current': current})
    url = '{}?{}'.format(base_url, query_string)
    return redirect(url)
