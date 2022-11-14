from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view

from supers.models import Super



@api_view(['GET'])
def supers_list(request,pk):
    if request.method == 'GET':
        super = get_object_or_404(Super,pk=pk)
        serializer = SuperSerializer(super)
        return Response(serializer.data, status = 201)
        