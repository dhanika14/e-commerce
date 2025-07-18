from django.db import models # type: ignore
from autoslug import AutoSlugField # type: ignore

class TaxType(models.Model):
    taxtype_id = models.AutoField(primary_key=True)

    taxtype_name = models.CharField(max_length=255, unique=True,null=True)
    taxtype_slug = AutoSlugField(populate_from="taxtype_name",unique=True ,null=True)


    class Meta:
        db_table = "tbl_taxtype"

    def __str__(self):
        return self.taxtype_name

# Create your models here.
