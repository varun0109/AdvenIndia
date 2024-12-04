from django.shortcuts import render , redirect

from django.contrib.auth.hashers import  check_password
from store.models.customer import Customer
from store.models.category import Category
from django.views import  View
from store.models.product import  Product
from store.models.customer import  Customer

def addnew_product(request):
     if request.method == 'GET':
          all_category=Category.objects.all()
          return render(request ,'addnew_product.html',{'all_category':all_category})
     
     if request.method == 'POST':
          prd=1
          return render(request ,'addnew_product.html',{'prd':prd})