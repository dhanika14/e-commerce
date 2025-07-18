from django.contrib import admin
from .models import Franchise

class FranchiseAdmin(admin.ModelAdmin):
    list_display = ('franchise_id', 'franchise_name', 'franchise_slug')
    search_fields = ('franchise_name',)

admin.site.register(Franchise, FranchiseAdmin)
