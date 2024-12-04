from django.shortcuts import render, redirect ,HttpResponseRedirect ,HttpResponse
 

from django.contrib.auth.hashers import check_password
from store.models.customer import Customer
from django.views import View
from django.db.models import Max
from store.models.product import Product
from store.models.orders import Order
from Nodetree.models import Balancing_income
from Nodetree.models import Customermart ,Nodetree
from Nodetree.views.nodetree_parse import tree_parse
import requests
import json
from store.views.sendsms import sendsms 

class CheckOut(View):
    
   
    def post(self, request):
        address = request.POST.get('address')
        phone = request.POST.get('phone')   
        addresszip = request.POST.get('addresszip') 
        customer = request.session.get('customer')
        username=request.session.get('username')
        cart = request.session.get('cart')
        print(' request.session cart', request.session['cart'] )
        cart_price=0
        cart_BVgained=0
        #url = "https://sandbox.cashfree.com/pg/links" ## move url to settings
        products = Product.get_products_by_id(list(cart.keys()))
        print('in check out--',address, phone, customer, cart,"---" ,products)
        order_id=''
        order_amount=0
        order_currency=''
        current_time="2023-03-07T17:04:05+05:30"
        auto_reminders=''
        order_purpose=''
        try:
           customer_order=Order.objects.all().aggregate(Max('order_id'))
           new_order_id=int(customer_order['order_id__max'])+1 
        except:
           new_order_id=100
        for product in products:
            print("product.id",product.id,cart)
            cart_price=int(product.price-((product.price*product.discount)/100))*int(cart.get(str(product.id))) + int(cart_price)
            
            cart_BVgained=int(product.BV_gained)*int(cart.get(str(product.id))) + int(cart_BVgained)
            
            ##get max order id ##
           
            
            print(customer_order)
            
            
            #####################

            order = Order(customer=Customer(id=customer),
                          product=product,
                          price=product.price-((product.price*product.discount)/100),
                          address=address,
                          phone=phone,
                          quantity=cart.get(str(product.id)),
                          order_id=new_order_id)
            product_orderquantity=cart.get(str(product.id))
            product_iid=product.id

            ## reducing number of items in product table in case of succesfully order ##
            prod_upd=Product.objects.get(id=product_iid)
            if prod_upd.quantity >0:
               prod_upd.quantity=int(prod_upd.quantity)-int(product_orderquantity)
               prod_upd.save()
            print("*******##",prod_upd.quantity ,' ',product_iid)
            order.save()  ## check if order is saved successfully

            ## update Custemer table BV on successfull purchase

            ##once order is saved Nodetree_balancing_income should have new updated balanced BV

            ##### reduce quantity from product table ####
            
            
            
             
           

            #############################################
            price=int(order.price)*int(order.quantity)
            
            ## create order 
            ## get max order id from table
            #order_id = Order.objects.all().values_list('id', flat=True).order_by('-id').first() 
            order_id=new_order_id
            order_amount=cart_price
            order_currency='INR'
            order_purpose='orderpayment'
            current_time="2024-01-07T18:04:05+05:30" ##change it datetime.datetime.now(pytz.timezone('Asia/Kolkata'))
            auto_reminders= False
        
        
        order_amt_obj=Order.objects.filter(order_id=new_order_id)
        for ord_coun in order_amt_obj:
           print("orddddd",)
           order_amt_objid=Order.objects.get(pk=ord_coun.id)
           order_amt_objid.total_order_price=cart_price
           order_amt_objid.save()
        ## not working
        cust_currobj = Customer.objects.get(pk=customer)
        #total_curr_BV=cart_BVgained+cust_currobj.BV
        #cust_updatedbv=Customer(id=cust_currobj.id)
        #cust_updatedbv.BV=total_curr_BV
        #cust_updatedbv.save(update_fields=["BV"])  


        ## update cust_mart table in case of purchase
    
        
        try:
          #nodetree_qs=Nodetree.objects.get(username=str(cust_currobj.username).strip())
          
          mart_updateBV=Nodetree.objects.get(username=username)
          print(username,"============>>>>>>>>>>>>>>>>>>>>>>.",mart_updateBV.id) 
          martid_4updateBV=Nodetree.objects.get(id=mart_updateBV.id)
          curr_pp=martid_4updateBV.purchase_points_pos
          print(username,"============>>>>>>>>>>>>>>>>>>>>>>.",curr_pp ,martid_4updateBV)
          martid_4updateBV.purchase_points_pos=int(cart_BVgained)+int(curr_pp)
          martid_4updateBV.save(update_fields=["purchase_points_pos"])
        except:
           pass
        
        ## run nodetree_parse.py to add data to  Nodetree_balancing_income table ##
        tree_parse(username)
       
        ############## get recent orders #########################################

        recent_orders=Order.objects.filter(customer__username=username).order_by('date')[:5]

        print("---->> recent_orders",recent_orders)

        ##########################################################################
        #########  generate UPI scan here for payment ############################
        order_dic={}
         
     
        curr_order=Order.objects.filter(order_id=new_order_id)


        for order_cntr in curr_order:
           print('order_cntr',order_cntr.product.name)
           print('order_cntr',order_cntr.product.image)
           print('order_cntr',order_cntr.price)
           print('order_cntr',order_cntr.quantity)
           print("---------------------------------")
           
        order_dic['total_amount']=cart_price
        order_dic['data']=curr_order
        order_dic['recent']=recent_orders
        print("order_dic",order_dic)
        ##########################################################################
       
        ## send sms to CP Yadav
        order_det={'orderid':new_order_id,'order_price':cart_price}

      


        sendsms(order_det)
        request.session['cart'] = {}
        ## pass order id , order date , products in order , price per product , total amount and scal
        ## and delivery date
        return render(request,'myupi_scan.html',order_dic)
       

