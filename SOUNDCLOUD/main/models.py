from django.db import models
from django.urls import reverse
from django.utils.text import slugify


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
        unique=True,
        blank=True
    )

    image = models.ImageField(
        upload_to='photos/%Y/%m/%d',
        verbose_name='Постер',
        blank=True
    )

    soundfile = models.FileField(
        upload_to='sound/%Y/%m/%d',
        verbose_name='Трек',
        blank=True
    )

    cat = models.ForeignKey(
        Categories,
        verbose_name='Категория',
        on_delete=models.CASCADE,
        blank=True
    )

    class Meta:
        verbose_name = 'Трек'
        verbose_name_plural = 'Треки'
        ordering = ['title']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        print('!!!------!!!!')
        super(Music, self).save(*args, **kwargs)
        if not self.slug:
            self.slug = slugify(self.title) + f'{self.author}' + f'{self.pk}'
            super().save(*args, **kwargs)
