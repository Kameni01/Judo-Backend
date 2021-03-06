from django.db import models
from django.contrib.auth import get_user_model
import PIL
from PIL import Image
from imagekit.models.fields import ImageSpecField
from imagekit.processors import ResizeToFit, Adjust, ResizeToFill

import cv2

def gen_cover(video):
    vidcap = cv2.VideoCapture('media/Main/VideoGallery/{}'.format(video))
    vidcap.set(0, 1000)
    success, image = vidcap.read()
    if success:
        cv2.imwrite("media/Main/VideoGallery/{}.jpg".format(video), image)
        return ("media/Main/VideoGallery/{}.jpg".format(video))




class News(models.Model):
    """Класс новостей"""
    NEWS = 'Новость'
    EVENT = 'Грядущее событие'
    TYPES = ((NEWS, 'Новость',), (EVENT, 'Грядущее событие',) )

    mainimg = models.ImageField(verbose_name='Фото', upload_to='Main/MainImg',
    width_field=None, max_length=256, blank=True, null=True)
    title = models.CharField(verbose_name='Заголовок', max_length=100, db_index=True)
    anons = models.CharField(verbose_name='Краткое содержание', max_length=150,
    null=True, blank=True)
    text = models.TextField(verbose_name='Текст', null=True, blank=True)
    file = models.FileField(verbose_name='Файл', upload_to='Main/files',
    max_length=None, blank=True, null=True)
    created = models.DateField(verbose_name='Дата создания', auto_now_add=True)
    news_type = models.CharField(verbose_name='Вид события', default=NEWS,
    choices=TYPES, max_length=50)

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"
        ordering = ["-id"]

    def __str__(self):
        return self.title



class SportCard(models.Model):
    """Класс карточек спортсменов"""
    unosha = 'unosha'
    student = 'student'
    master = 'master'
    DOSKA = ((unosha,'Призер юношеских соревнований',), (student, 'Призер студенческих соревнований',), (master, 'Мастер спорта',))

    name = models.CharField(verbose_name='Имя', max_length=100)
    family = models.CharField(verbose_name='Фамилия', max_length=100, db_index=True)
    photo = models.ImageField(verbose_name='Фотография спортсмена',
    upload_to='Main/Photos', height_field=None, width_field=None,
    max_length=256, blank=True, null=True)
    status = models.CharField(verbose_name='Сектор доски почета',
    max_length=60, default=master, choices=DOSKA)
    birthday = models.DateField(verbose_name='Дата рождения')
    description = models.TextField(verbose_name='Описание спортсмена')

    class Meta:
        verbose_name = "Карточка спортсмена"
        verbose_name_plural = "Карточки спортсменов"
        ordering = ["-id"]

    def __str__(self):
        return self.family



