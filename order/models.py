from django.db import models
from customer.models import Customer
from product.models import Product

class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    c_id = models.ForeignKey(Customer, null=True, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, null=True, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    quantity = models.IntegerField(null=True)
    order_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "tbl_order"

    def __str__(self):
        return f"Order ID: {self.order_id}, Customer ID: {self.c_id}"
