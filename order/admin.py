from django.contrib import admin  
from .models import Order  

class OrderAdmin(admin.ModelAdmin):  
    list_display = ('order_id', 'c_id', 'product_id', 'price', 'quantity', 'order_date')  
    list_filter = ('c_id', 'product_id',)  
    search_fields = ('order_id',)  

admin.site.register(Order, OrderAdmin)  
