from django.contrib import admin
from django.urls import path,include
from django.http import JsonResponse
from genres.views import GenreListCreateAPIView, GenreDetailUpdateDestroyView
from actors.views import ActorsListCreateView,ActorRetrieveUpdateDestroyView
from movies.views import MovieListCreateView, MovieRetrieveUpdateDestroyView
from reviews.views import ReviewListCreateView,ReviewRetrieveUpdateDestroyView

def hello_view(request):
    return JsonResponse({'message': 'hello word'})

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/v1/',include('authentication.urls')),
    
    path('api/v1/',include('genres.urls')),
    
    path('api/v1/',include('actors.urls')),
    
    path('api/v1/',include('movies.urls')),

    path('api/v1/', include('reviews.urls')),

   

   
    
]

