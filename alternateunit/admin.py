from django.contrib import admin # type: ignore
from .models import AlternateUnit

class AlternateUnitAdmin(admin.ModelAdmin):
    list_display=('alternateunit_id','alternateunit_name','alternateunit_slug')
admin.site.register(AlternateUnit,AlternateUnitAdmin)

# Register your models here.
