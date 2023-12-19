from django.contrib.auth.views import LogoutView, PasswordChangeView, PasswordChangeDoneView, PasswordResetView, \
    PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from django.urls import path
from .views import *

app_name = 'register'
urlpatterns = [
    path('', LoginUser.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('password-change/', UserChangePassword.as_view(), name='password_change'),
    path('password-reset/', PasswordResetView.as_view(
        template_name='register/password_reset_form.html',
        email_template_name='register/password_reset_email.html',
        success_url=reverse_lazy('register:password_reset_done')),
         name='password_reset'),
    path('password-reset-done/', PasswordResetDoneView.as_view(
        template_name='register/password_reset_done.html'),
         name='password_reset_done'),
    path('password-reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(
        template_name='register/password_reset_confirm.html',
        success_url=reverse_lazy('register:login')),
         name='password_reset_confirm'),
    path('password-reset-complete/', PasswordResetCompleteView.as_view(
        template_name='register/password_reset_complete.html'),
         name='password_reset_complete'),
    path('register/', RegisterUser.as_view(), name='reg'),
    path('profile/', Profile.as_view(), name='profile'),
]