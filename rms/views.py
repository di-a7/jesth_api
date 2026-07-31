from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializer import CategorySerializer
# Create your views here.
# CLASS BASED VIEW
from rest_framework.generics import ListAPIView, CreateAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
class CategoryGeneric(ListCreateAPIView):
   queryset = Category.objects.all()
   serializer_class = CategorySerializer

class CategoryDetailGeneric(RetrieveUpdateDestroyAPIView):
   queryset = Category.objects.all()
   serializer_class = CategorySerializer
   lookup_field = 'id'
   
   def delete(self,request,id):
      category = self.get_object()
      item = OrderMenu.objects.filter(menu__category = category).count()
      if item > 0:
         return Response({"message":"Data can't be deleted. Protected Foreign Key in OrderMenu"})
      category.delete()
      return Response({"message":"Data has been deleted."})



# GENERIC VIEW with mixin
# from rest_framework.generics import GenericAPIView
# from rest_framework import mixins
# class CategoryGeneric(GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
#    queryset = Category.objects.all()
#    serializer_class = CategorySerializer
   
#    def get(self,request):
#       return self.list(request)
#       # category = self.get_queryset()
#       # serializer = self.serializer_class(category, many=True)
#       # return Response(serializer.data)
   
#    def post(self,request):
#       return self.create(request)
#    #    serializer = self.serializer_class(data=request.data)
#    #    serializer.is_valid(raise_exception=True)
#    #    serializer.save()
#    #    return Response(serializer.data)

# class CategoryDetailGeneric(GenericAPIView,mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
#    queryset = Category.objects.all()
#    serializer_class = CategorySerializer
#    lookup_field = 'id'
   
#    def get(self,request,id):
#       return self.retrieve(request, id)
#       # category = self.get_object()
#       # serializer = self.serializer_class(category)
#       # return Response(serializer.data)

#    def put(self,request,id):
#       return self.update(request, id)
#       # category = self.get_object()
#       # serializer = CategorySerializer(category, data=request.data)
#       # serializer.is_valid(raise_exception=True)
#       # serializer.save()
#       # return Response(serializer.data)
   
#    def delete(self,request,id):
#       category = self.get_object()           # Category.objects.get(id = id)
#       item = OrderMenu.objects.filter(menu__category = category).count()
#       if item > 0:
#          return Response({"message":"Data can't be deleted. Protected Foreign Key in OrderMenu"})
#       category.delete()
#       return Response({"message":"Data has been deleted."})

# APIVIEW
# from rest_framework.views import APIView

# class CategoryView(APIView):
#    def get(self,request):
#       category = Category.objects.all()
#       serializer = CategorySerializer(category, many=True)
#       return Response(serializer.data)
   
#    def post(self,request):
#       serializer = CategorySerializer(data=request.data)
#       serializer.is_valid(raise_exception=True)
#       serializer.save()
#       return Response(serializer.data)


# class CategoryDetailView(APIView):
#    def get(self,request,id):
#       category = Category.objects.get(id = id)
#       serializer = CategorySerializer(category)
#       return Response(serializer.data)
   
#    def put(self,request,id):
#       category = Category.objects.get(id = id)
#       serializer = CategorySerializer(category, data=request.data)
#       serializer.is_valid(raise_exception=True)
#       serializer.save()
#       return Response(serializer.data)
   
#    def delete(self,request,id):
#       category = Category.objects.get(id = id)
#       item = OrderMenu.objects.filter(menu__category = category).count()
#       if item > 0:
#          return Response({"message":"Data can't be deleted. Protected Foreign Key in OrderMenu"})
#       category.delete()
#       return Response({"message":"Data has been deleted."})
# fetch single data
# create a class, get method, put method, delete method
# url define





# FUNCTION BASED VIEW
# @api_view(['GET','POST'])
# def category_list(request):
#    if request.method == 'GET':
#       category = Category.objects.all()
#       serializer = CategorySerializer(category, many=True)  # serialize, serializetion: convert queryset to json format
#       return Response(serializer.data)
#    elif request.method == 'POST':
#       serializer = CategorySerializer(data=request.data)  # deserialize, deserializer: convert json into queryset
#       serializer.is_valid(raise_exception=True)
#       serializer.save()
#       # return Response({"message":"Data added.","result":serializer.data})
#       return Response(serializer.data)

# @api_view(['GET','DELETE','PUT'])
# def category_detail(request,id):
#    category = Category.objects.get(id = id)
#    if request.method == 'GET':
#       serializer = CategorySerializer(category)
#       return Response(serializer.data)
#    elif request.method == 'DELETE':
#       item = OrderMenu.objects.filter(menu__category = category).count()
#       if item > 0:
#          return Response({"message":"Data can't be deleted. Protected Foreign Key in OrderMenu"})
#       category.delete()
#       return Response({"message":"Data has been deleted."})
# implement PUT request, add update method in serializer
# complete CRUD operation in Table api

