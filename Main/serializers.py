from rest_framework import serializers
from django.conf import settings
from .models import *
from rest_framework.settings import api_settings


class NewsListSerializer(serializers.ModelSerializer):
    # created = serializers.DateField(input_formats=None, format='%d %B %Y')
    # created = serializers.DateField(input_formats=None, format='%d-%m-%Y')
    class Meta:
        model = News
        fields = ('id', 'mainimg', 'title', 'anons', 'created', 'news_type')



class NewsFullSerializer(serializers.ModelSerializer):
    # created = serializers.DateField(input_formats=None, format='%d-%m-%Y')
    class Meta:
        model = News
        fields = ('id', 'mainimg', 'title', 'text', 'file', 'created', 'news_type')



class SportCardListSerializer(serializers.ModelSerializer):
    class Meta:
        model = SportCard
        fields = ('id', 'name', 'family', 'photo', 'status')



class SportCardListDoskaSerializer(serializers.ModelSerializer):
    class Meta:
        model = SportCard
        fields = ('id', 'name', 'family', 'photo', 'status')



class SportCardFullSerializer(serializers.ModelSerializer):
    class Meta:
        model = SportCard
        fields = ('id', 'name', 'family', 'photo', 'birthday', 'description')



class AchievementsFull_v2Serializer(serializers.ModelSerializer):
    class Meta:
        model = Achievements
        fields = ('id', 'title', 'medal')



class AchievementsFullSerializer(serializers.ModelSerializer):
    class Meta:
        model = Achievements
        fields = ('id', 'title', 'medal', 'owner')



class TrenerCardListSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrenerCard
        fields = ('id', 'name', 'family', 'patronymic', 'photo')



class TrenerCardFirstSerializer(serializers.Serializer):
    id = serializers.IntegerField(label='ID', read_only=True)
    name = serializers.CharField(required=False, allow_blank=True, max_length=100)
    family = serializers.CharField(required=False, allow_blank=True, max_length=100)
    patronymic = serializers.CharField(required=False, allow_blank=True, max_length=100)
    photo = serializers.ImageField(allow_null=True, label='Фотография тренера', max_length=256, required=False)

class TrenerCardSecondSerializer(serializers.Serializer):
    education = serializers.CharField(required=False, allow_blank=True, max_length=100)
    qualification = serializers.CharField(required=False, allow_blank=True, max_length=100)
    academic_degree = serializers.CharField(required=False, allow_blank=True, max_length=100)
    experience = serializers.IntegerField(max_value=None, min_value=None)



class MaterialsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Materials
        fields = ('id', 'title')



class MaterialsFullSerializer(serializers.ModelSerializer):
    # created = serializers.DateField(input_formats=None, format='%d-%m-%Y')
    class Meta:
        model = Materials
        fields = ('id', 'title', 'text', 'file', 'created', 'video_title',
        'video', 'comment', 'type')



class VideoAlbumsFullSerializer(serializers.ModelSerializer):
    # created = serializers.DateField(input_formats=None, format='%d-%m-%Y')
    class Meta:
        model = VideoAlbums
        fields = ('id', 'title', 'created')


class VideoAlbumsShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoAlbums
        fields = ('id', )



class VideoGalleryShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoGallery
        fields = ('id', 'title', 'video', 'cover')



class VideoGalleryFull_v2Serializer(serializers.ModelSerializer):
    class Meta:
        model = VideoGallery
        fields = ('id', 'title', 'video', 'descriptions')



class PhotoAlbumsFullSerializer(serializers.ModelSerializer):
    # created = serializers.DateField(input_formats=None, format='%d-%m-%Y')
    class Meta:
        model = VideoAlbums
        fields = ('id', 'title', 'created')



class PhotoGalleryFull_v2Serializer(serializers.ModelSerializer):
    photo_s = serializers.ImageField(allow_null=True, max_length=256, required=False)
    class Meta:
        model = PhotoGallery
        fields = ('id', 'photo', 'photo_s', 'descriptions')



class PhotoGalleryForAlbumSerializer(serializers.ModelSerializer):
    photo_s = serializers.ImageField(allow_null=True, max_length=256, required=False)
    class Meta:
        model = PhotoGallery
        fields = ('id', 'photo_s')
