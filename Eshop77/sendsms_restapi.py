import requests

url = "https://api.txtconsole.com/v1/sms"

payload = {
    "source": "varun",
    "destination": "+919354562833",
    "text": "hello world this is good"
}
headers = {
    "accept": "application/json",
    "content-type": "application/json",
    "authorization": "Basic SGx4RDVMREFjbWVxako2OkN4OFp1TUhz"
}

response = requests.post(url, json=payload, headers=headers)

print(response.text)


#https://txtconsole.readme.io/reference/post_sms
#https://ozeki-sms-gateway.com
#https://ozekisms.com/p_7050-how-to-setup-an-smpp-sms-gateway.html
#https://ozekisms.com/p_2145-smpp-gateway.html#:~:text=Although%20there%20are%20no%20free,of%20your%20Android%20mobile%20phone.
#https://ozekisms.com/p_2145-smpp-gateway.html#:~:text=Although%20there%20are%20no%20free,of%20your%20Android%20mobile%20phone.
