from django.shortcuts import render, redirect

from django.contrib.auth.hashers import check_password
from store.models.customer import Customer
from django.views import View

from store.models.product import Product
from store.models.orders import Order
from store.middlewares.auth import auth_middleware

class OrderView(View):


    def get(self , request ):
       
        customer = request.session.get('customer')
        orders = Order.get_orders_by_customer(customer)

       
       
        ########################################################################################
        order_diclist={}
        order_list=[]
        print('orders-->',orders)
        for order_items in orders:
            prod_dic={'name':order_items.product.name,'date':order_items.date,'quantity':order_items.quantity,'price':order_items.price}
            
            if order_items.order_id in order_diclist:
               order_list.append(prod_dic)
               order_diclist[order_items.order_id]=order_list

            else:
                order_diclist[order_items.order_id]=order_list

             
        print('order_diclist',order_diclist)
        #######################################################################################
        
        return render(request , 'orders.html'  , {'orders' : orders})
