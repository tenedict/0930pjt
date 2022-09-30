from django.shortcuts import render, redirect
from .models import Movie

# Create your views here.


def index(request):
    movies = Movie.objects.all()

    context = {
        "movies": movies,
    }
    return render(request, "movies/index.html", context)


def new(request):

    return render(request, "movies/new.html")



def create(request):
    content = request.GET.get("content")
    title = request.GET.get("title")
    created_at = request.GET.get("created_at")
    print(title, content)
    Movie.objects.create(
        content=content,
        title=title,
        created_at = created_at,
    )

    return redirect("movies:index")

def detail(request, pk):
    movie = Movie.objects.get(pk=pk)
    
    return render(request, 'movies/detail.html', {'movie':movie})

def edit(request, pk):
    movie = Movie.objects.get(pk=pk)

    return render(request, 'movies/edit.html', {'movie':movie})


def update(request, pk):
    movie = Movie.objects.get(pk=pk)
    content = request.GET.get("content")
    title = request.GET.get("title")
    updated_at = request.GET.get("updated_at")

    movie.content = content
    movie.title = title
    movie.updated_at = updated_at
    movie.save()

    return redirect('movies:index')


def delete(request,pk):
    movie = Movie.objects.get(pk=pk)
    movie.delete()

    return redirect('movies:index')