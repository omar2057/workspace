# Create your views here.

from django.http import HttpResponse
from recicladora.apps.app_recicladora.models import *

from django.core import serializers



def wsCamion(request):
	data=serializers.serialize('json',mantenimiento.objects.filter(status=0))
	return HttpResponse(data,mimetype='application/json')