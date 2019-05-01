from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from rest_framework.response import Response

from .serializers import *
from .models import *

from django.http import Http404
from rest_framework.views import APIView
from rest_framework import status



class NewsList(APIView):
    def get(self, request, format=None):
        obj = News.objects.all()
        serializer = NewsListSerializer(obj, many=True)
        return Response(serializer.data)



class NewsDetail(APIView):
    def get_object(self, id):
        try:
            return News.objects.get(id=id)
        except News.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        obj = self.get_object(id)
        serializer = NewsFullSerializer(obj)
        return Response(serializer.data)



class NewsNEWS(APIView):
    def get(self, request, format=None):
        obj = News.objects.filter(news_type='Новость')
        serializer = NewsListSerializer(obj, many=True)
        return Response(serializer.data)



class NewsEVENTS(APIView):
    def get(self, request, format=None):
        obj = News.objects.filter(news_type='Грядущее событие')
        serializer = NewsListSerializer(obj, many=True)
        return Response(serializer.data)



class SportCardList(APIView):
    def get(self, request, format=None):
        obj = SportCard.objects.all()
        serializer = SportCardListSerializer(obj, many=True)
        return Response(serializer.data)



class SportCardDetail(APIView):
    def get_object(self, id):
        try:
            return SportCard.objects.get(id=id)
        except SportCard.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        obj = self.get_object(id)
        serializer = SportCardFullSerializer(obj)
        return Response(serializer.data)

class SportCardDetail_v2(APIView):
    def get_object(self, id):
        try:
            return SportCard.objects.get(id=id)
        except SportCard.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        achievs = Achievements.objects.filter(owner_id=id)
        achiev_ser = AchievementsFull_v2Serializer(achievs, many=True)
        obj = self.get_object(id)
        serializer = SportCardFullSerializer(obj)
        data = {}
        data.update(serializer.data)
        data['medals'] = []
        for element in achiev_ser.data:
            data['medals'].append(element)
        return Response(data)



class AchievementsDetail(APIView):
    def get_object(self, id):
        try:
            return Achievements.objects.filter(owner_id=id)
        except Achievements.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        obj = self.get_object(id)
        serializer = AchievementsFullSerializer(obj, many=True)
        return Response(serializer.data)



class TrenerCardList(APIView):
    def get(self, request, format=None):
        obj = TrenerCard.objects.all()
        serializer = TrenerCardListSerializer(obj, many=True)
        return Response(serializer.data)



class TrenerCardDetail(APIView):
    def get_object(self, id):
        try:
            return TrenerCard.objects.get(id=id)
        except TrenerCard.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        obj = self.get_object(id)
        serializer_1 = TrenerCardFirstSerializer(obj)
        serializer_2 = TrenerCardSecondSerializer(obj)
        data = {}
        data.update(serializer_1.data)
        data['info'] = {}
        data['info'].update(serializer_2.data)
        return Response(data)



class MaterialsList(APIView):
    def get(self, request, format=None):
        obj = Materials.objects.all()
        serializer = MaterialsListSerializer(obj, many=True)
        return Response(serializer.data)



class MaterialsDetail(APIView):
    def get_object(self, id):
        try:
            return Materials.objects.get(id=id)
        except Materials.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        obj = self.get_object(id)
        serializer = MaterialsFullSerializer(obj)
        return Response(serializer.data)



class VideoAlbumsList(APIView):
    def get(self, request, format=None):
        obj = VideoAlbums.objects.all()
        serializer = VideoAlbumsFullSerializer(obj, many=True)
        return Response(serializer.data)



class VideoAlbumsDetail(APIView):
    def get_object(self, id):
        try:
            return VideoAlbums.objects.get(id=id)
        except VideoAlbums.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        obj = self.get_object(id)
        serializer = VideoAlbumsFullSerializer(obj)
        return Response(serializer.data)



class VideoAlbumsItems(APIView):
    def get_album(self, id):
        try:
            return VideoAlbums.objects.get(id=id)
        except VideoAlbums.DoesNotExist:
            raise Http404

    def get_videos(self, id):
        try:
            return VideoGallery.objects.filter(album_id=id)
        except VideoGallery.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        album = self.get_album(id)
        album_ser = VideoAlbumsFullSerializer(album)
        videos = self.get_videos(id)
        videos_ser = VideoGalleryShortSerializer(videos, many=True)
        data = {}
        data.update(album_ser.data)
        data['videos'] = []
        for element in videos_ser.data:
            data['videos'].append(element)
        return Response(data)



class VideoGalleryList(APIView):
    def get(self, request, format=None):
        obj = VideoGallery.objects.all()
        serializer = VideoGalleryFullSerializer(obj, many=True)
        return Response(serializer.data)



class VideoGalleryDetail(APIView):
    def get_album(self, id):
        try:
            return VideoAlbums.objects.get(id=id)
        except VideoAlbums.DoesNotExist:
            raise Http404

    def get_video(self, pk):
        try:
            return VideoGallery.objects.get(id=pk)
        except VideoGallery.DoesNotExist:
            raise Http404

    def get(self, request, id, pk, format=None):
        album = self.get_album(id)
        album_ser = VideoAlbumsFullSerializer(album)
        video = self.get_video(pk)
        video_ser = VideoGalleryFull_v2Serializer(video)
        data = {}
        data.update(album_ser.data)
        data['video'] = []
        data['video'].append(video_ser.data)
        return Response(data)



class PhotoAlbumsList(APIView):
    def get(self, request, format=None):
        obj = PhotoAlbums.objects.all()
        serializer = PhotoAlbumsFullSerializer(obj, many=True)
        return Response(serializer.data)



class PhotoAlbumsDetail(APIView):
    def get_object(self, id):
        try:
            return PhotoAlbums.objects.get(id=id)
        except PhotoAlbums.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        obj = self.get_object(id)
        serializer = PhotoAlbumsFullSerializer(obj)
        return Response(serializer.data)




class PhotoGalleryList(APIView):
    def get(self, request, format=None):
        obj = PhotoGallery.objects.all()
        serializer = PhotoGalleryFullSerializer(obj, many=True)
        return Response(serializer.data)




class PhotoGalleryAlbum_v2(APIView):
    def get(self, request, id, format=None):
        album = PhotoAlbums.objects.get(id=id)
        album_ser = PhotoAlbumsFullSerializer(album)
        obj = PhotoGallery.objects.filter(album_id=id)
        serializer = PhotoGalleryFull_v2Serializer(obj, many=True)
        data = {}
        data.update(album_ser.data)
        data['photos'] = []
        for element in serializer.data:
            data['photos'].append(element)
        print(data)
        return Response(data)



class PhotoGalleryDetail(APIView):
    def get_object(self, id):
        try:
            return PhotoGallery.objects.get(id=id)
        except PhotoGallery.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        obj = self.get_object(id)
        serializer = PhotoGalleryFullSerializer(obj)
        return Response(serializer.data)
