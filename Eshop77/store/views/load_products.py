from django.shortcuts import render, redirect

from django.contrib.auth.hashers import check_password
from store.models.customer import Customer
from django.views import View

from store.models.product import Product
from store.models.category import Category
from store.models.orders import Order
from store.middlewares.auth import auth_middleware
import simplejson as json
from django.http import HttpResponse

class load_product(View):


    def get(self , request ):
       
        customer = request.session.get('customer')
        prod_items = Product.objects.all().order_by('-id')
        

       
       
        ########################################################################################
        
        print('prod_items-->',prod_items)
         
        #######################################################################################
        
        return render(request , 'load_products.html'  , {'prod_items' : prod_items})
    

    def post(self , request ):
       if request.method == 'POST':
         
        productname=request.POST.get('productname')
        mrp=request.POST.get('selllingpricemrp')
        adminpc=request.POST.get('admin_per')
        selllingprice=request.POST.get('sprice')
        cost2me=request.POST.get('cost2me')
        BV=request.POST.get('BV')
        categry=request.POST.get('categry')
        descript=request.POST.get('descript')
        volume=request.POST.get('volume')
        brands=request.POST.get('brands')
        disc_pc=request.POST.get('disc_pc')
        vendor_disc_pc=request.POST.get('vendor_discpc')
        man_dt=request.POST.get('man_dt')
        ex_dt=request.POST.get('ex_dt')
        barcode=request.POST.get('barcode')
        img1=request.FILES.get('img1')
        img2=request.FILES.get('img2')
        img3=request.FILES.get('img3')
        img4=request.FILES.get('img4')
        img5=request.FILES.get('img5')
        mart_flag=request.POST.get('martid')
        gst_seller=request.POST.get('gst')
        vendor_name=request.POST.get('vendor')

        cgst=request.POST.get('cgst')
        sgst=request.POST.get('sgst')
        invoice_nm=request.POST.get('invoice')
        hsn=request.POST.get('hsn')
        pos_flag=request.POST.get('pos_flag')

        print("-------------->>>>>>--",cgst,"-->>>",sgst)

       #'uploads/products/default-profile-.png'

        if not img1:
           img1='uploads/products/default-profile-.png'
        
        if not img2:
           img2='uploads/products/default-profile-.png'

        if not img3:
           img3='uploads/products/default-profile-.png'

        if not img4:
           img4='uploads/products/default-profile-.png'

        if not img5:
           img5='uploads/products/default-profile-.png'

        catg_obj=Category.objects.get(name=str(categry).strip())


        ## check if product already exists ##
        if not mart_flag:
           mart_flag=0
        if not barcode:
           barcode='X'
        if not gst_seller:
           gst_seller='-'


        if not vendor_name:
           vendor_name='-'

        if not sgst:
           sgst=0
        if not cgst:
           cgst=0

        if not invoice_nm:
           invoice_nm='-'

        if not hsn:
           hsn='-'

        if not vendor_disc_pc:
           vendor_disc_pc=0

        try:
           
           prod_pos_obj = Product.objects.get(barcode=barcode)

         
           print("------ product already in repository --------")

           print(prod_pos_obj.name,' ',prod_pos_obj.MRP)
           prod_to_upd=prod_pos_obj
        except:  
           prod_obj=Product(name=productname,
                         price=mrp,
                         MRP=mrp,
                         cost_price=cost2me,
                         admin_percentage=adminpc,
                         sell_price=selllingprice,
                         category_id=catg_obj.id,
                         description=descript,
                         BV_gained=BV,
                         image=img1,
                         image1=img2,
                         image2=img3,
                         image3=img4,
                         image4=img5,
                         quantity=volume,
                         Product_brand=brands,
                         discount=disc_pc,
                         manufactur_date=man_dt,
                         expiry_date=ex_dt,
                         barcode=barcode,
                         mart_flag=mart_flag,
                         seller_gst=gst_seller,
                         seller_name=vendor_name,
                         sgst=sgst,
                         cgst=cgst,
                         invoice_nm=invoice_nm,
                         hsn=hsn,
                         discount_by_vendor=vendor_disc_pc
                         )
        
           prod_obj.save()
        prod_items = Product.objects.all()
        print('-----inside load post function---')
        messages="Product stored successfully!"
        if pos_flag ==1 :
           resp={}
           
           resp['prod_pos_obj']=prod_pos_obj
           
           return HttpResponse(json.dumps(resp), content_type="application/json")
        else:
           return render(request ,'load_products.html' ,{'prod_items' : prod_items,'messages':messages,'prod_to_upd':prod_to_upd})
