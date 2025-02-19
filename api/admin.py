from django.contrib import admin
from .models import Mitarbeiter, Artikel, Pferd

# Register your models here.
admin.site.register(Mitarbeiter)
admin.site.register(Artikel)
admin.site.register(Pferd)