from django.shortcuts import render , redirect , HttpResponseRedirect ,HttpResponse
from django.contrib.auth.hashers import  check_password
from store.models.customer import Customer
from django.views import  View


def cart_quantity(request):
    #print("cart objects --->>>>",request.session.get('cart'));
    try:
        cart_count=len([i for i,j in request.session.get('cart').items() if int(j)>0 ])
    except :
        cart_count=0
    return HttpResponse(cart_count)


