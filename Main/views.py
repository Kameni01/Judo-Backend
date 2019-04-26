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
        # achievs = Achievements.objects.filter(owner_id=id)
        # achiev_ser = AchievementsFullSerializer(achievs, many=True)
        obj = self.get_object(id)
        serializer = SportCardFullSerializer(obj)
        return Response(serializer.data)



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
        serializer = TrenerCardFullSerializer(obj)
        return Response(serializer.data)



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



class VideoGalerryList(APIView):
    def get(self, request, format=None):
        obj = VideoGalerry.objects.all()
        serializer = VideoGalerryFullSerializer(obj, many=True)
        return Response(serializer.data)



class VideoGalerryAlbum(APIView):
    def get(self, request, id, format=None):
        obj = VideoGalerry.objects.filter(album_id=id)
        serializer = VideoGalerryFullSerializer(obj, many=True)
        return Response(serializer.data)



class VideoGalleryDetail(APIView):
    def get_object(self, id):
        try:
            return VideoGalerry.objects.get(id=id)
        except VideoGalerry.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        obj = self.get_object(id)
        serializer = VideoGalerryFullSerializer(obj)
        return Response(serializer.data)
