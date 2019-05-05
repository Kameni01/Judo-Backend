# Generated by Django 2.1.4 on 2019-04-26 20:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0009_auto_20190426_2313'),
    ]

    operations = [
        migrations.CreateModel(
            name='PhotoAlbums',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=100, verbose_name='Название альбома')),
                ('created', models.DateField(auto_now_add=True, verbose_name='Дата создание альбома')),
            ],
            options={
                'verbose_name': 'Фотоальбом',
                'verbose_name_plural': 'Фотоальбомы',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='PhotoGallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=100, verbose_name='Название фото')),
                ('created', models.DateField(auto_now_add=True, verbose_name='Дата добавления фото')),
                ('photo', models.ImageField(blank=True, max_length=256, null=True, upload_to='Main/PhotoGallery', verbose_name='Фото')),
                ('descriptions', models.TextField(blank=True, null=True, verbose_name='Описание фото')),
                ('album', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Main.PhotoAlbums', verbose_name='Альбом')),
            ],
            options={
                'verbose_name': 'Фотография',
                'verbose_name_plural': 'Фотографии',
                'ordering': ['-id'],
            },
        ),
        migrations.AlterField(
            model_name='news',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='Main/files', verbose_name='Файл'),
        ),
    ]
