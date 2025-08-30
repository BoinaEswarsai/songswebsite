from django.http import JsonResponse
from .models import Song

def song_list(request):
    songs = Song.objects.all().values("id", "title")
    return JsonResponse(list(songs), safe=False)

def song_detail(request, song_id):
    song = Song.objects.get(id=song_id)
    return JsonResponse({"title": song.title, "lyrics": song.lyrics})
from django.shortcuts import render

def home(request):
    return render(request, "index.html")
