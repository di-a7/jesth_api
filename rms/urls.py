from django.urls import path
from .views import category_list

urlpatterns = [
   path('category/', category_list)
]