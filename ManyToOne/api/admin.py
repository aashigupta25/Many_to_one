from django.contrib import admin
from .models import Blog

# Register your models here.
@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display= ['blog_title', 'blog_category', 'blog_publish_date', 'user']