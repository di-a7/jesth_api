from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Category
from .serializer import CategorySerializer
# Create your views here.

@api_view()
def category_list(request):
   category = Category.objects.all()
   serializer = CategorySerializer(category, many=True)   # serialize, serializetion: convert queryset to json format
   return Response(serializer.data)

# create a api endpoint to get data of table model