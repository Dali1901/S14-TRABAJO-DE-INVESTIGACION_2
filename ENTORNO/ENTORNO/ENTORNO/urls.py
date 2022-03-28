"""ENTORNO URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from unicodedata import name
from django.contrib import admin
from django.urls import path
from mantenimiento.views import inicio,crearCargo,editarCargo,eliminarCargo,crearDepartamento,editarDepartamento,eliminarDepartamento,crearEmpleado,editarEmpleado,eliminarEmpleado,insertarCargo,insertarDepartamento,insertarEmpleado

urlpatterns = [

    path('admin/', admin.site.urls),
    path('',inicio,name="inicio"),
    #path('cargo/',cargo,name="cargo"),
    
    path('cargo/',crearCargo,name="cargo"),
    path('insertarCargo',insertarCargo,name="insertarCargo"),
    path('editarCargo/<int:id>/',editarCargo ,name="editarCargo"),
    path('eliminarCargo/<int:id>/',eliminarCargo ,name="eliminarCargo"),

    path('departamento/',crearDepartamento,name="departamento"),
    path('insertarDepartamento',insertarDepartamento,name="insertarDepartamento"),
    path('editarDepartamento/<int:id>/',editarDepartamento ,name="editarDepartamento"),
    path('eliminarDepartamento/<int:id>/',eliminarDepartamento ,name="eliminarDepartamento"),

    path('empleado/',crearEmpleado,name="empleado"),
    path('insertarEmpleado',insertarEmpleado,name="insertarEmpleado"),
    path('editarEmpleado/<int:id>/',editarEmpleado ,name="editarEmpleado"),
    path('eliminarEmpleado/<int:id>/',eliminarEmpleado ,name="eliminarEmpleado")


]
