from django.contrib.auth.models import User
from django.db import models
from main.models import Music


class MyMusic(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    music = models.ForeignKey(Music, on_delete=models.CASCADE, related_name='my_music')

    def __str__(self):
        return f'Избраное для пользователя {self.user.username}'