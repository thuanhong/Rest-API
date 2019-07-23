from django.shortcuts import render
from .models import Songs
from .serializers import SongsSerializer
from rest_framework import generics

# Create your views here.

class ListSongView(generics.ListAPIView):
    """
    Provides a get method handler
    """
    queryset = Songs.objects.all()
    serializer_class = SongsSerializer
