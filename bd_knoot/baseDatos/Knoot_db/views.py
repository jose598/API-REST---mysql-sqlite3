from django.shortcuts import render
from rest_framework import viewsets
from .models import Anuncio
from .serializers import AnuncioSerializer

class AnuncioViewSet(viewsets.ModelViewSet):
    serializer_class=AnuncioSerializer
    queryset=Anuncio.objects.all()
