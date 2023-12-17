# Generated by Django 4.2.7 on 2023-12-14 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_music_cat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='music',
            name='image',
            field=models.ImageField(blank=True, upload_to='photos/%Y/%m/%d', verbose_name='Постер'),
        ),
        migrations.AlterField(
            model_name='music',
            name='soundfile',
            field=models.FileField(blank=True, upload_to='sound/%Y/%m/%d', verbose_name='Трек'),
        ),
    ]
