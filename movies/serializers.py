from django.db.models import Avg
from django.forms import ValidationError
from movies.models import Movie
from genres.serializers import GenreSerializer
from actors.serializers import ActorSerializer
from rest_framework import serializers


class MoviesSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=Movie
        fields= '__all__'

#essa função get retorna a media de avaliações do filme usando uma função com metodos SQL aggregate e Average
   


    # def validate_release_date(self,value):
    #     if value.year < 1990:
    #         raise ValidationError('A data de lançamento deve ser maior do que 1990')
    #     return value
    

    def validade_description(self,value):
        if len(value) >= 500:
            raise serializers.ValidationError("digite uma descrição menor que 500")
        return value 
    
class MovieListDetailSerializer(serializers.ModelSerializer):
    actors= ActorSerializer(many= True)
    genre= GenreSerializer()
    rate= serializers.SerializerMethodField(read_only=True)

    class Meta:

        model= Movie
        fields=  ['id','title', 'genre','actors','rate']
    
    
    def get_rate(self, obj):
        rate= obj.reviews.aggregate(Avg('stars'))['stars__avg']

        if rate:
            return round(rate, 1)
        
        return None