from rest_framework import serializers
from .models import Mitarbeiter, Artikel, Pferd

class MitarbeiterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mitarbeiter
        fields = [
            'id',
            'firstname',
            'lastname',
            'gehalt',
            'schichtzeiten',
            'position',
        ]

class ArtikelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artikel
        fields = [
            'id',
            'artikelnummer',
            'beschreibung',
            'lagerbestand',
        ]

class PferdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pferd
        fields = [
            'id',
            'name',
            'gewicht',
            'herkunft',
        ]
