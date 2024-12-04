from django.shortcuts import render , redirect , HttpResponseRedirect

from django.contrib.auth.hashers import  check_password
from store.models.customer import Customer
from django.views import  View


class Login(View):
    return_url = None
    def get(self , request):
        Login.return_url = request.GET.get('return_url')
        return render(request , 'login.html')

    def post(self , request):
        username = str(request.POST.get('username')).strip()
        password = request.POST.get('password')
        #customer = Customer.get_customer_by_email(email)
        customer = Customer.get_customer_by_username(str(username).lower().strip())
        print('username',username)
        print('password',password)
        error_message = None
        if customer:
            flag = check_password(password, customer.password)
            
            if flag:
                request.session['customer'] = customer.id
                request.session['username'] = customer.username
                print("--------------------------------------------------")
                print('customer.id --',customer.first_name ,'---',customer.last_name,'----',customer.phone)
                request.session['Name'] = customer.first_name + ' ' + customer.last_name
                request.session['Phone'] = customer.phone
                request.session['Address'] = '123 XYZ Karol Bagh , Delhi'

                if Login.return_url:
                    return HttpResponseRedirect(Login.return_url)
                else:
                    Login.return_url = None
                    return redirect('homepage')
            else:
                error_message = 'Email or Password invalid !!'
        else:
            error_message = 'Email or Password invalid !!'

         
        return render(request, 'login.html', {'error': error_message})

def logout(request):
    request.session.clear()
    return redirect('login')
