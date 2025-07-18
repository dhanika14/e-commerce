from django.contrib import admin # type: ignore
from .models import Taluka

class TalukaAdmin(admin.ModelAdmin):
    list_display = ('taluka_id', 'taluka_name', 'district', 'taluka_slug')
    list_filter = ('district',)
    search_fields = ('taluka_name',)
admin.site.register(Taluka, TalukaAdmin)
