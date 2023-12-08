from django.urls import path
from .views import *

app_name = 'main'
urlpatterns = [
    path('', MusicHome.as_view(), name='home'),
    path('add/', AddMusic.as_view(), name='add'),
    path('category/<slug:cat_slug>/', ListCategories.as_view(), name='category')
]
