from django.contrib import admin
from .models import  Fileupl, FilmWork

class FileuplAdmin(admin.TabularInline):
    model = Fileupl

class FilmWorkAdmin(admin.ModelAdmin):
    list_display = ['title']
    inlines = [FileuplAdmin]

admin.site.register(FilmWork, FilmWorkAdmin)
admin.site.register(Fileupl)


