from unicodedata import category

from rest_framework.serializers import ModelSerializer 
from .models import *
from rest_framework import serializers

class CategoryModelSerializer(ModelSerializer):
   class Meta:
      model = Category
      fields = '__all__'
      # fields = ['id','name']
      # exclude = ['name']
   
   def save(self, **kwargs):
      validated_data = self.validated_data
      item = Category.objects.filter(name = validated_data.get('name')).count()
      if item > 0:
         raise serializers.ValidationError({"message":"Data already exists"})
      return super().save(self.instance,**kwargs)
   
   # def create(self, validated_data):
   #    item = Category.objects.filter(name = validated_data.get('name')).count()
   #    if item > 0:
   #       raise serializers.ValidationError({"message":"Data already exists"})
   #    return super().create(validated_data)

   # def update(self, instance, validated_data):
   #    item = Category.objects.filter(name = validated_data.get('name')).count()
   #    if item > 0:
   #       raise serializers.ValidationError({"message":"Data already exists"})
   #    return super().update(instance, validated_data)


class MenuSerializer(ModelSerializer):
   price_with_tax = serializers.SerializerMethodField()
   category = serializers.StringRelatedField()
   category_id = serializers.PrimaryKeyRelatedField(queryset = Category.objects.all())
   class Meta:
      model = Menu
      fields = ['id' , 'name', 'category_id','category','price','price_with_tax']
   
   def get_price_with_tax(self, menu:Menu):
      return menu.price * 0.13 + menu.price
   
   # calculate 10% discount and show using api

# class CategorySerializer(serializers.Serializer):
#    id = serializers.IntegerField(read_only=True)
#    name = serializers.CharField()
   
#    def create(self, validated_data):
#       return Category.objects.create(name = validated_data.get('name'))
   
#    def update(self, instance, validated_data):
#       instance.name = validated_data.get('name', instance.name)
#       return instance
   # validated_data: {"name":"category1"}
