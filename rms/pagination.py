from rest_framework.pagination import PageNumberPagination

class CategoryPagination(PageNumberPagination):
   page_size = 5
   page_query_param = 'p'
   max_page_size = 10