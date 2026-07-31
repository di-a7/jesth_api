from django.urls import path
from .views import *

urlpatterns = [
   path('category/', CategoryGeneric.as_view()),
   path('category/<id>/', CategoryDetailGeneric.as_view()),
]