import requests
  
def sendsms(order):  
  print("--->",order['orderid'],order['order_price'])

    
  # url = "https://www.fast2sms.com/dev/bulkV2"
  
  # querystring = {
  #   "authorization": "z8FCDG6e74BvwtRNIU9YcsqKdbAWh2g1xQfrioTpMjuyEP3XHJ0ix2Snuvqah3co8PjQYAHTy1OWJRrE",
  #   "message": "This is Message sent from\
  #        Adven India .Your order with order id "+str(order['orderid'])+" with payable amount Rs."+str(order['order_price'])+" is confirmed. Please share payment screenshot to +918382919600\
  #        for assistance",
  #   "language": "english",
  #   "route": "q",
  #   "numbers": "8382919600,9354562833"} ## change user phone number
  
  # headers = {
  #   'cache-control': "no-cache"
  # }
  # try:
  #   response = requests.request("GET", url,
  #                               headers = headers,
  #                               params = querystring)
      
  #   print("SMS Successfully Sent")
  # except:
  #   print("Oops! Something wrong")