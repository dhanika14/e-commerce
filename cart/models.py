from django.db import models # type: ignore
from customer.models import Customer
from product.models import Product

# Create your models here.
class Cart(models.Model): 
    cart_id = models.AutoField(primary_key=True)
    c_id = models.ForeignKey(Customer,null=True,on_delete=models.CASCADE)

    product_id = models.ForeignKey(Product,null=True,on_delete=models.CASCADE)

    cart_quantity = models.CharField(max_length=255,null=True)
    
    cart_price= models.CharField(max_length=255,null=True)

    class Meta:
        db_table = "tbl_cart"
    def __str__(self):
        return f"Cart Id:{self.cart_id}"

