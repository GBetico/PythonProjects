from django.contrib import admin

# Register your models here.
from producto.models import TipoProducto
from producto.models import Producto

admin.site.register(TipoProducto)

admin.site.register(Producto)

