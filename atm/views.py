from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.http import HttpResponseNotFound
from django.shortcuts import render_to_response
from atm.models import Bank_Details
from twilio.rest import Client
from django.core.exceptions import ObjectDoesNotExist
import math, random 

# Create your views here.
def sendSmsToPhone(phone, otp):
	
	

	# account_sid = "AC9e2ec3e819222baac7d6d520cdf79897"
	# auth_token  = "a0664845c9fa0e0dc0340a663a2c2159"
	# client = Client(account_sid, auth_token)
	# to = "+919476212584"
	# message = client.messages.create(
	#     body="Your otp is "+otp,
	#     to=to,
	#     from_="+18173859700"
	#     )
	# print (message.sid)

	# url = "https://www.fast2sms.com/dev/bulk"
	# payload = "sender_id=FSTSMS&message=goodMorning&language=english&route=p&numbers=9476212584"
	# headers = {
	# 'authorization': "wKxiMZ6zATtErGc7HFWadSYLX0oOCmleBNq9b23U5JyhP4ug1fJCv9zUMQysPkhwqTZ6IH5clp2F3N7X",
	# 'Content-Type': "application/x-www-form-urlencoded",
	# 'Cache-Control': "no-cache",
	# }
	# response = requests.request("POST", url, data=payload, headers=headers)
	# print(response.text)

	import requests

	url = "https://www.fast2sms.com/dev/bulk"

	querystring = {"authorization":"wKxiMZ6zATtErGc7HFWadSYLX0oOCmleBNq9b23U5JyhP4ug1fJCv9zUMQysPkhwqTZ6IH5clp2F3N7X","sender_id":"FSTSMS","message":"This is test message","language":"english","route":"p","numbers":"9476212584"}

	headers = {
	    'cache-control': "no-cache"
	}

	response = requests.request("GET", url, headers=headers, params=querystring)

	print(response.text)

def generateOTP() :  
    digits = "0123456789"
    OTP = "" 
    for i in range(6) : 
        OTP += digits[math.floor(random.random() * 10)] 
    return OTP 

def home(request):
	print("Here")
	return render(request,'index.html')

def cardless(request):
	print("cardless")
	return render(request,'cardless.html')

def view_screen(request):
	print("view")
	return render(request,'card.html')

def card(request):
	print("card")
	return redirect(reverse('atm:view_screen'))

def verifyOTP(request):
	print('verifyOTP')
	phone = request.POST['phone']
	otp = request.POST['otp']
	try:
		det = Bank_Details.objects.get(phone=phone)
	except ObjectDoesNotExist:
		return HttpResponse("False")
	if det.otp == otp: 
		return redirect(reverse('atm:view_screen'))
	else:
		return HttpResponse("Invalid OTP")

def checkValidAndOTP(request):
	phone = request.POST['phone']
	pin = request.POST['pin']
	try:
		det = Bank_Details.objects.get(phone=phone,pin=pin)
		det.otp = generateOTP()
		sendSmsToPhone(phone, det.otp)
		det.save()
		return HttpResponse("True")
	except ObjectDoesNotExist:
		return HttpResponse("False")