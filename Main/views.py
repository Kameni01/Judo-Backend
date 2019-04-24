from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse
from django.views.generic import View

from django.contrib.auth.mixins import LoginRequiredMixin

from .models import *
from .forms import *
from .utils import *

from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from rest_framework.response import Response

from .serializers import *


@api_view(['GET'])
def api_root(request, format=None):
    """
    Стартовая точка API
    """
    return Response({
        'news': reverse('news-list', request=request),
        'groups': reverse('group-list', request=request),
    })



class NewsList(generics.ListCreateAPIView):
    model = News
    serializer_class = NewsSerializer



class NewsDetail(generics.RetrieveUpdateDestroyAPIView):
    model = News
    serializer_class = NewsSerializer



class SportCardList(generics.ListCreateAPIView):
    model = SportCard
    serializer_class = SportCardSerializer



class SportCardDetail(generics.RetrieveUpdateDestroyAPIView):
    model = SportCard
    serializer_class = SportCardSerializer



class TrenerCardList(generics.ListCreateAPIView):
    model = TrenerCard
    serializer_class = SportCardSerializer



class TrenerCardDetail(generics.RetrieveUpdateDestroyAPIView):
    model = TrenerCard
    serializer_class = TrenerCardSerializer



class MaterialsList(generics.ListCreateAPIView):
    model = Materials
    serializer_class = MaterialsSerializer



class MaterialsDetail(generics.RetrieveUpdateDestroyAPIView):
    model = Materials
    serializer_class = MaterialsSerializer
