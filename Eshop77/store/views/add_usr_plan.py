from django.shortcuts import render, redirect

from django.contrib.auth.hashers import check_password
from store.models.customer import Customer
from django.views import View

from store.models.product import Product
from store.models.orders import Order
from Nodetree.models import Nodetree ,Custreferral_income
from store.middlewares.auth import auth_middleware

class usrpln_conf(View):


    def get(self , request ):
       
        customer = request.session.get('customer')
        cust_obj=Customer.objects.all()
       
        context={'cust_all':cust_obj}
        return render(request , 'add_user_points.html'  ,context)
    
    def post(self , request ):
       
        userBV_points = str(request.POST.get('userBV')).strip()
        cust_username = str(request.POST.get('custuser_name')).strip()
        ## update BV points in customer table ##
        customer_obj =Customer.objects.get(username=cust_username)
        customer_objrec=Customer.objects.get(id=customer_obj.id)
        customer_objrec.BV=int(userBV_points)
        customer_objrec.save()

        ## update BV points in Nodetree table and referral table##
        try:
           nodecust_obj =Nodetree.objects.get(username=cust_username)
           nodecust_objrec=Nodetree.objects.get(id=nodecust_obj.id)
           nodecust_objrec.BV=int(userBV_points)
           nodecust_objrec.save()

           referral_obj=Custreferral_income.objects.get(referre_custname=cust_username)
           referral_idobj=Custreferral_income.objects.get(id=referral_obj.id)
           referral_idobj.referre_origBV=int(userBV_points)
           referral_idobj.save()


        except:
            print('no record in nodetree')




        cust_obj_updated=Customer.objects.all()

        context={'cust_all':cust_obj_updated}

        
        
         
        return render(request , 'add_user_points.html' ,context )


    # def parse_orders(request):
    # ord2cnf = []
    # if request.method == 'POST':
    #     ord2cnf = request.POST.getlist('ordchecks2')
    #     ord2rev = request.POST.getlist('ordchecks1')
    #     print()
    #     for upd_counter in ord2cnf:
    #          print('upd_counterupd_counter',upd_counter)
    #          ord_upd=Order.objects.get(id=upd_counter)
    #          ord_upd.status=True
    #          ord_upd.save()

             
    #     for upd_counter2 in ord2rev:
    #          print('revert order',upd_counter2)
    #          ord_upd2=Order.objects.get(id=upd_counter2)
    #          ord_upd2.status=False
    #          ord_upd2.save()

    # return JsonResponse({'ord_upd':ord2cnf,'ord_rev':ord2rev})

        

        
        

       
       
        ########################################################################################
       
        #######################################################################################
        
       

    
