# Generated by Django 4.2.7 on 2023-12-19 19:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32, verbose_name='Название')),
                ('slug', models.SlugField(max_length=32, unique=True, verbose_name='слаг')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Music',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32, verbose_name='Название')),
                ('author', models.CharField(max_length=32, verbose_name='Автор')),
                ('slug', models.SlugField(blank=True, max_length=32, unique=True, verbose_name='слаг')),
                ('image', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d', verbose_name='Постер')),
                ('soundfile', models.FileField(blank=True, db_index=True, upload_to='sound/%Y/%m/%d', verbose_name='Трек')),
                ('cat', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='main.categories', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Трек',
                'verbose_name_plural': 'Треки',
                'ordering': ['title'],
            },
        ),
    ]
