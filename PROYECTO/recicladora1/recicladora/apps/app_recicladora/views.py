# Create your views here.
from recicladora.apps.app_recicladora.models import *
from django.shortcuts import render_to_response
from recicladora.apps.app_recicladora.forms import *
from django.http import *
from django.template import *

#cosas para usuarios

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required


def inicio(request):
    return render_to_response('index.html',context_instance = RequestContext(request))

@login_required(login_url='/ingresar')
def nueva_ruta(request):
	if request.method=='POST':
		formulario=rutaForm(request.POST)
		if formulario.is_valid():
			formulario.save()
			return HttpResponseRedirect('/')
	else:
		formulario=rutaForm()
	return render_to_response('ruta.html',locals(),context_instance=RequestContext(request))

@login_required(login_url='/ingresar')
def rutas_pendientes(request):
	a=ruta.objects.filter(status=1)
	return render_to_response('rutas_pendientes.html',locals(),context_instance=RequestContext(request))

@login_required(login_url='/ingresar')
def rutas_proceso(request):
	a=ruta.objects.filter(status=2)
	return render_to_response('rutas_proceso.html',locals(),context_instance=RequestContext(request))

@login_required(login_url='/ingresar')
def camiones(request,id_ruta):
	id_ruta=ruta.objects.get(id=id_ruta)
	a=camion.objects.filter(status=1)
	return render_to_response('camiones_disponibles.html',locals(),context_instance=RequestContext(request))

@login_required(login_url='/ingresar')
def trabajadores(request,id_ruta,id_camion):
	id_ruta=ruta.objects.get(id=id_ruta)
	id_camion=camion.objects.get(id=id_camion)
	a=trabajador.objects.all()
	return render_to_response('trabajadores.html',locals(),context_instance=RequestContext(request))

@login_required(login_url='/ingresar')
def asignar(request,id_ruta,id_camion,id_trabajador):
	id_ruta=ruta.objects.filter(id=id_ruta).values('id')
	id_ruta=id_ruta[0]['id']

	id_camion=camion.objects.filter(id=id_camion).values('id')
	id_camion=id_camion[0]['id']

	id_trabajador=trabajador.objects.filter(id=id_trabajador).values('id')
	id_trabajador=id_trabajador[0]['id']

	p=asigana(ruta_id=id_ruta,camion_id=id_camion,trabajador_id=id_trabajador)
	p.save()

	camion.objects.filter(id=id_camion).update(status=0)
	ruta.objects.filter(id=id_ruta).update(status=2)
	return HttpResponseRedirect('/')

@login_required(login_url='/ingresar')
def terminar(request,id_ruta):
	id_camion=asigana.objects.filter(ruta_id=id_ruta).values('camion')
	id_camion=id_camion[0]['camion']

	ruta.objects.filter(id=id_ruta).update(status=3)

	camion.objects.filter(id=id_camion).update(status=1)

	return HttpResponseRedirect('/editar/precio/%s'%id_ruta)

@login_required(login_url='/ingresar')
def camions(request):
	a=camion.objects.filter(status=1)
	b=camion.objects.filter(status=2)


	return render_to_response('camiones_reparar.html',locals(),context_instance=RequestContext(request))

@login_required(login_url='/ingresar')
def  mantenimiento1(request,id_camion):
	camion.objects.filter(id=id_camion).update(status=2)

	id_camion=camion.objects.filter(id=id_camion).values('id')
	id_camion=id_camion[0]['id']

	p=mantenimiento(camion_id=id_camion)
	p.save()

	return HttpResponseRedirect('/')

