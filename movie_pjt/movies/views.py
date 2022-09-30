from django.shortcuts import render, redirect
from .models import Movie

# Create your views here.


def index(request):
    movies = Movie.objects.all()

    context = {
        "movies": movies,
    }
    return render(request, "movies/index.html", context)


def neww(request):
    content = request.GET.get("content")
    title = request.GET.get("title")

    Movie.objects.create(
        content=content,
        title=title,
    )

    return redirect("movies:index")
