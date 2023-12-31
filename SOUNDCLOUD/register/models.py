from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    image = models.ImageField(upload_to='users', blank=True, null=True, verbose_name='Фотография')
    day_birth = models.DateTimeField(blank=True, null=True, verbose_name='День рождения')