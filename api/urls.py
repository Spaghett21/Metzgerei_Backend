from django.urls import path
from .views import MitarbeiterAPIView, MitarbeiterDetailAPIView, ArtikelAPIView, ArtikelDetailAPIView, PferdAPIView, PferdDetailAPIView

urlpatterns = [
    path('metzgerei/mitarbeiter/', MitarbeiterAPIView.as_view(), name="mitarbeiter_list"),
    path('metzgerei/mitarbeiter/<int:pk>/', MitarbeiterDetailAPIView.as_view(), name="mitarbeiter_detail"),
    
    path('metzgerei/artikel/', ArtikelAPIView.as_view(), name="artikel_list"),
    path('metzgerei/artikel/<int:pk>/', ArtikelDetailAPIView.as_view(), name="artikel_detail"),
    
    path('metzgerei/pferd/', PferdAPIView.as_view(), name="pferd_list"),
    path('metzgerei/pferd/<int:pk>/', PferdDetailAPIView.as_view(), name="pferd_detail"),
]
