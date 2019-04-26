# Generated by Django 2.1.4 on 2019-04-25 11:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AcademicDegree',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=150, verbose_name='Степень')),
            ],
            options={
                'verbose_name': 'Ученая степень',
                'verbose_name_plural': 'Ученые степени',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Achievements',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=100, verbose_name='Заголовок')),
                ('medal', models.IntegerField(choices=[(0, 'Золотая'), (1, 'Серебрянная'), (2, 'Бронзовая')], default=0, verbose_name='Вид медали')),
            ],
            options={
                'verbose_name': 'Достижение',
                'verbose_name_plural': 'Достижения',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=150, verbose_name='Уровень образования')),
            ],
            options={
                'verbose_name': 'Уровень образования',
                'verbose_name_plural': 'Уровни образования',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Materials',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=100, verbose_name='Название статьи')),
                ('text', models.TextField(blank=True, null=True, verbose_name='Текст')),
                ('file', models.FileField(blank=True, max_length=256, null=True, upload_to='Main/Materials', verbose_name='Файл')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания статьи')),
                ('video_title', models.CharField(blank=True, max_length=100, null=True, verbose_name='Заголовок')),
                ('video', models.FileField(blank=True, max_length=256, null=True, upload_to='Main/Videos', verbose_name='Видео')),
                ('comment', models.CharField(blank=True, max_length=300, null=True, verbose_name='Заголовок')),
            ],
            options={
                'verbose_name': 'Статья из учебных материалов',
                'verbose_name_plural': 'Статьи из учебных материалов',
                'ordering': ['created'],
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mainimg', models.ImageField(blank=True, max_length=256, null=True, upload_to='Main/MainImg', verbose_name='Фото')),
                ('title', models.CharField(db_index=True, max_length=100, verbose_name='Заголовок')),
                ('text', models.TextField(blank=True, null=True, verbose_name='Текст')),
                ('file', models.FileField(blank=True, max_length=256, null=True, upload_to='Main/files', verbose_name='Файл')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('news_type', models.IntegerField(choices=[(0, 'Новость'), (1, 'Грядущее событие')], default=0, verbose_name='Вид события')),
            ],
            options={
                'verbose_name': 'Новость',
                'verbose_name_plural': 'Новости',
                'ordering': ['created'],
            },
        ),
        migrations.CreateModel(
            name='Qualification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=150, verbose_name='Квалификация')),
            ],
            options={
                'verbose_name': 'Квалификация',
                'verbose_name_plural': 'Квалификации',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='SportCard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Имя')),
                ('family', models.CharField(db_index=True, max_length=100, verbose_name='Фамилия')),
                ('photo', models.ImageField(blank=True, max_length=256, null=True, upload_to='Main/Photos', verbose_name='Фотография спортсмена')),
                ('birthday', models.DateField(verbose_name='Дата рождения')),
                ('description', models.TextField(verbose_name='Описание спортсмена')),
            ],
            options={
                'verbose_name': 'Карточка спортсмена',
                'verbose_name_plural': 'Карточки спортсменов',
                'ordering': ['family'],
            },
        ),
        migrations.CreateModel(
            name='TrenerCard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Имя')),
                ('family', models.CharField(db_index=True, max_length=100, verbose_name='Фамилия')),
                ('patronymic', models.CharField(max_length=100, verbose_name='Отчество')),
                ('photo', models.ImageField(blank=True, max_length=256, null=True, upload_to='Main/Photos', verbose_name='Фотография тренера')),
                ('experience', models.IntegerField(max_length=2, verbose_name='Стаж работы тренером')),
                ('academic_degree', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Main.AcademicDegree', verbose_name='Ученая степень')),
                ('education', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Main.Education', verbose_name='Уровень образования')),
                ('qualification', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Main.Qualification', verbose_name='Квалификация')),
            ],
            options={
                'verbose_name': 'Карточка тренера',
                'verbose_name_plural': 'Карточки тренеров',
                'ordering': ['family'],
            },
        ),
        migrations.CreateModel(
            name='VideoAlbums',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=100, verbose_name='Название альбома')),
                ('created', models.DateField(auto_now_add=True, verbose_name='Дата создание альбома')),
            ],
            options={
                'verbose_name': 'Альбом видое',
                'verbose_name_plural': 'Альбомы видео',
                'ordering': ['created'],
            },
        ),
        migrations.CreateModel(
            name='VideoGalerry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=100, verbose_name='Название видео')),
                ('created', models.DateField(auto_now_add=True, verbose_name='Дата добавления видео')),
                ('video', models.FileField(max_length=256, upload_to='Main/VideoGallery', verbose_name='Видео')),
                ('descriptions', models.TextField(blank=True, null=True, verbose_name='Описание видео')),
                ('album', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Main.VideoAlbums', verbose_name='Альбом')),
            ],
            options={
                'verbose_name': 'Видеозапись',
                'verbose_name_plural': 'Видеозаписи',
                'ordering': ['created'],
            },
        ),
        migrations.AddField(
            model_name='achievements',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Main.SportCard', verbose_name='Владелец достижения'),
        ),
    ]