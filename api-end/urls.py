from django.urls import path
from . import views


urlpatterns=[
    path('list/',views.movie_list,name='list'),
    path('list/<int:pk>/',views.movie_details,name='list')
]