from django.contrib import admin

from movies.models import Movie, Rating, Tag, Genre, Link, Rater


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ['title', 'genres', 'id']


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ['user_id', 'movie_id', 'rating', 'timestamp', 'id']


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['user_id', 'movie_id', 'tag', 'timestamp', 'id']


@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    list_display = ['movie_id', 'imdb_id', 'tmdb_id', 'id']


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ['genre', 'id']


@admin.register(Rater)
class RaterAdmin(admin.ModelAdmin):
    list_display = ['age', 'gender', 'occupation', 'zip_code']