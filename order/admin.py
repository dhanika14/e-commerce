from django.contrib import admin   # type: ignore
from .models import Order  

class OrderAdmin(admin.ModelAdmin):
    list_display = ('order_id', 'c_id', 'product_id', 'quantity', 'price', 'stock_at_order_time', 'current_stock', 'order_date')

    

admin.site.register(Order, OrderAdmin)
