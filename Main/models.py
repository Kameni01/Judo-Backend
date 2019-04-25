from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

User = get_user_model()


class News(models.Model):
    """Класс новостей"""
    NEWS = 0
    EVENT = 1
    TYPES = ((NEWS, 'Новость',), (EVENT, 'Грядущее событие',) )

    mainimg = models.ImageField(verbose_name='Фото', upload_to='Main/MainImg', height_field=None, width_field=None, max_length=256, blank=True, null=True)
    title = models.CharField(verbose_name='Заголовок', max_length=100, db_index=True)
    text = models.TextField(verbose_name='Текст', null=True, blank=True)
    file = models.FileField(verbose_name='Файл', upload_to='Main/files', max_length=256, blank=True, null=True)
    created = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    news_type = models.IntegerField(verbose_name='Вид события', default=NEWS, choices=TYPES)

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"
        ordering = ["created"]

    def __str__(self):
        return self.title



class SportCard(models.Model):
    """Класс карточек спортсменов"""
    name = models.CharField(verbose_name='Имя', max_length=100)
    family = models.CharField(verbose_name='Фамилия', max_length=100, db_index=True)
    photo = models.ImageField(verbose_name='Фотография спортсмена', upload_to='Main/Photos', height_field=None, width_field=None, max_length=256, blank=True, null=True)
    birthday = models.DateField(verbose_name='Дата рождения')
    description = models.TextField(verbose_name='Описание спортсмена')

    class Meta:
        verbose_name = "Карточка спортсмена"
        verbose_name_plural = "Карточки спортсменов"
        ordering = ["family"]

    def __str__(self):
        return self.family



class Achievements(models.Model):
    """Класс достижений спортсменов"""
    GOLD = 0
    SILVER = 1
    BRONZE = 2
    MEDALS = ((GOLD, 'Золотая',), (SILVER, 'Серебрянная',), (BRONZE, 'Бронзовая',))

    title = models.CharField(verbose_name='Заголовок', max_length=100, db_index=True)
    medal = models.IntegerField(verbose_name='Вид медали', default=GOLD, choices=MEDALS)
    owner = models.ForeignKey(SportCard, verbose_name='Владелец достижения', on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Достижение"
        verbose_name_plural = "Достижения"
        ordering = ["title"]

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
        ordering = ["family"]

    def __str__(self):
        return self.title



class Materials(models.Model):
    """Класс статей из учебных материалов"""
    title = models.CharField(verbose_name='Название статьи', max_length=100, db_index=True)
    text = models.TextField(verbose_name='Текст', null=True, blank=True)
    file = models.FileField(verbose_name='Файл', upload_to='Main/Materials', max_length=256, blank=True, null=True)
    created = models.DateTimeField(verbose_name='Дата создания статьи', auto_now_add=True)
    video_title = models.CharField(verbose_name='Заголовок', max_length=100, null=True, blank=True)
    video = models.FileField(verbose_name='Видео', upload_to='Main/Videos', max_length=256, blank=True, null=True)
    comment = models.CharField(verbose_name='Заголовок', max_length=300, null=True, blank=True)

    class Meta:
        verbose_name = "Статья из учебных материалов"
        verbose_name_plural = "Статьи из учебных материалов"
        ordering = ["created"]

    def __str__(self):
        return self.title



class VideoAlbums(models.Model):
    """Класс альбомов видеогалереи"""
    title = models.CharField(verbose_name='Название альбома', max_length=100, db_index=True)
    created = models.DateField(verbose_name='Дата создание альбома', auto_now_add=True)

    class Meta:
        verbose_name = "Альбом видое"
        verbose_name_plural = "Альбомы видео"
        ordering = ["created"]

    def __str__(self):
        return self.title



class VideoGalerry(models.Model):
    title = models.CharField(verbose_name='Название видео', max_length=100, db_index=True)
    created = models.DateField(verbose_name='Дата добавления видео', auto_now_add=True)
    video = models.FileField(verbose_name='Видео', upload_to='Main/VideoGallery', max_length=256)
    descriptions = models.TextField(verbose_name='Описание видео', null=True, blank=True)
    album = models.ForeignKey(VideoAlbums, verbose_name='Альбом', null=True, blank=True, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Видеозапись"
        verbose_name_plural = "Видеозаписи"
        ordering = ["created"]

    def __str__(self):
        return self.title
