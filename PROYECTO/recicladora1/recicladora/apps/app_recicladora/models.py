from django.db import models

# Create your models here.
class estado(models.Model):
    estado=models.CharField(max_length=10)

    class Admin:
        pass

    class Meta:
        ordering = ['id']

    def __unicode__(self):
        return '%s'%(self.estado)

class ruta(models.Model):
    nombre=models.CharField(max_length=30)
    direccion=models.CharField(max_length=100)
    costo_compra=models.IntegerField(null=True,blank=True)
    fecha=models.DateTimeField(auto_now=True)
    status=models.ForeignKey(estado,default=1)

    class Admin:
        pass

    class Meta:
        ordering = ['fecha']

    def __unicode__(self):
        return '%s,%s,%s'%(self.nombre,self.direccion,self.fecha)

class trabajador(models.Model):
    nombre=models.CharField(max_length=20)
    apellido=models.CharField(max_length=20)
    telefono=models.CharField(max_length=15)

    class Admin:
        pass

    class Meta:
        ordering = ['nombre']

    def __unicode__(self):
        return '%s'%(self.nombre)

class camion(models.Model):
    serie=models.CharField(max_length=10)
    marca=models.CharField(max_length=20)
    placa_camion=models.CharField(max_length=10)
    placa_caja=models.CharField(max_length=10)
    status=models.IntegerField(default=1)

    class Admin:
        pass

    class Meta:
        ordering = ['serie']

    def __unicode__(self):
        return '%s'%(self.serie)

class asigana(models.Model):
    ruta=models.ForeignKey(ruta)
    camion=models.ForeignKey(camion)
    trabajador=models.ForeignKey(trabajador)
    fecha=models.DateTimeField(auto_now=True)

    class Admin:
        pass

    class Meta:
        ordering = ['fecha']

    def __unicode__(self):
        return '%s'%(self.ruta)

class mantenimiento(models.Model):
    camion=models.ForeignKey(camion)
    fecha=models.DateTimeField(auto_now=True)
    status=models.BooleanField(default=1)

    class Admin:
        pass

    class Meta:
        ordering = ['fecha']

    def __unicode__(self):
        return '%s'%(self.fecha)

class aseguradora(models.Model):
    proveedor=models.CharField(max_length=50)
    direccion=models.CharField(max_length=100)
    telefono=models.CharField(max_length=10)

    class Admin:
        pass

    def __unicode__(self):
        return '%s'%(self.proveedor)

class camion_aseguradora(models.Model):
    proveedor=models.ForeignKey(aseguradora)
    camion=models.ForeignKey(camion)
    fecha_inicio=models.DateTimeField(auto_now=True)
    fecha_fin=models.DateTimeField()

    class Admin:
        pass

    def __unicode__(self):
        return '%s'%(self.fecha_inicio)