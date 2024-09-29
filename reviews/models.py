from django.db import models
# from django.core.validators import MaxLengthValidator, MinValueValidator
from movies.models import Movie


class Review(models.Model):
    movie = models.ForeignKey(Movie,on_delete=models.PROTECT, related_name='reviews')
    stars = models.IntegerField()
    comments = models.TextField(blank = True, null = True)


    def __str__(self):
        return self.movie