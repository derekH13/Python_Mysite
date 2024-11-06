from django.contrib import admin

# Register your models here.
from .models import Post


class PostAdmin(admin.ModelAdmin):
    # definindo que quer que apareça no admin post
    # colunas
    list_display = ('title', 'slug', 'status', 'created_on')
    # um filtro para status
    list_filter = ('status', )
    # barra de pesquisa para title e content
    search_fields = ['title', 'content']
    # pre popula o slug baseado no title
    prepopulated_fields = {'slug': ('title', )}

# dxdddd


class PostEvercicio(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status', 'created_on')
    list_filter = ('status', )
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title', )}


# faz aparecer um post no django admin
admin.site.register(Post, PostEvercicio)
