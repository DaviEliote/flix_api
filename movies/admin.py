from django.contrib import admin
from movies.models import Movie
# Register your models here.

@admin.register(Movie)
class AdminMovies(admin.ModelAdmin):
    list_display=('title','description','genre')
    
