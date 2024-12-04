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

class CheckOut(View):
    
    def post(self, request):
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        customer = request.session.get('customer')
        cart = request.session.get('cart')
        cart_price=0
        cart_BVgained=0
        url = "https://sandbox.cashfree.com/pg/links" ## move url to settings
        products = Product.get_products_by_id(list(cart.keys()))
        print('in check out--',address, phone, customer, cart,"---" ,products)
        order_id=''
        order_amount=0
        order_currency=''
        current_time="2023-03-07T17:04:05+05:30"
        auto_reminders=''
        order_purpose=''
        customer_order=Order.objects.filter(customer=customer).aggregate(Max('order_id'))
        new_order_id=int(customer_order['order_id__max'])+1 
        for product in products:
            print("product.id",product.id,cart)
            cart_price=int(product.price-((product.price*product.discount)/100))*int(cart.get(str(product.id))) + int(cart_price)

            cart_BVgained=int(product.BV_gained)*int(cart.get(str(product.id))) + int(cart_BVgained)
            
            ##get max order id ##
           
            
            print(customer_order)
            
            
            #####################

            order = Order(customer=Customer(id=customer),
                          product=product,
                          price=product.price,
                          address=address,
                          phone=phone,
                          quantity=cart.get(str(product.id)),
                          order_id=new_order_id)
            product_orderquantity=cart.get(str(product.id))
            product_iid=product.id
            prod_upd=Product.objects.get(id=product_iid)
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
        
        ## not working
        cust_currobj = Customer.objects.get(pk=customer)
        total_curr_BV=cart_BVgained+cust_currobj.BV
        #cust_updatedbv=Customer(id=cust_currobj.id)
        #cust_updatedbv.BV=total_curr_BV
        #cust_updatedbv.save(update_fields=["BV"])  

        ## update cust_mart table in case of purchase
        try:
          print('inside purchase_points_pos update block start')
          custmart_nodeqs=Nodetree.objects.get(username=str(cust_currobj.username).strip())
           #print("custmart_nodeqs",custmart_nodeqs.id)
          custmart_updateBV=Nodetree(id=custmart_nodeqs.id)
          custmart_updateBV.purchase_points_pos=cart_BVgained
          custmart_updateBV.save(update_fields=["purchase_points_pos"])
          print('inside purchase_points_pos update block end')
        except:
           pass
        
        ## run nodetree_parse.py to add data to  Nodetree_balancing_income table ##
        tree_parse()
        
        #########
         
        payload = {
                      "customer_details": {
                      "customer_phone": "9999999999",
                      "customer_email": "varun.singh0109@gmail.com",
                      "customer_name": "varun"
                       },
                      "link_meta": {"return_url": "http://127.0.0.1:8000/return/link_id/{link_id}"},
                      "link_notify": {
                      "send_sms": False,
                      "send_email": False
                       },
                      "link_id": 'order'+str(order_id),
                      "link_amount": order_amount,
                      "link_currency": order_currency,
                      "link_purpose": order_purpose,
                      "link_expiry_time": current_time,
                      "link_auto_reminders": auto_reminders
                      }
        headers = {
                      "accept": "application/json",
                      "x-client-id": "282916962f4ccec00dd8b2e660619282",
                      "x-client-secret": "TESTe32d870e1a1976d4b25b1aed9f46dfd0b938668a",
                      "x-api-version": "2022-09-01",
                      "content-type": "application/json"
                      }
            

        ##https://merchantsite.com/return?link_id={link_id}
        ## verify all fields are non null before sending request
        response = requests.post(url, json=payload, headers=headers)
        json_data = json.loads(response.text)
        print("================================")
        print(json_data)
        print(response.status_code)
        print("================================")
        
        if response.status_code==200:
          for res_key, res_val in json_data.items():
              print(res_key ,"--", res_val)
        else:
            print("there is some error")
        
        

       
        request.session['cart'] = {}

        ## handle response
        return HttpResponseRedirect(json_data['link_url'])
       

