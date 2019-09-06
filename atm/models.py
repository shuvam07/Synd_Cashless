from django.db import models

# Create your models here.

class Bank_Details(models.Model):
	name = models.CharField(max_length=50)
	phone = models.CharField(max_length=10)
	pin = models.IntegerField(max_length=4)
	otp = models.CharField(max_length = 6,blank=True)
	