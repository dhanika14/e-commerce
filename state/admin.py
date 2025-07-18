from django.contrib import admin
from .models import State

class StateAdmin(admin.ModelAdmin):
    list_display = ('state_id', 'state_name', 'state_slug')
    search_fields = ('state_name',)

admin.site.register(State, StateAdmin)
