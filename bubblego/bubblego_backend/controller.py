

from bubblego_backend.models import Appointment, Service
from django.core.exceptions import ObjectDoesNotExist


def get_services():
    services_list = Service.objects.values_list('id', flat = True)
    if services_list.count() > 0:
        return 200, [get_service(service_id)[1] for service_id in services_list]
    else:
        return 204, 'There are no Service objects'


def get_service(id):
    try:
        service = Service.objects.get(pk = id)
        service_json = {
            'id': id,
            'service_title': service.service_title,
            'checkbox_status': service.checkbox_status,
            'price': service.price,
        }
        return 200, service_json
    except ObjectDoesNotExist:
        return 204, 'Service with {0} does not exist'.format(id)

def get_appointments():
    appointments_list = Appointment.objects.values_list('id', flat = True)
    if appointments_list.count() > 0:
        return 200, [get_appointment(service_id)[1] for service_id in appointments_list]
    else:
        return 204, 'There are no Appointments objects'

def get_appointment(id):
    try:
        appointment = Appointment.objects.get(pk = id)
        appointment_json = {
                'id': id,
                'services_list': [get_service(service.id)[1] for service in appointment.services_list.all()],
                'location': appointment.location,
                'details': appointment.details,
                'final_price': appointment.final_price,
                'payment_status': appointment.payment_status
            }
        return 200, appointment_json
    except ObjectDoesNotExist:
        return 204, 'Appointment with {0} does not exist'.format(id)