from django.shortcuts import render , redirect

from django.contrib.auth.hashers import  check_password
from store.models.customer import Customer
from django.views import  View
from store.models.product import  Product
from store.models.customer import  Customer

class Cart(View):
    def get(self , request):
        print("inside cart.py",request.session.get('cart'))

        #ids = list(request.session.get('cart').keys())
        ids=[i for i,j in request.session.get('cart').items() if int(j)>0 ]
        print(ids)
        products = Product.get_products_by_id(ids)
        print(products)
        return render(request , 'cart.html' , {'products' : products} )

