from django import template

register = template.Library()

@register.filter(name='is_in_cart')
def is_in_cart(product  , cart):
    if product and cart.keys():
        cart_keys = cart.keys()
        keys=[key for key in cart_keys if key !='null' ]
        for id in keys:
                if int(id) == product.id:
                    return True
         
    return False;


@register.filter(name='cart_quantity')
def cart_quantity(product  , cart):
    if cart:
        keys = cart.keys()
        for id in keys:
            if int(id) == product.id:
                return cart.get(id)
        return 0;
    return 0;


@register.filter(name='price_total')
def price_total(product  , cart):
    if cart and product  :
        return round((product.price - ((product.discount*product.price)/100)) * int(cart_quantity(product , cart)),2)
    return 0


@register.filter(name='total_cart_price')
def total_cart_price(products , cart):
    sum = 0 ;
    for p in products:
        sum += price_total(p , cart)
        

    return round(sum,2)
    
@register.filter(name='afterdiscount')
def afterdiscount( beforediscount ,discount ):
    return round((beforediscount - ((discount * beforediscount)/100)),2)


 