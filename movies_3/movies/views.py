
from django.shortcuts import render
#from faker import Factory
from movies.models import Rater, Movie


#fake = Factory.create
#for Rater in range(0,100):

def list_movies(request):
    all_movies = Movie.objects.all()
    return render(request, '/forms.html', {'movies' : all_movies})
