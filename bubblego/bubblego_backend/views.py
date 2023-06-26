from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import bubblego_backend.controller as controller

from bubblego_backend.models import Appointment, Service


def index(request):
	return HttpResponse("Hello BubbleGo!")
	
def services(request):
	if request.method == 'GET':
		data = controller.get_services()
		return JsonResponse({'data': data[1]}, status = data[0])

def appointments(request):
	if request.method == 'GET':
		data = controller.get_appointments()
		return JsonResponse({'data': data[1]}, status = data[0])
	if request.method == 'POST':
		return JsonResponse({'message': 'Request received'}, status = 200)

