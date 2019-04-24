from rest_framework import serializers
from .models import *

class NewsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = News
        fields = ('mainimg', 'title', 'text', 'file', 'created', 'news_type')



class SportCardSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SportCard
        fields = ('name', 'family', 'photo', 'birthday', 'description')



class AchievmentsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = 'Achievements'
        fields = ('title', 'medal', 'owner')



class EducationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Education
        fields = ('title')



class QualificationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Qualification
        fields = ('title')



class AcademicDegreeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AcademicDegree
        fields = ('title')



class TrenerCardSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TrenerCard
        fields = ('name', 'family', 'patronymic', 'photo', 'education',
        'qualification', 'academic_degree', 'experience')



class MaterialsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Materials
        fields = ('title', 'text', 'file', 'created', 'video_title', 'video',
        'comment')



class VideoAlbumsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = VideoAlbums
        fields = ('title', 'created')



class VideoGalerrySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = VideoGalerry
        fields = ('title', 'created', 'video', 'description', 'album')
