from django.contrib import admin # type: ignore

# Register your models here.
from .models import Cart

class CartAdmin(admin.ModelAdmin):
    list_display=('cart_id','c_id','product_id','cart_quantity','cart_price',)
    list_filter=('c_id','product_id',)
    search_fields=('cart_id',)


admin.site.register(Cart, CartAdmin)