class Achievements(models.Model):
    """Класс достижений спортсменов"""
    GOLD = 'gold'
    SILVER = 'silver'
    BRONZE = 'bronze'
    MEDALS = ((GOLD, 'Золотая',), (SILVER, 'Серебрянная',), (BRONZE, 'Бронзовая',))

    title = models.CharField(verbose_name='Достижение', max_length=100, db_index=True)
    medal = models.CharField(verbose_name='Вид медали', default=GOLD, choices=MEDALS, max_length=100)
    owner = models.ForeignKey(SportCard, verbose_name='Владелец достижения', on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Достижение"
        verbose_name_plural = "Достижения"
        ordering = ["-id"]

    def __str__(self):
        return self.title



class Education(models.Model):
    """Класс уровней образования тренеров"""
    title = models.CharField(verbose_name='Уровень образования', max_length=150, db_index=True)

    class Meta:
        verbose_name = "Уровень образования"
        verbose_name_plural = "Уровни образования"
        ordering = ["title"]

    def __str__(self):
        return self.title



class Qualification(models.Model):
    """Класс квалификации тренеров"""
    title = models.CharField(verbose_name='Квалификация', max_length=150, db_index=True)

    class Meta:
        verbose_name = "Квалификация"
        verbose_name_plural = "Квалификации"
        ordering = ["title"]

    def __str__(self):
        return self.title



class AcademicDegree(models.Model):
    """Класс ученых степеней тренеров"""
    title = models.CharField(verbose_name='Степень', max_length=150, db_index=True)

    class Meta:
        verbose_name = "Ученая степень"
        verbose_name_plural = "Ученые степени"
        ordering = ["title"]

    def __str__(self):
        return self.title



class TrenerCard(models.Model):
    """Класс карточек тренеров"""
    name = models.CharField(verbose_name='Имя', max_length=100)
    family = models.CharField(verbose_name='Фамилия', max_length=100, db_index=True)
    patronymic = models.CharField(verbose_name='Отчество', max_length=100)
    photo = models.ImageField(verbose_name='Фотография тренера', upload_to='Main/Photos', height_field=None, width_field=None, max_length=256, blank=True, null=True)
    education = models.ForeignKey(Education, verbose_name='Уровень образования', on_delete=models.CASCADE)
    qualification = models.ForeignKey(Qualification, verbose_name='Квалификация', on_delete=models.CASCADE)
    academic_degree = models.ForeignKey(AcademicDegree, verbose_name='Ученая степень', on_delete=models.CASCADE)
    experience = models.IntegerField(verbose_name='Стаж работы тренером')

    class Meta:
        verbose_name = "Карточка тренера"
        verbose_name_plural = "Карточки тренеров"
        ordering = ["-id"]

    def __str__(self):
        return self.family



class Materials(models.Model):
    """Класс статей из учебных материалов"""
    FOR_KIDS = 'Для детей'
    FOR_PARENTES = 'Для родителей'
    OTHER = 'Другое'
    TYPE = ((FOR_KIDS, 'Для детей',), (FOR_PARENTES, 'Для родителей',), (OTHER, 'Другое'))

    title = models.CharField(verbose_name='Название статьи', max_length=100, db_index=True)
    text = models.TextField(verbose_name='Текст', null=True, blank=True)
    file = models.FileField(verbose_name='Файл', upload_to='Main/Materials', max_length=256, blank=True, null=True)
    created = models.DateField(verbose_name='Дата создания статьи', auto_now_add=True)
    video_title = models.CharField(verbose_name='Название видео', max_length=100, null=True, blank=True)
    video = models.FileField(verbose_name='Видео', upload_to='Main/Videos', max_length=256, blank=True, null=True)
    comment = models.CharField(verbose_name='Комментарий', max_length=300, null=True, blank=True)
    type = models.CharField(verbose_name='Для кого статья', default=OTHER, choices=TYPE, max_length=100)

    class Meta:
        verbose_name = "Статья из учебных материалов"
        verbose_name_plural = "Статьи из учебных материалов"
        ordering = ["-id"]

    def __str__(self):
        return self.title



class VideoAlbums(models.Model):
    """Класс альбомов видеогалереи"""
    title = models.CharField(verbose_name='Название альбома', max_length=100, db_index=True)
    created = models.DateField(verbose_name='Дата создание альбома', auto_now_add=True)

    class Meta:
        verbose_name = "Альбом видое"
        verbose_name_plural = "Альбомы видео"
        ordering = ["-id"]

    def __str__(self):
        return self.title



class VideoGallery(models.Model):
    title = models.CharField(verbose_name='Название видео', max_length=100,
    db_index=True)
    created = models.DateField(verbose_name='Дата добавления видео',
    auto_now_add=True)
    video = models.FileField(verbose_name='Видео',
    upload_to='Main/VideoGallery', max_length=256, null=True, blank=True)
    cover = models.ImageField(verbose_name='Превью', upload_to='Main/covers',
    height_field=None, width_field=None, max_length=256, blank=True, null=True)
    descriptions = models.TextField(verbose_name='Описание видео',
    null=True, blank=True)
    album = models.ForeignKey(VideoAlbums, verbose_name='Альбом',
    null=True, blank=True, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Видеозапись"
        verbose_name_plural = "Видеозаписи"
        ordering = ["-id"]

    def save(self, *args, **kwargs):
        if self.video:
            self.cover = gen_cover(self.video)
            print(gen_cover(self.video))
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title



class PhotoAlbums(models.Model):
    """Класс альбомов видеогалереи"""
    title = models.CharField(verbose_name='Название альбома', max_length=100, db_index=True)
    created = models.DateField(verbose_name='Дата создание альбома', auto_now_add=True)

    class Meta:
        verbose_name = "Фотоальбом"
        verbose_name_plural = "Фотоальбомы"
        ordering = ["-id"]

    def __str__(self):
        return self.title



class PhotoGallery(models.Model):
    title = models.CharField(verbose_name='Название фото', max_length=100,
    db_index=True)
    created = models.DateField(verbose_name='Дата добавления фото', auto_now_add=True)
    photo = models.ImageField(verbose_name='Фото', upload_to='Main/PhotoGallery',
    height_field=None, width_field=None, max_length=256, blank=True, null=True)
    photo_s = ImageSpecField([Adjust(contrast=1.0, sharpness=1.0),
            ResizeToFill(350, 170)], source='photo',
            format='JPEG', options={'quality': 100})
    descriptions = models.TextField(verbose_name='Описание фото', null=True,
    blank=True)
    album = models.ForeignKey(PhotoAlbums, verbose_name='Альбом', null=True,
    blank=True, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Фотография"
        verbose_name_plural = "Фотографии"
        ordering = ["-id"]


    def save(self, *args, **kwargs):

        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
