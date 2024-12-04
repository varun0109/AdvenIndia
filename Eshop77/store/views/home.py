from django.shortcuts import render , redirect , HttpResponseRedirect ,HttpResponse
from store.models.product import Product
from store.models.category import Category
from store.models.customer import Customer
from store.models.addfavourites import favourite
from django.conf import settings
from django.views import View
from django.db.models import Q  # New
from math import radians, cos, sin, asin, sqrt
from store.models.orders import Order
from django.http import JsonResponse
 


# Create your views here.#
class Index(View):
     
     
    def post(self , request):
        aj_call=0
        product=request.POST.get('product')
        quantity=request.POST.get('quantity')
        aj_call=request.POST.get('aj_counter')
        
        cart = request.session.get('cart')
        
        
        if cart:
            cart[product]=quantity
            request.session['cart']=cart
            
        else:
            cart={}
            cart[product]=quantity
            request.session['cart']=cart

        if  aj_call=='1':
            print('ajcall is 1')
            return HttpResponse('success')
        else:
            print('ajcall is 0')
            return redirect('homepage')
        

      



    def get(self , request):
        
        return HttpResponseRedirect(f'/store')
        #return render(request,'index.html')

def store(request):
    
    cart = request.session.get('cart')
    
    if not cart:
        request.session['cart'] = {}
    products = None
    categories = Category.get_all_categories()
    categoryID = request.GET.get('category')
    if categoryID:
        products = Product.get_all_products_by_categoryid(categoryID)
    else:
        products = Product.get_all_products();
     

    data = {}
    ## change it ############################################################
    #favourite_items=set()
    
    #favs_qset=favourite.get_all_favs_by_customerid(request.session['customer']);

    #converting favourite_qset to list for filter condition in template
    #if favs_qset:
    #  for i_fav in favs_qset:
    #    favourite_items.add(i_fav.favourites.id)
    #else :
    customer_favs={}
    all_favs=[]
    #favourite_items=favourites.objects.get(customer=request.session['customer'])
    data['products'] = products
    data['categories'] = categories
    
    #data['favs']=favourite_items 
    #print('favourite_items--->',favourite_items) #######
    disp_thumbnailcat=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    data['disp_list']=disp_thumbnailcat  #thumbnail to be displayed only for these categories
    print('in cart')
    
    if 'customer' in request.session.keys():
        customer_favs=favourite.get_all_favs_by_customerid(request.session['customer']);
        for fav_item in customer_favs:
            all_favs.append(fav_item.favourites.id)
        
    else:
        customer_favs=[-99]
    data['customer_favs']=all_favs
    print("###",all_favs)
    return render(request, 'index.html', data)


def index_search(request):
    search_post = request.GET.get('search')
    categories = Category.get_all_categories()
    data = {}
    data['categories'] = categories

    if search_post:
      searched_products = Product.objects.filter(Q(name__icontains=search_post) | Q(description__icontains=search_post))
      data['products'] = searched_products
      for i_product in searched_products:
        print(i_product)
    else:
    # If not searched, return default posts
      products = Product.objects.all()
      data['products']=products
    return render(request, 'index_search.html', data)
    # return HttpResponse(search_post)

def category(request):
    return render(request, 'category.html')

def add_favourite(request):
    productid=request.GET['productid']

    if 'customer' in request.session.keys():
        customer=Customer.objects.get(pk=request.session['customer'])
        product=Product.objects.get(pk=productid)
        fav=favourite(favourites=product,customer=customer)
        fav.save()
        login_error='none'
    else :
        print('user not logged in ')
        login_error='User not logged in'
    
    return JsonResponse({'login_error':login_error})
     

def rem_favourite(request):
    productid=request.GET['productid']
    ## if customer exists 
    ## change here to flash login message in casr not logged on
    customer=Customer.objects.get(pk=request.session['customer'])
    product=Product.objects.get(pk=productid)
    favourite.objects.filter(favourites=product,customer=customer).delete()
    return HttpResponse('green')

def favourites(request):
    favourite_items={}
    favs=favourite.get_all_favs_by_customerid(request.session['customer']);
    for i in favs:
        print(i)
    favourite_items['favs']=favs
    
    return render(request,'favourites.html',favourite_items)

