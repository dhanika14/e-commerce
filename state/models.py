from django.db import models # type: ignore
from autoslug import AutoSlugField  # type: ignore # Install via `pip install django-autoslug`

    
class State(models.Model):
    state_id = models.AutoField(primary_key=True)
    state_name = models.CharField(max_length=255, unique=True)
    state_slug = AutoSlugField(populate_from="state_name", unique=True)

    class Meta:
        db_table = "tbl_state"

    def __str__(self):
        return self.state_name
