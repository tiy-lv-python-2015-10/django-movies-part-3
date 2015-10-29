from django.contrib import admin
from movierater.models import Movie, Rater, Rating


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'genre')

@admin.register(Rater)
class RaterAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'gender', 'age', 'occupation', 'zip_code')

@admin.register(Rating)
class AdminRating(admin.ModelAdmin):
    list_display = ('id', 'rater', 'movie', 'rating', 'timestamp')

