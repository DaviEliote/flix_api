from django.urls import path
from . import views


urlpatterns= [
  
    path ('movies/', views.MovieListCreateView.as_view(),name='movies'),
    path('movies/<int:pk>/',views.MovieRetrieveUpdateDestroyView.as_view(),name='moviespk'),
    
    
            ]