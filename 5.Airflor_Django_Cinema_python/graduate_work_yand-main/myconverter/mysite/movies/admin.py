from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import FilmWorkMovie


class FilmWorkMovieAdmin(admin.TabularInline):
    model = FilmWorkMovie

admin.site.register(FilmWorkMovie)