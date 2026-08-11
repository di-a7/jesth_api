from django.db import models
from django.conf import settings
# from django.contrib.auth.models import User
# from django.contrib.auth import get_user_model
# User = get_user_model()
User = settings.AUTH_USER_MODEL
# Create your models here.
class Category(models.Model):    # breakfast, dinner, lunch, drink
   name = models.CharField(max_length = 200)
   
   def __str__(self):
      return self.name

class Menu(models.Model):
   name = models.CharField(max_length=200)      # sprint
   category = models.ForeignKey(Category, on_delete = models.CASCADE)   # drink
   price = models.FloatField()
   image = models.ImageField(null=True, blank=True)
   
   def __str__(self):
      return self.name

class Table(models.Model):
   num = models.CharField(max_length=2)
   is_available = models.BooleanField(default=True)

   def __str___(self):
      return f"Table {self.num} - {self.is_available}"

class Order(models.Model):
   STATUS_CHOICE = [
      ('P','Pending'),
      ('C',"Completed"),
      ('D',"Delivered")
   ]
   user = models.ForeignKey(User, on_delete=models.CASCADE)
   quantity = models.IntegerField(null=True, blank=True,default=1)
   total_price = models.FloatField(null=True, blank=True)
   status = models.CharField(max_length=1, choices=STATUS_CHOICE, default='P')
   is_paid = models.BooleanField(default=False)

class OrderMenu(models.Model):
   order = models.ForeignKey(Order, on_delete=models.PROTECT, related_name='items')
   menu = models.ForeignKey(Menu, on_delete=models.PROTECT, related_name='items')