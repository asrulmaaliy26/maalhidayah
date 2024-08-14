from django.views.generic import TemplateView, ListView, DetailView, FormView
from django.shortcuts import get_object_or_404
from django.conf import settings
from django.core.paginator import Paginator
from myapp.models import Post
from myapp.forms import ContactForm
from django.contrib.messages.views import SuccessMessageMixin

class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            context['kegiatan_posts'] = Post.objects.filter(category__name='kegiatan')[:4]
            context['header_beranda_posts'] = Post.objects.filter(category__name='header')
            context['recent_posts'] = Post.objects.all().order_by("-id")[:3]
            context['media_url'] = settings.MEDIA_URL
        except Post.DoesNotExist as e:
            context['error'] = f"Error fetching posts: {str(e)}"
        return context

class VisiMisiView(TemplateView):
    template_name = 'visimisi.html'

class StrukturOrganisasiView(TemplateView):
    template_name = 'strukturorganisasi.html'

class PrestasiMaView(TemplateView):
    template_name = 'prestasima.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            context['recent_posts'] = Post.objects.filter(category__name='prestasi').order_by("-id")[:2]
            context['posts'] = Post.objects.filter(category__name='prestasi')
            context['posts_asia'] = Post.objects.filter(category__name='prestasi', pendidikan__name='asia')
            context['posts_nasional'] = Post.objects.filter(category__name='prestasi', pendidikan__name='nasional')
            context['posts_provinsi'] = Post.objects.filter(category__name='prestasi', pendidikan__name='provinsi')
            context['posts_kabupaten'] = Post.objects.filter(category__name='prestasi', pendidikan__name='kabupaten')
            context['posts_kecamatan'] = Post.objects.filter(category__name='prestasi', pendidikan__name='kecamatan')
            context['media_url'] = settings.MEDIA_URL
        except Post.DoesNotExist as e:
            context['error'] = f"Error fetching posts: {str(e)}"
        return context

class BeritaView(ListView):
    model = Post
    template_name = 'berita.html'
    context_object_name = 'page_obj'
    paginate_by = 5

    def get_queryset(self):
        return Post.objects.all().order_by("-id")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            context['penting_posts'] = Post.objects.filter(category__name='penting')
            context['recent_posts'] = Post.objects.all().order_by("-id")[:2]
            context['media_url'] = settings.MEDIA_URL
        except Post.DoesNotExist as e:
            context['error'] = f"Error fetching posts: {str(e)}"
        return context

class FasilitasView(TemplateView):
    template_name = 'fasilitas.html'

class ContactView(SuccessMessageMixin, FormView):
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = '/contact/'
    success_message = 'Thank you for contacting us. We will get back to you soon.'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class PostDetailView(DetailView):
    model = Post
    template_name = 'detail.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            context['recent_posts'] = Post.objects.all().order_by("-id")[:2]
            context['media_url'] = settings.MEDIA_URL
        except Post.DoesNotExist as e:
            context['error'] = f"Error fetching post detail: {str(e)}"
        return context
