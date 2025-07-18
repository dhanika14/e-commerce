from django.contrib import admin # type: ignore
from .models import Customer
class CustomerAdmin(admin.ModelAdmin):
    list_display=['c_id','c_fullNameEng','c_fullNameMarathi','c_mobile','c_birthDate','c_pinCode','c_email','c_password']
admin.site.register(Customer,CustomerAdmin)


