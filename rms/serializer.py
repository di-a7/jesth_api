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
      item = Category.objects.filter(name = validated_data.get('name'))
      if self.instance:
         item = item.exclude(pk=self.instance.pk)
      if item.exists():
         raise serializers.ValidationError(
            {"message": "Data already exists"}
         )
      return super().save(**kwargs)
   
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
   # category = serializers.StringRelatedField(read_only=True)
   # category_id = serializers.PrimaryKeyRelatedField(queryset = Category.objects.all())
   class Meta:
      model = Menu
      fields = ['id' , 'name','category','price','price_with_tax']
   
   def get_price_with_tax(self, menu:Menu):
      return menu.price * 0.13 + menu.price
   
   # calculate 10% discount and show using api

class OrderMenuSerializer(ModelSerializer):
   class Meta:
      model = OrderMenu
      fields = ['menu']

class OrderSerializer(ModelSerializer):
   user = serializers.HiddenField(default = serializers.CurrentUserDefault())
   total_price = serializers.FloatField(read_only = True)
   status = serializers.CharField(read_only=True)
   is_paid = serializers.BooleanField(read_only=True)
   items = OrderMenuSerializer(many=True)
   class Meta:
      model = Order
      fields = ['id',"user","quantity","total_price","status","is_paid",'items']
   
   def create(self, validated_data):
      items = validated_data.pop('items')
      total = 0
      for item in items:
         food_id = item.get('menu')
         food_price = food_id.price * validated_data.get('quantity')
         total += food_price
      
      order = Order.objects.create(total_price = total,**validated_data)
      for item in items:
         OrderMenu.objects.create(order = order, menu=item.get('menu'))
      return order

# ordermenu.quantity field add
# validated_data :
#    {
#       "quantity": 2,
#    }

# items :
# "items": [
#          {
#          "menu": 11,
#           "quantity":2
#          },
#           {
   #           "menu": 12
#              "quantity":5
   #        }
# ]









# class CategorySerializer(serializers.Serializer):
#    id = serializers.IntegerField(read_only=True)
#    name = serializers.CharField()
   
#    def create(self, validated_data):
#       return Category.objects.create(name = validated_data.get('name'))
   
#    def update(self, instance, validated_data):
#       instance.name = validated_data.get('name', instance.name)
#       return instance
   # validated_data: {"name":"category1"}
