import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from genres.models import Genre
from rest_framework import mixins, views,generics
from genres.serializers import GenreSerializer
from rest_framework.permissions import  IsAuthenticated
from app.permissions import GlobalDefaultPermission




# @csrf_exempt
class GenreListCreateAPIView(generics.ListCreateAPIView):
    permission_classes=(IsAuthenticated,GlobalDefaultPermission,) 
    queryset= Genre.objects.all()
    serializer_class=GenreSerializer


class GenreDetailUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes= (IsAuthenticated,GlobalDefaultPermission,)
    queryset= Genre.objects.all()
    serializer_class= GenreSerializer

    
    # def get(self):
    #     genres=Genre.objects.all()
    #     data= [{'id': genre.id, 'name': genre.name} for genre in genres]
    #     return JsonResponse(data,safe=False)
    # elif request.method =='POST':
    #     data=json.loads(request.body.decode('utf-8'))
    #     new_genre=Genre(name=data['name']).save()
    #     return JsonResponse({ 'name':new_genre.name},status=201)


# @csrf_exempt
# def gente_detail(request,pk):
#     genre= get_object_or_404(Genre,pk=pk)
#     if request.method =='GET':
#         return JsonResponse({'id': genre.id,'name': genre.name})
#     elif request.method =='PUT':
        
#         data= json.loads(request.body.decode('utf-8'))
#         genre.name=data['name']
#         genre.save()
#         return JsonResponse(
#             {'id':genre.id,'name':genre.name}
#             )   
#     elif request.method =='DELETE':
#         genre.delete()
#         return JsonResponse({'message':'genre excluded successfull'},status=204)