from django.db import models
from .product import Product
from .customer import Customer


class favourite(models.Model):
    favourites= models.ForeignKey(Product,
                                on_delete=models.CASCADE,null=True)
    customer=models.ForeignKey(Customer,
                                on_delete=models.CASCADE,null=True)

  
 
    @staticmethod
    def get_all_favs_by_customerid(customer_id):
        if customer_id:
            return favourite.objects.filter(customer = customer_id)
        else:
            return None