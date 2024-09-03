from django.contrib import admin
from .models import Blog

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'date_created', 'image', 'video')
    search_fields = ('title', 'subtitle', 'content', 'author__username')
    list_filter = ('date_created', 'author')

    fieldsets = (
        (None, {'fields': ('title', 'subtitle', 'content')}),
        ('Media', {'fields': ('image', 'video')}),
        ('Información Adicional', {'fields': ('author', 'date_created')}),
    )
