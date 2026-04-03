
from django.contrib import admin
from .models import Post, Comment

@admin.action(description='Delete selected posts')
def delete_selected_posts(modeladmin, request, queryset):
    queryset.delete()

class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'created_at', 'updated_at']
    search_fields = ['title', 'content', 'author__username']
    list_filter = ['author', 'created_at']
    actions = [delete_selected_posts]

class CommentAdmin(admin.ModelAdmin):
    list_display = ['post', 'author', 'created_at']
    search_fields = ['content', 'author__username', 'post__title']
    list_filter = ['created_at']

admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