@login_required(login_url='/ingresar')
def  editar_precio(request,id_ruta):
	p=ruta.objects.get(id=id_ruta)

	if request.method=='POST':
		form= rutaForm(request.POST,request.FILES)
		if form.is_valid():
			
			nombre=form.cleaned_data['nombre']
			direccion=form.cleaned_data['direccion']
			costo_compra=form.cleaned_data['costo_compra']

			p.nombre=nombre
			p.direccion=direccion
			p.costo_compra=costo_compra
			p.save()

			return HttpResponseRedirect('/')
	if request.method=='GET':
		form = rutaForm(initial={
			'nombre':p.nombre,
			'direccion':p.direccion,
			'costo_compra':p.costo_compra,
			'status':3,
			})
	ctx={'formulario':form,'p':p}
	return render_to_response('editarPrecio.html',ctx,context_instance=RequestContext(request))


@login_required(login_url='/ingresar')
def estadoDe_camiones(request):
	a=camion.objects.all()
	return render_to_response('estados_camiones.html',locals(),context_instance=RequestContext(request))

@login_required(login_url='/ingresar')
def sacarMantenimiento(request,id_camion):
	camion.objects.filter(id=id_camion).update(status=1)
	mantenimiento.objects.filter(camion_id=id_camion,status=1).update(status=0)
	return HttpResponseRedirect('/')

@login_required(login_url='/ingresar')
def historialMantenimiento(request):
	mantenimientoProceso=mantenimiento.objects.filter(status=1)
	mantenimientoHechos=mantenimiento.objects.filter(status=0)
	return render_to_response('histoMantenimiento.html',locals(),context_instance=RequestContext(request))

@login_required(login_url='/ingresar')
def historialRutas(request):
	a=ruta.objects.filter(status=3)
	return render_to_response('histoRuta.html',locals(),context_instance=RequestContext(request))

@login_required(login_url='/ingresar')
def totalCamiones(request):
	a=camion.objects.all()
	return render_to_response('camiones.html',locals(),context_instance=RequestContext(request))

@login_required(login_url='/ingresar')
def totalTrabajadores(request):
	a=trabajador.objects.all()
	return render_to_response('histoTrabajadores.html',locals(),context_instance=RequestContext(request))

@login_required(login_url='/ingresar')
def nueva_aseguradora(request):
	if request.method=='POST':
		formulario=aseguradoraForm(request.POST)
		if formulario.is_valid():
			formulario.save()
			return HttpResponseRedirect('/')
	else:
		formulario=aseguradoraForm()
	return render_to_response('aseguradora.html',locals(),context_instance=RequestContext(request))

@login_required(login_url='/ingresar')
def camion_aseguradora_formulario(request):
	if request.method=='POST':
		formulario=camion_aseguradoraForm(request.POST)
		if formulario.is_valid():
			formulario.save()
			return HttpResponseRedirect('/')
	else:
		formulario=camion_aseguradoraForm()
	return render_to_response('asignar_aseguradora.html',locals(),context_instance=RequestContext(request))


@login_required(login_url='/ingresar')
def camiones_asegurados1(request):
	a=camion_aseguradora.objects.all()
	return render_to_response('camiones_asegurados.html',locals(),context_instance=RequestContext(request))

@login_required(login_url='/ingresar')
def aseguradoras_view(request):
	a=aseguradora.objects.all()
	return render_to_response('consulta_aseguradoras.html',locals(),context_instance=RequestContext(request))

@login_required(login_url='/ingresar')
def altaTrabajadores(request):
	if request.method=='POST':
		formulario=alta_empleadoForm(request.POST)
		if formulario.is_valid():
			formulario.save()
			return HttpResponseRedirect('/')
	else:
		formulario=alta_empleadoForm()
	return render_to_response('alta_empleado.html',locals(),context_instance=RequestContext(request))

@login_required(login_url='/ingresar')
def altaUnidad(request):
	if request.method=='POST':
		formulario=alta_camionForm(request.POST)
		if formulario.is_valid():
			formulario.save()
			return HttpResponseRedirect('/')
	else:
		formulario=alta_camionForm()
	return render_to_response('alta_unidad.html',locals(),context_instance=RequestContext(request))
