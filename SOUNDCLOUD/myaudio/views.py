from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from django.views.generic import ListView

from .models import *
from .utils import *


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
    context = {'my_music': my_music,
               'menu': menu,
               'cats': cats,
               'title': "Мои аудиозаписи"
               }
    return render(request, 'myaudio/myaudio.html', context)
