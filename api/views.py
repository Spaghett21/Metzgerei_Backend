from django.shortcuts import render
from rest_framework import viewsets
from .models import Mitarbeiter, Artikel, Pferd
from .serializers import MitarbeiterSerializer, ArtikelSerializer, PferdSerializer
from rest_framework import generics



class MitarbeiterAPIView(generics.ListCreateAPIView):
    queryset = Mitarbeiter.objects.all()
    serializer_class = MitarbeiterSerializer
    #permission to define permission_classes = [IsAuthenticated]


class MitarbeiterDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Mitarbeiter.objects.all()
    serializer_class = MitarbeiterSerializer
    # permission to define permission_classes = [IsAuthenticated]


class ArtikelAPIView(generics.ListCreateAPIView):
    queryset = Artikel.objects.all()
    serializer_class = ArtikelSerializer
     #permission to define permission_classes = [IsAuthenticated]


class ArtikelDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Artikel.objects.all()
    serializer_class = ArtikelSerializer
    #permission to define permission_classes = [IsAuthenticated]

class PferdAPIView(generics.ListCreateAPIView):
    queryset = Pferd.objects.all()
    serializer_class = PferdSerializer
    #permission to define permission_classes = [IsAuthenticated]  

class PferdDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pferd.objects.all()
    serializer_class = PferdSerializer
    #permission to define permission_classes = [IsAuthenticated]


# Alternative 
# class MitarbeiterViewSet(viewsets.ModelViewSet):
#   queryset = Mitarbeiter.objects.all()
#   serializer_class = MitarbeiterSerializer