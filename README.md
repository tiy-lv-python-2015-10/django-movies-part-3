# Django Movie Ratings Part 3

## Description

Create an interface in Django to the [MovieLens dataset][movielens] to create and modify data.

## Learning Objectives

After completing this assignment, you should be able to:

* Distinguish when to use GET vs POST
* Create forms
* Extend user objects via OneToOneFields
* Understand function and class based views
* Processing form data
* Use logged in user from request

## Details

### Requirements
* Tests
* No pep8 errors

### Deliverables

* A Git repo called django-movies containing at least:
  * a `requirements.txt` file
  * a `README.md` file
  * a Django project called `movieratings`

### Normal Mode
Continuing with last night's homework use the data and views already created to save time.

Link your Rater model to the built-in User model via a OneToOneField. Create a username, email, and password for all raters.

Add the ability for a user to rate a movie they have not previously rated from the movie page.

When logged in, customize pages for the user. For example, on the page that shows the top 20 movies rated, show the user which ones they've rated.

Add the ability for a user to rate a movie they have not previously rated from the movie page.


### Hard Mode

Add a personal page for each user that only they can see. It should have all their ratings, allow them to edit or delete those ratings, and also show them the top 20 movies they have not rated.

Add the ability for a user to edit a rating they've made.

Add registration, login, and logout to your application.
