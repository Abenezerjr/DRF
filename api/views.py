from django.shortcuts import render

# Create your views here.
from .models import Movie
from django.http import JsonResponse


def movieList(request):
    movies=Movie.objects.all() # qureies set
    data={
        'movies':list(movies.values())
    }
    return JsonResponse(data)
    # context={
    #     'movies':movies
    # }
    #
    # return render(request,'api/movies/movies.html',context)
    # return JsonResponse()
def movieDetailes(request,pk):
    movie=Movie.objects.get(id=pk)

    data={
        'name':movie.name,
        'description':movie.description,
        'active':movie.active,
    }

    return JsonResponse(data)