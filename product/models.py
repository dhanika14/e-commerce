from django.db import models # type: ignore
from autoslug import AutoSlugField # type: ignore
from tax.models import Tax
from brands.models import Brands
from category.models import Category
from primaryunit.models import Primaryunit
from taxtype.models import TaxType
from alternateunit.models import AlternateUnit



class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=255 , null=True)
    product_marathi_name=models.CharField(max_length=255 , null=True)
    product_hsn_code=models.CharField(max_length=255 , null=True)
    product_slug = AutoSlugField(populate_from="product_name", unique=True)
    tax=models.ForeignKey(Tax,null=True,on_delete=models.CASCADE)
    brands=models.ForeignKey(Brands,null=True,on_delete=models.CASCADE)
    category=models.ForeignKey(Category,null=True,on_delete=models.CASCADE)
    product_img=models.ImageField(upload_to='',null=True)
    primaryunit=models.ForeignKey(Primaryunit,null=True,on_delete=models.CASCADE)
    taxtype=models.ForeignKey(TaxType,null=True,on_delete=models.CASCADE)
    alternateunit=models.ForeignKey(AlternateUnit,null=True,on_delete=models.CASCADE)
    barcode=models.CharField(max_length=255 , null=True)
    qrcode=models.CharField(max_length=255 , null=True)
    mrp=models.CharField(max_length=255 , null=True)
    sale=models.CharField(max_length=255 , null=True)
    op_qty=models.CharField(max_length=255 , null=True)
    op_value=models.CharField(max_length=255 , null=True)
    mfg_date=models.DateField(max_length=255 , null=True)
    exp_date=models.DateField(max_length=255 , null=True)






    class Meta:
       db_table= "tbl_product"
    def __str__(self):
        return self.product_name
# Create your models here.





