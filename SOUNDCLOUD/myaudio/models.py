from django.contrib.auth import get_user_model
from django.db import models
from main.models import Music


class MyMusic(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    music = models.ForeignKey(Music, on_delete=models.CASCADE, related_name='my_music')

    def __str__(self):
        return f'Избраное для пользователя {self.user.username}'