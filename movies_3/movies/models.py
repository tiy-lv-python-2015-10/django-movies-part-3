from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=100)
    genres = models.CharField(max_length=100)
    date_added = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.title)


class Rating(models.Model):
    user_id = models.IntegerField()
    movie_id = models.ForeignKey(Movie)
    rating = models.FloatField()
    timestamp = models.IntegerField(null=True)
    date_added = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)


class Tag(models.Model):
    user_id = models.IntegerField()
    movie_id = models.IntegerField()
    tag = models.CharField(max_length=100)
    timestamp = models.IntegerField()
    date_added = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)


class Link(models.Model):
    imdb_id = models.IntegerField()
    tmdb_id = models.IntegerField()
    movie_id = models.IntegerField(null=True)
    date_added = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)


class Genre(models.Model):
    genre = models.CharField(max_length=100)
    id = models.IntegerField(primary_key=True)
    date_added = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)


class Rater(models.Model):
    male = 'male'
    female = 'female'
    other = 'other'
    gender_choices = ((male, 'man'), (female, 'woman'), (other, 'complicated'))
    gender = models.CharField(max_length=8, choices=gender_choices, default=male)
    age = models.IntegerField(null=True)
    occupation = models.CharField(max_length=30)
    zip_code = models.CharField(max_length=10)
    def __str__(self):
        return "age: {} gender: {} occupation: {} zip: {}".format(self.age, self.gender,
                                                                  self.occupation, self.zip_code)
