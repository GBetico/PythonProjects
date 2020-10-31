from django.db import models

# Create your models here.
class TipoEmpleado(models.Model):
	descripcion = models.CharField(max_length=100)
	def __str__(self):
		return self.descripcion

class Empleado(models.Model):
	tipo_empleado = models.ForeignKey(TipoEmpleado,on_delete=models.CASCADE)
	Nombre = models.CharField(max_length=100)
	Apellido = models.CharField(max_length=100)
	Direccion = models.CharField(max_length=100)
	Telefono = models.CharField(max_length=10)
	Correo = models.CharField(max_length=100)
	
	def __str__(self):
		return self.descripcion