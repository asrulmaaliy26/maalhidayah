from django.views.generic.base import RedirectView
from django.urls import path
from .views import (
    IndexView, VisiMisiView, StrukturOrganisasiView, PrestasiMaView, 
    BeritaView, FasilitasView, ContactView, PostDetailView
)

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('visimisi/', VisiMisiView.as_view(), name='visimisi'),
    path('strukturorganisasi/', StrukturOrganisasiView.as_view(), name='strukturorganisasi'),
    path('prestasima/', PrestasiMaView.as_view(), name='prestasima'),
    path('berita/', BeritaView.as_view(), name='berita'),
    path('fasilitas/', FasilitasView.as_view(), name='fasilitas'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='detail'),
    path('ppdb', RedirectView.as_view(url='https://ppdb.almannan.id/', permanent=False), name='ppdb'),
]
