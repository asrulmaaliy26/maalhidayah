from pyexpat.errors import messages
from django.shortcuts import get_object_or_404, render
from myapp.forms import ContactForm
from myapp.models import Post
from django.conf import settings
from django.core.paginator import Paginator

# Create your views here.
def index(request):
    context = {}
    try:
        kegiatan_posts = Post.objects.filter(category__name='kegiatan')[:4]
        header_beranda_posts = Post.objects.filter(category__name='header')
        recent_posts = Post.objects.all().order_by("-id")[:3]

        context.update({
            'kegiatan_posts': kegiatan_posts,
            'header_beranda_posts': header_beranda_posts,
            'recent_posts': recent_posts,
            'media_url': settings.MEDIA_URL
        })
    except Post.DoesNotExist as e:
        context['error'] = f"Error fetching posts: {str(e)}"

    return render(request, 'index.html', context)

def visimisi(request):

    return render(request, 'visimisi.html')

def strukturorganisasi(request):

    return render(request, 'strukturorganisasi.html')

def prestasima(request):
    context = {}
    try:
        recent_posts = Post.objects.filter(category__name='prestasi').order_by("-id")[:2]
        posts = Post.objects.filter(category__name='prestasi')
        posts_asia = Post.objects.filter(category__name='prestasi',pendidikan__name='asia')
        posts_nasional = Post.objects.filter(category__name='prestasi',pendidikan__name='nasional')
        posts_provinsi = Post.objects.filter(category__name='prestasi',pendidikan__name='provinsi')
        posts_kabupaten = Post.objects.filter(category__name='prestasi',pendidikan__name='kabupaten')
        posts_kecamatan = Post.objects.filter(category__name='prestasi',pendidikan__name='kecamatan')

        context.update({
            'posts': posts,
            'recent_posts': recent_posts,
            'posts_asia': posts_asia,
            'posts_nasional': posts_nasional,
            'posts_provinsi': posts_provinsi,
            'posts_kabupaten': posts_kabupaten,
            'posts_kecamatan': posts_kecamatan,
            'media_url': settings.MEDIA_URL
        })
    except Post.DoesNotExist as e:
        context['error'] = f"Error fetching posts: {str(e)}"

    return render(request, 'prestasima.html', context)

def berita(request):
    context = {}
    try:
        # Ambil semua post dan urutkan berdasarkan ID
        post_list = Post.objects.all().order_by("-id")
        
        # Setup pagination
        paginator = Paginator(post_list, 5)  # Tampilkan 5 post per halaman
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        penting_posts = Post.objects.filter(category__name='penting')
        recent_posts = Post.objects.all().order_by("-id")[:2]

        context.update({
            'page_obj': page_obj,
            'penting_posts': penting_posts,
            'recent_posts': recent_posts,
            'media_url': settings.MEDIA_URL
        })
    except Post.DoesNotExist as e:
        context['error'] = f"Error fetching posts: {str(e)}"

    return render(request, 'berita.html', context)

def fasilitas(request):

    return render(request, 'fasilitas.html')

def contact(request):
    success_message = ''
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            success_message = 'Thank you for contacting us. We will get back to you soon.'
            messages.success(request, success_message)
            form = ContactForm()  # Reset the form after saving
        else:
            messages.error(request, 'There was an error in your submission.')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form, 'success_message': success_message})

def detail(request, id):
    context = {}
    try:
        post = get_object_or_404(Post, id=id)
        recent_posts = Post.objects.all().order_by("-id")[:2]
        context.update({
            'post': post,
            'media_url': settings.MEDIA_URL,
            'recent_posts': recent_posts,
        })
    except Post.DoesNotExist as e:
        context['error'] = f"Error fetching post detail: {str(e)}"

    return render(request, 'detail.html', context)