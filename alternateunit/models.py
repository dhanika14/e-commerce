from django.db import models # type: ignore
from autoslug import AutoSlugField # type: ignore

class AlternateUnit(models.Model):
    alternateunit_id = models.AutoField(primary_key=True)
    alternateunit_name = models.CharField(max_length=255, unique=True)
    alternateunit_slug = AutoSlugField(populate_from="alternateunit_name",unique=True)

    class Meta:
        db_table = "tbl_alternateunit"

    def __str__(self):
        return self.alternateunit_name


# Create your models here.