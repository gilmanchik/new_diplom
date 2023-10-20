from django.contrib.auth import logout, login
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import *
from main.models import *


class RegisterUser(CreateView):
    form_class = RegisterUser
    template_name = 'register/reg.html'
    success_url = reverse_lazy('register:login')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Регистрация'
        context['cats'] = Categories.objects.all()
        return context

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('main:home')


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'register/login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Авторизация'
        context['cats'] = Categories.objects.all()
        return context

    def get_success_url(self):
        return reverse_lazy('main:home')


def logout_user(request):
    logout(request)
    return redirect('main:home')
