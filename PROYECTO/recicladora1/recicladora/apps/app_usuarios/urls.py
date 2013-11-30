from django.conf.urls import patterns, include, url



urlpatterns = patterns('recicladora.apps.app_usuarios.views',
	    #cosas de usuarios
    url(r'^usuario','nuevo_usuario'),
    url(r'^ingresar','ingresar'),
    url(r'^privado','privado'),
    url(r'^cerrar$', 'cerrar'),
    )