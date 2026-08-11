from django.urls import path
from .views import *
from rest_framework import routers

route = routers.DefaultRouter()
route.register('category',CategoryModelViewSet)
route.register('menu', MenuModelViewSet)
route.register('order', OrderViewSet)


urlpatterns = [
   # path('category/',CategoryModelViewSet.as_view({'get':'list', 'post':'create'})),
   # path('category/<id>',CategoryModelViewSet.as_view({'get':'retrieve','put':'update','delete':'destroy'}))
   # path('category/', CategoryViewSet.as_view({'get':'list', 'post':'create'})),
   # path('category/<id>/', CategoryDetailView.as_view({'get':'retrieve','put':'update','delete':'destroy'})),
] + route.urls