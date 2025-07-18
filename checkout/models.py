from django.db import models

class Checkout(models.Model):
    PAYMENT_METHOD_CHOICES = [
        ('cod', 'Cash On Delivery'),
        ('online', 'Online Transfer'),
    ]
    checkout_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    email = models.EmailField()
    telephone = models.CharField(max_length=15)
    address = models.TextField()
    payment_method = models.CharField(max_length=10, choices=PAYMENT_METHOD_CHOICES,null=True)
    coupon_code = models.CharField(max_length=50, blank=True, null=True)
    card_number = models.CharField(max_length=16, blank=True, null=True)
    agree_terms = models.BooleanField(default=False)
    

    def str(self):
        return  self.first_name
    
    class Meta:
        db_table = 'tbl_checkout'