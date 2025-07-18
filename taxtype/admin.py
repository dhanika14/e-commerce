from django.contrib import admin # type: ignore
from .models import TaxType

class TaxTypeAdmin(admin.ModelAdmin):
    list_display=('taxtype_id','taxtype_name','taxtype_slug')
admin.site.register(TaxType,TaxTypeAdmin)
   

# Register your models here.
