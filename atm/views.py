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
	# // https://www.twilio.com/console/phone-numbers/verified
	account_sid = "AC9e2ec3e819222baac7d6d520cdf79897"
	auth_token  = "a0664845c9fa0e0dc0340a663a2c2159"
	client = Client(account_sid, auth_token)
	to = "+91"+phone
	msg = "Your OTP for cardless transaction is "+otp+". It will be valid for 10 minutes. Do not disclose this to anyone."
	message = client.messages.create(
	    body=msg,
	    to=to,
	    from_="+18173859700"
	    )
	print (to, message.sid)

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
		return render(request,'card.html')
	else:
		return HttpResponse("Invalid OTP")

def checkValidAndOTP(request):
	print ("hello world")
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