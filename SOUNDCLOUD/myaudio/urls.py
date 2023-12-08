from django.urls import path

from .views import *

app_name = 'myaudio'
urlpatterns = [
    path('add/<int:music_id>/', music_add, name='music_add'),
    path('remove/<int:music_id>/', music_remove, name='music_remove'),
    path('my_aupiolist/', my_music_list, name='myaudiolist'),
]
