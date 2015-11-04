from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from movierater.forms import RatingForm
from movierater.models import Movie, Rater


def list_movies(request):
    movies = Movie.objects.all()
    return render(request, 'movierater/movies.html', {'movies': movies})


def movie_detail(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    return render(request, 'movierater/movie_detail.html', {'movie': movie})


def rater_detail(request, rater_id):
    rater = get_object_or_404(Rater, pk=rater_id)
    return render(request, 'movierater/rater.html', {'rater': rater})


def rate_movie(request):
    if request.methon == 'POST':
        form = RatingForm(request.POST)

        if form.is_valid():
            rating = form.save(commit=False)
            rating.author = request.user
            rating.save()

            return HttpResponseRedirect(reverse('movies'))

        else:
            form = RatingForm()
