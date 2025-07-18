from django.db import models
from autoslug import AutoSlugField
class Contactus(models.Model):
    contact_id = models.AutoField(primary_key=True)
    contact_name = models.CharField(max_length=255 , null=True)
    contact_email = models.CharField(max_length=255 , null=True)
    contact_enquiry = models.CharField(max_length=255 , null=True)
    contact_slug = AutoSlugField(populate_from="contact_name", unique=True)
    class Meta:
       db_table= "tbl_contact"


    def __str__(self):
        return self.contact_name
# Create your models here.
