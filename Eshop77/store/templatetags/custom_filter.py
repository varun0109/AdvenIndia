from django import template
from store.models.product import Product

register = template.Library()

@register.filter(name='currency')
def currency(number):
    return "₹ "+str(number)



@register.filter(name='multiply')
def multiply(number , number1):
    return number * number1


@register.filter(name='divide')
def divide(number , number1):
    if number1!=0:
       return number/number1
    else :
       return number


@register.filter(name='add')
def add(number , number1):
    return number + number1

@register.filter(name='subtract')
def subtract(number , number1):
    return abs(number - number1)

@register.filter(name='round_dec')
def round_dec(number):
    return round(number,2)

##will need to merge it with round_dec
@register.filter(name='round_dec1')
def round_dec1(number):
    return round(number,1)

## will need to be changed
@register.filter(name='gst_cal')
def gst_cal(prod_id):
    prod = Product.objects.get(id=prod_id)
    prod_after_discount=prod.cost_price-(prod.cost_price*prod.discount_by_vendor/100)
    prod_cgst=round(prod.cgst/100,4)
    prod_sgst=round(prod.cgst/100,4)
    prod_cgst_amt=prod_cgst*prod_after_discount*prod.quantity
    prod_sgst_amt=prod_sgst*prod_after_discount*prod.quantity
    prod_gst_amt=prod_cgst_amt+prod_sgst_amt
    return prod_gst_amt

 
 
     
 




