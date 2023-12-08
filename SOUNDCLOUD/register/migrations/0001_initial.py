# Generated by Django 4.2.7 on 2023-12-06 17:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyMusic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('music', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='my_music', to='main.music')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_my_music', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]