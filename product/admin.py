from django.contrib import admin # type: ignore

from .models import Product
class ProductAdmin(admin.ModelAdmin):
    list_display=('product_id','product_name','product_marathi_name','product_hsn_code','product_slug','tax','brands','category','product_img','primaryunit','taxtype','alternateunit','barcode','qrcode','mrp','sale','op_qty','op_value','mfg_date','exp_date',)
    list_filter=('tax','brands','category','primaryunit','taxtype','alternateunit',)
    search_fields=('product_name',)
admin.site.register(Product,ProductAdmin)
# Register your models here.
