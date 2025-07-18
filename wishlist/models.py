from django.db import models # type: ignore
from customer.models import Customer  # Importing District model
from product.models import Product
class Wishlist(models.Model):
    wish_id = models.AutoField(primary_key=True)
    
    c_id = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    

    class Meta:
        db_table = "tbl_wish"

    def __str__(self):
         return f"Wishlist ID: {self.wish_id}"

# Create your models here.
