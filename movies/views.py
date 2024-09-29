from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from movies.models import Movie
from movies.serializers import MoviesSerializer, MovieListDetailSerializer
from app.permissions import GlobalDefaultPermission


class MovieListCreateView(generics.ListCreateAPIView):
    permission_classes =(IsAuthenticated,GlobalDefaultPermission)
    queryset = Movie.objects.all()
    serializer_class = MoviesSerializer

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return MovieListDetailSerializer
        return MoviesSerializer


class MovieRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes =(IsAuthenticated,GlobalDefaultPermission)
    queryset = Movie.objects.all()
    

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return MovieListDetailSerializer
        return MoviesSerializer    