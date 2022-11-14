from django import views
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from supers import serializers


from supers.models import Super
from supers.serializers import SuperSerializer


@api_view(['POST'])
def supers_list(request):
    if request.method == 'POST':
        serializer = SuperSerializer(data = request.data)
        if serializer.is_valid() = True:
            serializer.save()
            return Response(serializer.data,status=201)
        else:
            return Response(serializer.errors,status=400)



@api_view(['GET'])
def supers_detail(request,pk):
    if request.method == 'GET':
        super = get_object_or_404(Super,pk=pk)
        serializer = SuperSerializer(super)
        return Response(serializer.data, status = 201)
