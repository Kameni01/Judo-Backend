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
from quickstart.serializers import UserSerializer, GroupSerializer


@api_view(['GET'])
def api_root(request, format=None):
    """
    Стартовая точка API
    """
    return Response({
        'users': reverse('user-list', request=request),
        'groups': reverse('group-list', request=request),
    })
