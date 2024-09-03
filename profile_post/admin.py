
from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('content_snippet', 'user', 'created_at')
    search_fields = ('content', 'user__username')
    list_filter = ('created_at', 'user')
    ordering = ('-created_at',)

    def content_snippet(self, obj):
        return obj.content[:50]  
    content_snippet.short_description = 'Content Snippet'