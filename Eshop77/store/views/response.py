
from django.shortcuts import render , redirect , HttpResponseRedirect ,HttpResponse

from django.views import  View
 

class out_response(View):
    def get(self , request,orderid):
        print(f'/store{request.get_full_path()[1:]}')
        return render (request , 'payment.html')
        #return HttpResponseRedirect(f'/store{request.get_full_path()[1:]}')

    def post(self, request,orderid):
        return render (request , 'payment.html')