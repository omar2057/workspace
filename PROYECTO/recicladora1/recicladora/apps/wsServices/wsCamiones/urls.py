from django.conf.urls import patterns, include, url



urlpatterns = patterns('recicladora.apps.wsServices.wsCamiones.views',
	    #cosas de usuarios
    url(r'^ws','wsCamion'),
  
    )