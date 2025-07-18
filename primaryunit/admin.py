from django.contrib import admin

from .models import Primaryunit
class PrimaryunitAdmin(admin.ModelAdmin):
    list_display=('primaryunit_id','primaryunit_name','primaryunit_slug')
admin.site.register(Primaryunit,PrimaryunitAdmin)
# Register your models here.

