from django.contrib import admin
from .models import *
# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
   list_display = ('id','name')

admin.site.register(Category, CategoryAdmin)

class MenuAdmin(admin.ModelAdmin):
   list_display = ('id','name','price','category')
   search_fields = ('name',)
   list_filter=('category',)
admin.site.register(Menu, MenuAdmin)

admin.site.register(Table)

class OrderMenuInline(admin.TabularInline):
   model = OrderMenu
   autocomplete_fields = ("menu",)

class OrderAdmin(admin.ModelAdmin):
   list_display = ('id', 'user','total_price','status')
   inlines = [OrderMenuInline]

admin.site.register(Order, OrderAdmin)
# admin.site.register(OrderMenu)
