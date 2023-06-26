from django.db import models


class Service(models.Model):
	checkbox_status = models.BooleanField(default = False)
	service_title = models.CharField(max_length = 60)
	price = models.CharField(max_length = 60)
	
	def __str__(self):
		return f'{self.service_title} | {self.price} Lei' 

class Appointment(models.Model):
	services_list = models.ManyToManyField(Service)
	location = models.CharField(max_length = 60)
	details = models.CharField(max_length = 200)
	final_price = models.CharField(max_length = 60)
	payment_status = models.BooleanField(default = False)
	
	def __str__(self):
		services = [service.__str__() for service in self.services_list.all()]
		return f'{services} | {self.location} | Payment {self.payment_status}' 
