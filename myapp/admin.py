from django.contrib import admin
from ckeditor.widgets import CKEditorWidget
from .models import Post, Category, Contact, Pendidikan
from django import forms

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        widgets = {
            'content': CKEditorWidget(),
        }

class PostAdmin(admin.ModelAdmin):
    form = PostForm
    list_display = ('postname', 'display_category', 'display_pendidikan', 'created', 'updated')
    list_filter = ('category', 'pendidikan')
    search_fields = ('postname', 'content')

    def display_pendidikan(self, obj):
        pendidikan_names = [pendidikan.name for pendidikan in obj.pendidikan.all()]
        return ", ".join(pendidikan_names)
    display_pendidikan.short_description = 'Pendidikan'
    
    def display_category(self, obj):
        category_names = [category.name for category in obj.category.all()]
        return ", ".join(category_names)
    display_category.short_description = 'Category'

admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(Contact)
admin.site.register(Pendidikan)

admin.site.site_header = 'YAYASAN AL MANNAN | ADMIN PANEL'
admin.site.site_title = 'AL MANNAN | BLOGGING WEBSITE'
admin.site.index_title = 'Al - Mannan Site Administration'
    