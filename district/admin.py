from django.contrib import admin # type: ignore
from .models import District

class DistrictAdmin(admin.ModelAdmin):
    list_display = ('district_id', 'district_name', 'state', 'district_slug')
    list_filter = ('state',)
    search_fields = ('district_name',)

admin.site.register(District, DistrictAdmin)
