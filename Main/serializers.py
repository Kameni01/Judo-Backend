from rest_framework import serializers
from .models import *



class NewsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ('id', 'mainimg', 'title', 'anons', 'created', 'news_type')



class NewsFullSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ('id', 'mainimg', 'title', 'text', 'file', 'created', 'news_type')



class SportCardListSerializer(serializers.ModelSerializer):
    class Meta:
        model = SportCard
        fields = ('id', 'name', 'family', 'photo')


#Dobavit suda dostigheniya!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
class SportCardFullSerializer(serializers.ModelSerializer):
    class Meta:
        model = SportCard
        fields = ('id', 'name', 'family', 'photo', 'birthday', 'description')



class AchievementsFullSerializer(serializers.ModelSerializer):
    class Meta:
        model = Achievements
        fields = ('id', 'title', 'medal', 'owner')



class TrenerCardListSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrenerCard
        fields = ('id', 'name', 'family', 'patronymic', 'photo')



class TrenerCardFullSerializer(serializers.Serializer):
    id = serializers.IntegerField(label='ID', read_only=True)
    name = serializers.CharField(required=False, allow_blank=True, max_length=100)
    family = serializers.CharField(required=False, allow_blank=True, max_length=100)
    patronymic = serializers.CharField(required=False, allow_blank=True, max_length=100)
    photo = serializers.ImageField(allow_null=True, label='Фотография тренера', max_length=256, required=False)
    education = serializers.CharField(required=False, allow_blank=True, max_length=100)
    qualification = serializers.CharField(required=False, allow_blank=True, max_length=100)
    academic_degree = serializers.CharField(required=False, allow_blank=True, max_length=100)
    experience = serializers.IntegerField(max_value=None, min_value=None)



class MaterialsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Materials
        fields = ('id', 'title')



class MaterialsFullSerializer(serializers.ModelSerializer):
    class Meta:
        model = Materials
        fields = ('id', 'title', 'text', 'file', 'created', 'video_title',
        'video', 'comment', 'type')



class VideoAlbumsFullSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoAlbums
        fields = ('id', 'title', 'created')



class VideoGalerryFullSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(label='ID', read_only=True)
    title = serializers.CharField(required=False, allow_blank=True, max_length=100)
    description = serializers.CharField(required=False, allow_blank=True, max_length=1000)
    album = serializers.CharField(required=False, allow_blank=True, max_length=100)
    class Meta:
        model = VideoGalerry
        fields = ('id', 'title', 'video', 'description', 'album')
