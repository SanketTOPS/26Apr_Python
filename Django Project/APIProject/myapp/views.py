from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework.decorators import api_view


# Create your views here.

@api_view(['GET'])
def getalldata(request):
    if request.method=='GET':
        stdata=studinfo.objects.all()
        serial=studSerial(stdata,many=True)
        return Response(data=serial.data)

