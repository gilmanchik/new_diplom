from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from django.views.generic import ListView

from .models import *
from .utils import *


@require_POST
def music_add(request, music_id):
    music = Music.objects.get(id=music_id)

    if music not in MyMusic.objects.filter(user=request.user):
        MyMusic.objects.create(user=request.user, music=music)
    else:
        return None
    return redirect(request.META['HTTP_REFERER'])


@require_POST
def music_remove(request, music_id):
    music = Music.objects.get(id=music_id)
    MyMusic.objects.filter(user=request.user, music=music).delete()
    return redirect(request.META['HTTP_REFERER'])


# class MyAudioList(DataMixin, ListView):
#     model = MyMusic
#     template_name = 'myaudio/myaudio.html'
#     context_object_name = 'myaudio'
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context2 = self.get_user_context(title="Мои аудиозаписи")
#         return context | context2

@login_required
def my_music_list(request):
    my_music = MyMusic.objects.filter(user=request.user)
    menu = [
        {'title': 'Главная страница', 'url_name': 'main:home'},
        {'title': 'Добавить трек', 'url_name': 'main:add'}
    ]
    cats = Categories.objects.all()
    return render(request, 'myaudio/myaudio.html', {'my_music': my_music, 'menu': menu, 'cats': cats})