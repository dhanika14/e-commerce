from django.contrib import admin
from .models import Contactus
class ContactusAdmin(admin.ModelAdmin):
    list_display=('contact_id','contact_name','contact_email','contact_enquiry','contact_slug')
admin.site.register(Contactus,ContactusAdmin)
# Register your models here.

