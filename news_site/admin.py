from django.contrib import admin
from .models import *

class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'time_create', 'photo', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'time_create')
    prepopulated_fields = {'slug': ('title',)}

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('id',)
    # prepopulated_fields = {'slug': ('name',)}

class CommentAdmin(admin.AdminSite):
    list_display = ('name', 'email', 'post', 'created', 'active')
    list_filter = ('active', 'created')
    search_fields = ('name', 'email', 'text')


admin.site.register(News, NewsAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Comment, CategoryAdmin)
