from django.contrib import admin
from django.contrib.admin import register

from app.models import User, Comment, Post

admin.site.register(User)
admin.site.register(Comment)
# admin.site.register(Post)


@register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author',)
    list_display_links = ('author',)
    list_filter = ('created',)
