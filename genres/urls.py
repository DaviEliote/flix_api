from django.urls import path
from . import views


urlpatterns= [  
    path('genre/',views.GenreListCreateAPIView.as_view(),name='genre_list'),
    path('genre/<int:pk>/',views.GenreDetailUpdateDestroyView.as_view(),name='gente_detail'),
    
    
    
    ]
