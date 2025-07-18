from django.db import models # type: ignore
from autoslug import AutoSlugField # type: ignore
from district.models import District  # Importing District model

class Taluka(models.Model):
    taluka_id = models.AutoField(primary_key=True)
    taluka_name = models.CharField(max_length=255,null=True)
    district = models.ForeignKey(District, on_delete=models.CASCADE, null=True)
    taluka_slug = AutoSlugField(populate_from="taluka_name", unique=True,null=True)

    class Meta:
        db_table = "tbl_taluka"

    def __str__(self):
        return self.taluka_name
