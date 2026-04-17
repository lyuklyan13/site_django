from django.contrib import admin, messages

from .models import Men


@admin.register(Men)
class MenAdmin(admin.ModelAdmin):
    fields = ['title', 'slug', 'photo',  'content']
    prepopulated_fields = {"slug": ("title", )}
    list_display = ('title', 'time_create')
    list_display_links = ('title', )
    ordering = ['-time_create', 'title']


