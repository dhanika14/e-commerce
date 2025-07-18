from django.db import models # type: ignore
from autoslug import AutoSlugField  # type: ignore # Install via `pip install django-autoslug`

    
class Franchise(models.Model):
    franchise_id = models.AutoField(primary_key=True)
    franchise_name = models.CharField(max_length=255, unique=True)
    franchise_slug = AutoSlugField(populate_from="franchise_name", unique=True)

    class Meta:
        db_table = "tbl_franchise"

    def __str__(self):
        return self.franchise_name
