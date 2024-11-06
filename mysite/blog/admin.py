from django.contrib import admin

# Register your models here.
from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'status', 'created_on']
    list_filter = ('status', 'created_on')
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}


class PostEvercicio(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status', 'created_on')
    list_filter = ('status', )
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title', )}


# faz aparecer um post no django admin
admin.site.register(Post, PostEvercicio)
