from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from .models import *
from .forms import *
from .utils import *


class MusicHome(DataMixin, ListView):
    model = Music
    template_name = 'main/index.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context2 = self.get_user_context(title='Главная страница')
        return context | context2


class ListCategories(DataMixin, ListView):
    model = Music
    template_name = 'main/index.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context2 = self.get_user_context(title=context['posts'][0].cat)
        return context | context2

    def get_queryset(self):
        return Music.objects.filter(cat__slug=self.kwargs['cat_slug'])


class AddMusic(DataMixin, LoginRequiredMixin, CreateView):
    form_class = AddMusicForm
    template_name = 'main/addmusic.html'
    success_url = reverse_lazy('main:home')
    login_url = 'register:login'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context2 = self.get_user_context(title='Добавление трека')
        return context | context2



