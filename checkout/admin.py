from django.contrib import admin
from .models import Checkout


class CheckoutAdmin(admin.ModelAdmin):
    list_display = ['checkout_id','first_name', 'email', 'telephone','address', 'payment_method','coupon_code','card_number','agree_terms']
    
admin.site.register(Checkout,CheckoutAdmin)