from django.db import models # type: ignore

# Create your models here.
class Brands(models.Model): 
    brands_id = models.AutoField(primary_key=True)
    
    brands_name = models.CharField(max_length=255)
    brands_img=models.ImageField(upload_to='brands/',null=True)
   
    class Meta:
        db_table = "tbl_brands"
    def __str__(self):
        return self.brands_name

