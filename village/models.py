from django.db import models
from autoslug import AutoSlugField
from taluka.models import Taluka  # Importing Taluka model

class Village(models.Model):
    village_id = models.AutoField(primary_key=True)
    village_name = models.CharField(max_length=255,null=True)
    taluka = models.ForeignKey(Taluka, on_delete=models.CASCADE, null=True)
    village_slug = AutoSlugField(populate_from="village_name", unique=True,null=True)

    class Meta:
        db_table = "tbl_village"

    def __str__(self):
        return self.village_name
