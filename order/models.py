from django.db import models# type: ignore
from customer.models import Customer
from product.models import Product
from django.utils import timezone # type: ignore

class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    c_id = models.ForeignKey(Customer, null=True, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, null=True, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    quantity = models.IntegerField(null=True)
    stock_at_order_time = models.IntegerField(null=True)
    current_stock = models.IntegerField(null=True) 
    order_date = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = "tbl_order"

    def _str_(self):
        return f"Order ID: {self.order_id}"
