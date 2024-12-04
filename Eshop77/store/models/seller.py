from django.db import models
from .category import Category


class Seller(models.Model):
    Seller_name = models.CharField(max_length=50)
    Product_name = models.CharField(max_length=50)
    product_price = models.IntegerField(default=0)
    Product_category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    Product_description = models.CharField(max_length=200, default='' , null=True , blank=True)
    Product_image = models.ImageField(upload_to='uploads/products/')
    Product_image1 = models.ImageField(upload_to='uploads/products/')
    Product_image2 = models.ImageField(upload_to='uploads/products/')
    Product_image3 = models.ImageField(upload_to='uploads/products/')
    Product_image4 = models.ImageField(upload_to='uploads/products/')
    Product_image5 = models.ImageField(upload_to='uploads/products/')
    Product_image6 = models.ImageField(upload_to='uploads/products/')
    size_xs=models.IntegerField(default=0)
    size_s=models.IntegerField(default=0)
    size_m=models.IntegerField(default=0)
    size_l=models.IntegerField(default=0)
    size_xl=models.IntegerField(default=0)
    size_xxl=models.IntegerField(default=0)
    quantity=models.IntegerField(default=0)

    @staticmethod
    def get_seller_by_id(ids):
        return Seller.objects.filter(id__in =ids)

    @staticmethod
    def get_all_seller():
        return Seller.objects.all()

    @staticmethod
    def get_all_seller_by_productid(product_id):
        if product_id:
            return Seller.objects.filter(id__in = product_id)
        else:
            return Seller.get_all_seller();