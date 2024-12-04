from django.db import models
from .category import Category
import datetime


class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits = 10,decimal_places = 2,default=0)
    MRP = models.DecimalField(max_digits = 10,decimal_places = 2,default=0)
    cost_price = models.DecimalField(max_digits = 10,decimal_places = 2,default=0)
    discount=models.DecimalField(max_digits = 10,decimal_places = 2,default=0)
    sell_price = models.DecimalField(max_digits = 10,decimal_places = 2,default=0)
    admin_percentage= models.DecimalField(max_digits = 10,decimal_places = 2,default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    description = models.CharField(max_length=200, default='' , null=True , blank=True)
    BV_gained=models.DecimalField(max_digits = 10,decimal_places = 2,default=0)
    image = models.ImageField(upload_to='uploads/products/' ,default='uploads/products/default-profile-.png')
    image1 = models.ImageField(upload_to='uploads/products/',default='uploads/products/default-profile-.png')
    image2 = models.ImageField(upload_to='uploads/products/',default='uploads/products/default-profile-.png')
    image3 = models.ImageField(upload_to='uploads/products/',default='uploads/products/default-profile-.png')
    image4 = models.ImageField(upload_to='uploads/products/',default='uploads/products/default-profile-.png')
    size_xs=models.IntegerField(default=0)
    size_s=models.IntegerField(default=0)
    size_m=models.IntegerField(default=0)
    size_l=models.IntegerField(default=0)
    size_xl=models.IntegerField(default=0)
    size_xxl=models.IntegerField(default=0)
    quantity=models.IntegerField(default=0)
    Product_brand=models.CharField(max_length=50 , default='Eshop')
    before_discount=models.IntegerField(default=0)
    Commission=models.DecimalField(max_digits = 10,decimal_places = 2,default=0)
    manufactur_date = models.DateField(default=datetime.datetime.today)
    expiry_date = models.DateField(default=datetime.datetime.today)
    status = models.IntegerField(default=1) 
    barcode = models.CharField(max_length=50,null=True,default='-')
    mart_flag = models.IntegerField(default=1) 
    seller_gst=models.CharField(max_length=20 , default='')
    seller_name=models.CharField(max_length=50 , default='-')
    sgst=models.DecimalField(max_digits = 5,decimal_places = 2,default=0)
    cgst=models.DecimalField(max_digits = 5,decimal_places = 2,default=0)
    invoice_nm=models.CharField(max_length=10 , default='-')
    hsn=models.CharField(max_length=10 , default='-')
    discount_by_vendor=models.DecimalField(max_digits = 10,decimal_places = 2,default=0)
 


    @staticmethod
    def get_products_by_id(ids):
        return Product.objects.filter(id__in =ids)

    @staticmethod
    def get_all_products():
        return Product.objects.all()

    @staticmethod
    def get_all_products_by_categoryid(category_id):
        if category_id:
            return Product.objects.filter(category = category_id)
        else:
            return Product.get_all_products();