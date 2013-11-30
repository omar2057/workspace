from django.conf.urls import patterns, include, url
import settings
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'recicladora.views.home', name='home'),
    # url(r'^recicladora/', include('recicladora.foo.urls')),
    url(r'^media/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.MEDIA_ROOT}),
    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    #cosas usuaurios
    url(r'^', include('recicladora.apps.app_usuarios.urls')),

    #Cosas rutas
    url(r'^$', 'recicladora.apps.app_recicladora.views.inicio'),
    url(r'^nueva_ruta/', 'recicladora.apps.app_recicladora.views.nueva_ruta'),
    url(r'^rutas_pendientes/', 'recicladora.apps.app_recicladora.views.rutas_pendientes'),
    url(r'^rutas_proceso/', 'recicladora.apps.app_recicladora.views.rutas_proceso'),
    url(r'^camiones/(?P<id_ruta>.*)','recicladora.apps.app_recicladora.views.camiones'),
    url(r'^trabajador/(?P<id_ruta>.*)/(?P<id_camion>.*)/','recicladora.apps.app_recicladora.views.trabajadores'),
    url(r'^asignar/(?P<id_ruta>.*)/(?P<id_camion>.*)/(?P<id_trabajador>.*)/','recicladora.apps.app_recicladora.views.asignar'),
    url(r'^terminar/(?P<id_ruta>.*)/','recicladora.apps.app_recicladora.views.terminar'),
    
    #Editar precio de la ruta terminada
    url(r'^editar/precio/(?P<id_ruta>.*)/','recicladora.apps.app_recicladora.views.editar_precio'),

    #Cosas mantenimineto
    url(r'^camion/','recicladora.apps.app_recicladora.views.camions'),
    url(r'^mantenimiento/(?P<id_camion>.*)/','recicladora.apps.app_recicladora.views.mantenimiento1'),
    url(r'^estados/camiones/','recicladora.apps.app_recicladora.views.estadoDe_camiones'),
    url(r'^sacar/camion/(?P<id_camion>.*)/','recicladora.apps.app_recicladora.views.sacarMantenimiento'),
    url(r'^historial/mantenimiento/','recicladora.apps.app_recicladora.views.historialMantenimiento'),
    url(r'^historial/rutas/','recicladora.apps.app_recicladora.views.historialRutas'),

    #Cosas adminsitrativas
    url(r'^administrativo/camiones/','recicladora.apps.app_recicladora.views.totalCamiones'),
    url(r'^administrativo/trabajadores/','recicladora.apps.app_recicladora.views.totalTrabajadores'),
    url(r'^alta/empleado/','recicladora.apps.app_recicladora.views.altaTrabajadores'),
    url(r'^alta/unidad/','recicladora.apps.app_recicladora.views.altaUnidad'),
        #aseguradora
        url(r'^aseguradoras/','recicladora.apps.app_recicladora.views.aseguradoras_view'),
        url(r'^administrativo/nueva_aseguradora/','recicladora.apps.app_recicladora.views.nueva_aseguradora'),
        url(r'^aseguradora/camion/','recicladora.apps.app_recicladora.views.camion_aseguradora_formulario'),
        url(r'^asegurados/','recicladora.apps.app_recicladora.views.camiones_asegurados1'),


    #json
    url(r'^', include('recicladora.apps.wsServices.wsCamiones.urls')),
)

