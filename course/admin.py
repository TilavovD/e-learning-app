from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Author)
admin.site.register(Tag)

@admin.register(Course)
class Admin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'category', 'level', 'type', 'duration')
    list_filter = ('type', 'level', 'duration',)
    search_fields = ('title',)
    ordering = ('title',)

@admin.register(Category)
class Admin(admin.ModelAdmin):
    list_display = ('title',)
    list_filter = ('title',)
    search_fields = ('title',)
    ordering = ('title',)
