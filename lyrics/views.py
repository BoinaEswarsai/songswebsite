from django.shortcuts import render
from django.http import JsonResponse
from .models import Song

def home(request):
    return render(request, "index.html")

def song_list(request):
    songs = Song.objects.all().values("id", "title")
    return JsonResponse(list(songs), safe=False)

def song_detail(request, song_id):   # must match urls.py
    try:
        song = Song.objects.get(id=song_id)
        return JsonResponse({
            "id": song.id,
            "title": song.title,
            "lyrics": song.lyrics
        })
    except Song.DoesNotExist:
        return JsonResponse({"error": "Song not found"}, status=404)
