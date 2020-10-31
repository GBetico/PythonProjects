from django.contrib import admin

# Register your models here.
from empleado.models import TipoEmpleado
from empleado.models import Empleado

admin.site.register(TipoEmpleado)

admin.site.register(Empleado)

