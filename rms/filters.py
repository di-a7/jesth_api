from django_filters.rest_framework import FilterSet, filters
from .models import Menu
class MenuFilter(FilterSet):
   min_price = filters.NumberFilter(field_name="price", lookup_expr='gte')
   max_price = filters.NumberFilter(field_name="price", lookup_expr='lte')
   class Meta:
      model = Menu
      fields = ['category', 'min_price', 'max_price']