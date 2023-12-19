from django.contrib.auth import logout, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from .forms import *
from .utils import *


class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUser
    template_name = 'register/reg.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context2 = self.get_user_context(title='Регистрация')
        return context | context2

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('main:home')


class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'register/login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context2 = self.get_user_context(title='Войти')
        return context | context2


class Profile(DataMixin, LoginRequiredMixin, UpdateView):
    model = get_user_model()
    form_class = ProfileForm
    template_name = 'register/profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context2 = self.get_user_context(title='Профиль')
        return context | context2

    def get_success_url(self):
        return reverse_lazy('main:home')

    def get_object(self, queryset=None):
        return self.request.user


class UserChangePassword(PasswordChangeView):
    form_class = UserChangePasswordForm
    success_url = reverse_lazy("register:profile")
    template_name = "register/password_change_form.html"
