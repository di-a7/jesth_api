from rest_framework import serializers
from .models import Category
class CategorySerializer(serializers.Serializer):
   id = serializers.IntegerField(read_only=True)
   name = serializers.CharField()
   
   def create(self, validated_data):
      return Category.objects.create(name = validated_data.get('name'))
   
   def update(self, instance, validated_data):
      instance.name = validated_data.get('name', instance.name)
      return instance
   # validated_data: {"name":"category1"}
