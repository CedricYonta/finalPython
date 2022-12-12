from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from tutorial.serializers import  CapteurSerializer
from tutorial.serializers import  Capteur
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseRedirect
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
from rest_framework.response import Response
import json
from django.urls import reverse
from rest_framework.decorators import api_view


def addrecord(request):
    if request.method == 'POST':
       tutorial_data = JSONParser().parse(request)
       print(tutorial_data)
       tutorial_serializer = CapteurSerializer(data=tutorial_data)
       if tutorial_serializer.is_valid():
            tutorial_serializer.save()
            return JsonResponse(tutorial_serializer.data, status=status.HTTP_201_CREATED) 
       return JsonResponse(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
     

    
class CapteurViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Capteur.objects.all()
   # serializer_class = GroupSerializer
    serializer_class = CapteurSerializer
    #permission_classes = [permissions.IsAuthenticated]