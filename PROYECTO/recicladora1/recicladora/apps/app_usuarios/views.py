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


@login_required(login_url='/ingresar')
def nuevo_usuario(request):
    if request.method == 'POST':
        formulario = UserCreationForm(request.POST)
        if formulario.is_valid():
	    	formulario.save()
	return HttpResponseRedirect('/')
    else:
        formulario = UserCreationForm()
    return render_to_response('nuevousuario.html',{'formulario':formulario}, context_instance = RequestContext(request))

def ingresar(request):
    if request.method == 'POST':
        formulario=AuthenticationForm(request.POST)
        if formulario.is_valid:
            usuario = request.POST['username']
            clave = request.POST['password']
            acceso = authenticate(username=usuario,password=clave)
            if acceso is not None:
                if acceso.is_active:
                    login(request,acceso)
                    return HttpResponseRedirect('/')
                else:
                    return render_to_response('noactivo.html', context_instance=RequestContext(request))
            else:
                return render_to_response('nousuario.html', context_instance=RequestContext(request))
    else:
        formulario = AuthenticationForm()
    return render_to_response('ingresar.html',{'formulario':formulario}, context_instance=RequestContext(request))
    if not request.user.is_anonymous():
        return HttpResponseRedirect('/privado')

@login_required(login_url='/ingresar')
def privado(request):
    usuario=request.user
    return render_to_response('privado.hmtl',locals(),context_instance=RequestContext(request))

@login_required(login_url='/ingresar')
def cerrar(request):
    logout(request)
    return render_to_response('index.html',context_instance=RequestContext(request))
