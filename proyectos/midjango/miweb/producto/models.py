from django.db import models

# Create your models here.
class TipoProducto(models.Model):
	descripcion = models.CharField(max_length=100)
	def __str__(self):
		return self.descripcion

class Producto(models.Model):
	tipo_producto = models.ForeignKey(TipoProducto,on_delete=models.CASCADE)
	descripcion = models.CharField(max_length=100)
	def __str__(self):
		return self.descripcion