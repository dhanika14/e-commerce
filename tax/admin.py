from django.contrib import admin

from .models import Tax
class TaxAdmin(admin.ModelAdmin):
    list_display=('tax_id','tax_name','tax_slug')
admin.site.register(Tax,TaxAdmin)
# Register your models here.

