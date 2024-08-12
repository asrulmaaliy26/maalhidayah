from django.urls import path
from django.views.generic.base import RedirectView
from .views import (
    detail,
    index,
    visimisi,
    strukturorganisasi,
    prestasima,
    berita,
    fasilitas,
    contact,
)

urlpatterns = [
    path('', index, name="index"),
    path('visimisi', visimisi, name="visimisi"),
    path('strukturorganisasi', strukturorganisasi, name="strukturorganisasi"),
    path('prestasima', prestasima, name="prestasima"),
    path('berita', berita, name="berita"),
    path('detail/<int:id>', detail, name="detail"),
    path('fasilitas', fasilitas, name="fasilitas"),
    path('contact', contact, name="contact"),
    path('ppdb', RedirectView.as_view(url='https://ppdb.almannan.id/', permanent=False), name='ppdb'),
]
