from django.contrib import admin # type: ignore
from .models import Wishlist

class WishlistAdmin(admin.ModelAdmin):
    list_display = ('wish_id', 'product_id','c_id')
    

admin.site.register(Wishlist,WishlistAdmin)
# Register your models here.
