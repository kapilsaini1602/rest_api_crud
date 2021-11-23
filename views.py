from django.shortcuts import render, HttpResponse, redirect
import io
from rest_framework.parsers import JSONParser
from .models import *
from .serializers import recordSerializer
from rest_framework.renderers import JSONRenderer
import json
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


# Create your views here.
@api_view(['GET', 'POST'])
def home(request, id=None):
    if request.method == "GET":
        print("get")
        if id == None:
            obj = record.objects.all()
            serializer = recordSerializer(obj, many=True)
            return Response(serializer.data)
        else:
            obj = record.objects.get(id=id)
            serializer = recordSerializer(obj)
            return Response(serializer.data)

    if request.method == "POST" and id == None:
        serializer = recordSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT', 'GET', 'PATCH', 'DELETE'])
def update(request, id):
    obj = record.objects.get(id=id)

    if request.method == "PUT" and id is not None:
        obj = record.objects.get(id=id)
        serializer = recordSerializer(obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    if request.method == "PATCH" and id is not None:
        serializer = recordSerializer(obj, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()

    if request.method == "DELETE" and id is not None:
        obj.delete()
        return redirect('http://127.0.0.1:8000/api/')

    serializer = recordSerializer(obj)
    return Response(serializer.data)
