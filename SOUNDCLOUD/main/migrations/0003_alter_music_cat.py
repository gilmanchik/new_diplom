# Generated by Django 4.2.7 on 2023-12-10 07:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_remove_music_release_alter_music_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='music',
            name='cat',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='main.categories', verbose_name='Категория'),
        ),
    ]
