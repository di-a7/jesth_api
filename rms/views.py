from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializer import CategorySerializer
# Create your views here.

@api_view(['GET','POST'])
def category_list(request):
   if request.method == 'GET':
      category = Category.objects.all()
      serializer = CategorySerializer(category, many=True)  # serialize, serializetion: convert queryset to json format
      return Response(serializer.data)
   elif request.method == 'POST':
      serializer = CategorySerializer(data=request.data)  # deserialize, deserializer: convert json into queryset
      serializer.is_valid(raise_exception=True)
      serializer.save()
      # return Response({"message":"Data added.","result":serializer.data})
      return Response(serializer.data)

@api_view(['GET','DELETE','PUT'])
def category_detail(request,id):
   category = Category.objects.get(id = id)
   if request.method == 'GET':
      serializer = CategorySerializer(category)
      return Response(serializer.data)
   elif request.method == 'DELETE':
      item = OrderMenu.objects.filter(menu__category = category).count()
      if item > 0:
         return Response({"message":"Data can't be deleted. Protected Foreign Key in OrderMenu"})
      category.delete()
      return Response({"message":"Data has been deleted."})
# implement PUT request, add update method in serializer
# complete CRUD operation in Table api

