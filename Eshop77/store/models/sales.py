from django.db import models
from django.utils import timezone
from store.models.product import Product


class Sales(models.Model):
    code = models.CharField(max_length=100)
    sub_total = models.FloatField(default=0)
    grand_total = models.FloatField(default=0)
    grand_total_rounded = models.FloatField(default=0)
    tax_amount = models.FloatField(default=0)
    tax = models.FloatField(default=0)
    discount = models.FloatField(default=0)
    tendered_amount = models.FloatField(default=0)
    amount_change = models.FloatField(default=0)
    date_added = models.DateTimeField(default=timezone.now) 
    date_updated = models.DateTimeField(auto_now=True) 
    cust_name = models.CharField(max_length=50,default='-')
    cust_userid = models.CharField(max_length=20,default='-')
    cust_phone=models.BigIntegerField(default=0, max_length=10)
    new_sales_code =models.CharField(max_length=10,default='-')
    return_flag =models.CharField(max_length=20,default='New')
    edit_usr =models.CharField(max_length=20,default='-')



    def __str__(self):
        return self.code
    
class salesItems(models.Model):
    sale_id = models.ForeignKey(Sales,on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product,on_delete=models.CASCADE)
    price = models.FloatField(default=0)
    qty = models.FloatField(default=0)
    discount_amt = models.FloatField(default=0)
    total = models.FloatField(default=0)
    salesItems_return_id =models.CharField(max_length=10,default='-')
    return_flag =models.CharField(max_length=20,default='New')
    edit_usr =models.CharField(max_length=20,default='-')
    delete_flag=models.CharField(max_length=1,default='N')
