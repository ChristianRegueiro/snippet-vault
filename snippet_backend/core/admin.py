from django.contrib import admin
from .models import Snippet, Tag

@admin.register(Snippet)
class SnippetAdmin(admin.ModelAdmin):
    list_display = ('name', 'language', 'pinned', 'created_at', 'updated_at')
    search_fields = ('name', 'language')
    list_filter = ('pinned', 'language')
    filter_horizontal = ('tags',)
    save_as = True
    

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'get_snippets_count')
    search_fields = ('name',)
    list_filter = ('name',)
    save_as = True
    
    def get_snippets_count(self, obj):
        return obj.snippets.count()
    get_snippets_count.short_description = 'Snippets Count'