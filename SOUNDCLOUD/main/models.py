from django.db import models
from django.urls import reverse


class Categories(models.Model):
    title = models.CharField(
        max_length=32,
        verbose_name='Название'
    )

    slug = models.SlugField(
        max_length=32,
        verbose_name='слаг',
        unique=True
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('main:category', kwargs={'cat_slug': self.slug})

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['title']


class Music(models.Model):
    title = models.CharField(
        max_length=32,
        verbose_name='Название'
    )

    author = models.CharField(
        max_length=32,
        verbose_name='Автор'
    )

    slug = models.SlugField(
        max_length=32,
        verbose_name='слаг',
        unique=True
    )

    image = models.ImageField(
        upload_to='photos/%Y/%m/%d',
        verbose_name='Постер'
    )

    soundfile = models.FileField(
        upload_to='sound/%Y/%m/%d',
        verbose_name='Трек'
    )

    release = models.DateTimeField(
        verbose_name='Дата выхода'
    )

    cat = models.ForeignKey(
        Categories,
        verbose_name='Категория',
        on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = 'Трек'
        verbose_name_plural = 'Треки'
        ordering = ['title']

    def __str__(self):
        return self.title
