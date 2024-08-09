from rest_framework.response import Response
from api.models import Movie
from .serializers import MovieSeralizer
from rest_framework.decorators import api_view
@api_view()
def movie_list(request):
    movie=Movie.objects.all()
    print(movie)
    serializer= MovieSeralizer(movie,many=True)
    return Response(serializer.data)


@api_view()
def movie_details(request,pk):
    movie=Movie.objects.get(id=pk)
    serializer = MovieSeralizer(movie)
    return Response(serializer.data)