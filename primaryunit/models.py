from django.db import models
from autoslug import AutoSlugField
class Primaryunit(models.Model):
    primaryunit_id = models.AutoField(primary_key=True)
    primaryunit_name = models.CharField(max_length=255 , null=True)
    primaryunit_slug = AutoSlugField(populate_from="primaryunit_name", unique=True)
    class Meta:
       db_table= "tbl_primaryunit"
    def __str__(self):
        return self.primaryunit_name

