# Generated by Django 4.2.7 on 2023-12-07 17:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0001_initial'),
        ('myaudio', '0002_mymusic_delete_myaudio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mymusic',
            name='music',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='my_music', to='main.music', unique=True),
        ),
        migrations.AlterField(
            model_name='mymusic',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]