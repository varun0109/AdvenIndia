from django.db import  models
from .product import Product
from django.core.validators import MinLengthValidator
import datetime

class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    password = models.CharField(max_length=500)
    favourites= models.ForeignKey(Product,
                                on_delete=models.CASCADE,null=True)
    BV=models.IntegerField(default=0)
    username = models.CharField(max_length=50,default='__')
    joining_date = models.DateField(default=datetime.datetime.today)
    
    

    def register(self):
        self.save()

    @staticmethod
    def get_customer_by_email(email):
        
        try:
           return Customer.objects.get(email=email)
        except:
             
            return False

    @staticmethod    
    def get_customer_by_username(username):
        try:
            return Customer.objects.get(username=username)
        except:
            return False
        
 


    def isExists(self):
        if Customer.objects.filter(username = self.username):
            return True

        return  False


