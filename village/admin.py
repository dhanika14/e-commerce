from django.contrib import admin
from .models import Village

class VillageAdmin(admin.ModelAdmin):
    list_display = ('village_id', 'village_name', 'taluka')

admin.site.register(Village, VillageAdmin)