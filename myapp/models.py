from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField
from django.db.models.signals import pre_save, post_delete
from django.dispatch import receiver
from PIL import Image
from io import BytesIO
from django.core.files.base import ContentFile
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name

class Pendidikan(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name

class Post(models.Model):
    postname = models.CharField(max_length=600)
    author = models.CharField(max_length=100, blank=True)
    category = models.ManyToManyField(Category)
    pendidikan = models.ManyToManyField(Pendidikan) 
    image = models.ImageField(upload_to='images/posts', blank=True, null=True)
    content = RichTextField()
    link = models.URLField(max_length=200, blank=True, null=True)  # Field baru untuk link
    created = models.DateTimeField(default=timezone.now)  # Field baru untuk created
    updated = models.DateTimeField(auto_now=True) 
    time = models.CharField(default=timezone.now().strftime("%d %B %Y"), max_length=100, blank=True)
    
    def __str__(self):
        return str(self.postname)

@receiver(pre_save, sender=Post)
def compress_image(sender, instance, **kwargs):
    if instance.image:
        # Open the image file
        img = Image.open(instance.image)
        
        # Convert image to RGB (necessary if image is RGBA or has an alpha channel)
        if img.mode in ("RGBA", "P"):
            img = img.convert("RGB")
        
        # Compress image
        img_io = BytesIO()
        img.save(img_io, format='JPEG', quality=70)  # Set the quality level (e.g., 70)
        img_content = ContentFile(img_io.getvalue(), instance.image.name)
        
        # Replace the image with the compressed one
        instance.image.save(instance.image.name, img_content, save=False)

@receiver(post_delete, sender=Post)
def delete_post_image(sender, instance, **kwargs):
    if instance.image:
        instance.image.delete(False)

class Contact(models.Model):
    name = models.CharField(max_length=600)
    email = models.EmailField(max_length=600)
    subject = models.CharField(max_length=1000)
    message = models.TextField(blank=True)
    
    def __str__(self):
        return self.name