from django.urls import path
from . import views


urlpatterns=[
    path('list/',views.movieList,name='list'),
    path('list/<int:pk>/',views.movieDetailes,name='list')
]