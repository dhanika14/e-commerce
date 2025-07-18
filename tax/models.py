from django.db import models # type: ignore
from autoslug import AutoSlugField # type: ignore
class Tax(models.Model):
    tax_id = models.AutoField(primary_key=True)
    tax_name = models.CharField(max_length=255 , null=True)
    tax_slug = AutoSlugField(populate_from="tax_name", unique=True)
    class Meta:
       db_table= "tbl_tax"
    def __str__(self):
        return self.tax_name

