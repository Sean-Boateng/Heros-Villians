

from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response

 
from rest_framework import status


from .models import Super
from .serializers import SuperSerializer


@api_view(['GET','POST'])
def supers_list(request):
    if request.method == 'GET':

        type_name= request.query_params.get('type')
        print(type_name)

        queryset = Super.objects.all()

        if type_name:
            queryset= queryset.filter(super_type__type_of_super=type_name)

        

        serializer = SuperSerializer(queryset,many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = SuperSerializer(data = request.data)
        if serializer.is_valid() == True:
            serializer.save()
            return Response(serializer.data,status=201)
        else:
            return Response(serializer.errors,status=400)
            
    



@api_view(['GET', 'PUT', 'DELETE'])
def supers_detail(request,pk):
    if request.method == 'GET':
        super = get_object_or_404(Super,pk=pk)
        serializer = SuperSerializer(super)
        return Response(serializer.data, status = 201)
    
    elif request.method == 'PUT':
        super = get_object_or_404(Super, pk=pk)
        serializer = SuperSerializer(super, data = request.data)
        serializer.is_valid(raise_exception = True)
        serializer.save()
        return Response(serializer.data, status= 200)
    
    elif request.method == 'DELETE':
        super = get_object_or_404(Super, pk=pk)
        super.delete()
        return Response(status= status.HTTP_204_NO_CONTENT)
