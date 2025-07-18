from django.contrib import admin # type: ignore
from .models import Slider
class SliderAdmin(admin.ModelAdmin):
    list_display=('slider_id','slider_name','slider_img')
admin.site.register(Slider,SliderAdmin)
# Register your models here.
