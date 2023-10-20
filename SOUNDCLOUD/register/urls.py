from django.urls import path
from .views import *

app_name = 'register'
urlpatterns = [
    path('', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', RegisterUser.as_view(), name='reg')
]