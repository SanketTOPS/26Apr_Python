from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework import status

# Create your views here.

@api_view(['GET'])
def getdata(request):
    if request.method=='GET':
        stdata=studinfo.objects.all()
        serial=studSerial(stdata,many=True)
        return Response(data=serial.data,status=status.HTTP_200_OK)
    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def getid(request,id):
    try:
        stid=studinfo.objects.get(id=id)
    except studinfo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serial=studSerial(stid)
    return Response(data=serial.data,status=status.HTTP_200_OK)
    

@api_view(['GET','DELETE'])
def deletedata(request,id):
    try:
        stid=studinfo.objects.get(id=id)
    except studinfo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method=='GET':
        serial=studSerial(stid)
        return Response(data=serial.data,status=status.HTTP_200_OK)
    if request.method=='DELETE':
        studinfo.delete(stid)
        return Response(status=status.HTTP_202_ACCEPTED)


@api_view(['POST'])
def savedata(request):
    if request.method=='POST':
        serial=studSerial(data=request.data)
        if serial.is_valid():
            serial.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET','PUT'])
def updatedata(request,id):
    try:
        stid=studinfo.objects.get(id=id)
    except studinfo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method=='GET':
        serial=studSerial(stid)
        return Response(data=serial.data,status=status.HTTP_200_OK)
    if request.method=='PUT':
        serial=studSerial(data=request.data,instance=stid)
        if serial.is_valid():
            serial.save()
            return Response(status=status.HTTP_202_ACCEPTED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

