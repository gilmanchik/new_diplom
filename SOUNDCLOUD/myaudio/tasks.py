from django.shortcuts import redirect
from django.views.decorators.http import require_POST

from main.models import Music
from myaudio.models import MyMusic


@require_POST
def music_add(request, music_id):
    music = Music.objects.get(id=music_id)
    my_music = MyMusic.objects.filter(user=request.user, music=music)

    if not my_music.exists():
        MyMusic.objects.create(user=request.user, music=music)
    else:
        pass
    return redirect(request.META['HTTP_REFERER'])


@require_POST
def music_remove(request, music_id):
    music = Music.objects.get(id=music_id)
    MyMusic.objects.filter(user=request.user, music=music).delete()
    return redirect(request.META['HTTP_REFERER'])
