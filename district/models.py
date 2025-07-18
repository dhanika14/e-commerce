from django.db import models # type: ignore
from autoslug import AutoSlugField # type: ignore
from state.models import State  # Importing State model



 
 
class District(models.Model):
     district_id = models.AutoField(primary_key=True)
     district_name = models.CharField(max_length=255)
     state = models.ForeignKey(State, on_delete=models.CASCADE, null=True)
     district_slug = AutoSlugField(populate_from="district_name", unique=True)

     class Meta:
        db_table = "tbl_district"

     def __str__(self):
        return self.district_name


    


   