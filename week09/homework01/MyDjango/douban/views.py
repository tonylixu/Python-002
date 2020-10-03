from django.shortcuts import render
from django.http import HttpResponse
from . models import Movie


def index(request):
    """Simply return Hello for empty string"""
    return HttpResponse('Hello')


def movies(request):
    """Return all movies that have starts >3"""
    all_movies = Movie.objects.filter(movies_stars__gt=3)
    return render(request, 'movies.html', locals())