def searchlocation(request):
    store_long1=settings.STORE_LONGITUDE
    store_lat1=settings.STORE_LATITUDE
    
    store_long2=settings.STORE_LONGITUDE2
    store_lat2=settings.STORE_LATITUDE2

    store_long1=radians(float(store_long1))
    store_lat1=radians(float(store_lat1))

    store_long2=radians(float(store_long2))
    store_lat2=radians(float(store_lat2))

    zipcode=request.GET['zipcode']
    
    with open('store/zipcodes/postalcode.csv' , 'r') as f:
      for line in f:
         pincode=line.split(';')[1]
         
         if pincode.strip() ==str(zipcode.strip()) :
            place=line.split(';')[2]
            state=line.split(';')[3]
            coor=line.split(';')[-1]
            lat2=coor.split(',')[0]
            long2=coor.split(',')[1]
            city=line.split(';')[5]
            break
         else:
            place='zip not found'
            state=' '
            city=''
            long2=0
            lat2=0

    #postal code of user #
    long2=radians(float(long2))
    lat2=radians(float(lat2)) 
    # Haversine formula
    dlon = long2 - store_long1
    dlat = lat2 - store_lat1

    dlon2 = long2 - store_long2
    dlat2 = lat2 - store_lat2

    a = sin(dlat / 2)**2 + cos(store_lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * asin(sqrt(a))
    
    a2 = sin(dlat2 / 2)**2 + cos(store_lat2) * cos(lat2) * sin(dlon2 / 2)**2
    c2=2 * asin(sqrt(a2))
    # Radius of earth in kilometers. Use 3956 for miles
    r = 6371
    #calculate result
    d1='%.3f'%(c * r  )

    d2='%.3f'%(c2 * r  )

    if d1<d2 :
        d=d1
    else:
        d=d2

    location={}
    location['place']=place
    location['state']=state
    location['d']=d
    location['city']=city
    
    ## make it json
    loc_data=str(place)+'-'+str(state)+'-'+str(d)+'-'+city
    

    return HttpResponse(loc_data) ## make it json and pass

    
def itemdetails(request):
    return render(request,'itemdetails.html')


def aboutus(request):
    return render(request,'about.html')


def usrprofile(request):
    if 'customer' in request.session.keys():
      customer=Customer.objects.get(pk=request.session['customer'])
      print('customer',customer.username)
      print('customer first name',customer.first_name)
      return render(request,'store_profile.html',{'customer':customer})
    
    else :
        return render(request,'index.html')



def parse_orders(request):
    ord2cnf = []
    if request.method == 'POST':
        ord2cnf = request.POST.getlist('ordchecks2')
        ord2rev = request.POST.getlist('ordchecks1')
        print()
        for upd_counter in ord2cnf:
             print('upd_counterupd_counter',upd_counter)
             ord_upd=Order.objects.get(id=upd_counter)
             ord_upd.status=True
             ord_upd.save()

             
        for upd_counter2 in ord2rev:
             print('revert order',upd_counter2)
             ord_upd2=Order.objects.get(id=upd_counter2)
             ord_upd2.status=False
             ord_upd2.save()

    return JsonResponse({'ord_upd':ord2cnf,'ord_rev':ord2rev})

def edit_prod(request):
    if request.method == 'POST':
        prdname = str(request.POST.get('prdname')).strip()
        prdprice=request.POST.get('prdprice')
        prdmrp=request.POST.get('prdmrp')
        admprc=request.POST.get('admprc')
        bvg=request.POST.get('bvg')
        prddsc=request.POST.get('prddsc')
        prdbr=request.POST.get('prdbr')
        productid=request.POST.get('prdid')  
        sell_price=request.POST.get('sell_price') 


        product_obj=Product.objects.get(pk=productid)

        product_obj.cost_price=prdprice
        product_obj.price=prdmrp
        product_obj.name=prdname
        product_obj.MRP=prdmrp
        product_obj.admin_percentage=admprc
        product_obj.BV_gained=bvg
        product_obj.description=prddsc
        product_obj.Product_brand=prdbr
        product_obj.sell_price=sell_price

        product_obj.save()
       

 
    return JsonResponse({'prdname':prdname,'prdprice':prdprice,'prdmrp':prdmrp,'admprc':admprc,'bvg':bvg,'prddsc':prddsc,'prdbr':prdbr})

def del_prod(request):
    if request.method == 'POST':
        productid=request.POST.get('prdid')
        msg="none"
        try:
          product_obj=Product.objects.get(pk=productid).delete()
          msg='success'
        except:
            print('no product found')
            msg='failed'
    


    return JsonResponse({'msg':msg})




 
    
  

 


  
    
     
