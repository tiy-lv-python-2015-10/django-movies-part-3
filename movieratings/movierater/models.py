from django.contrib.auth.models import User
from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=255)
    genre = models.CharField(max_length=255)

    @property
    def avg_rating(self):
        average = 0
        for rating in self.rating_set.all():
            average += rating.rating
        if self.rating_set.all().count() > 0:
            average = average / self.rating_set.all().count()
        return round(average, 2)

    def __str__(self):
        return str(self.title)


class Rater(models.Model):
    user = models.OneToOneField(User, null=True, blank=True)
    gender = models.CharField(max_length=20)
    age = models.IntegerField()
    occupation = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=10)


class Rating(models.Model):
    rater = models.ForeignKey(Rater)
    movie = models.ForeignKey(Movie)
    rating = models.IntegerField()
    timestamp = models.IntegerField()
