from code import InteractiveConsole
from threading import activeCount
from django.shortcuts import redirect, render, HttpResponse
from .forms import CargoForm, DepartamentoForm, EmpleadoForm
from .models import Cargo, Departamento, Empleado

# Create your views here.
def inicio(request):
    #return HttpResponse("<h1>Bienvenido a mi Sitio Web</h1>")
    return render(request, "inicio.html")

# vistas de cargos

def crearCargo(request):
    print(request)
    print(request.method)
    if request.method == "POST":
        print("Entró por POST")
        cargo_form = CargoForm(request.POST) 
        if cargo_form.is_valid():
            cargo_form.save()
    else:
        print("Entró por GET")
    cargo_form = CargoForm() #instanciando formulario
    cargos = Cargo.objects.all()
    return render(request, "pages/cargo.html",{'CargoForm':cargo_form,'cargos':cargos,'accion':'Crear'})

def insertarCargo(request):
    if request.method == "POST":
        print("Entró por POST")
        cargo_form = CargoForm(request.POST) 
        if cargo_form.is_valid():
            cargo_form.save()
            return redirect('cargo') 
    else:
        print("Entró por GET")
    cargo_form = CargoForm() #instanciando formulario
    cargos = Cargo.objects.all()
    return render(request, "pages/insertarCargo.html",{'CargoForm':cargo_form,'cargos':cargos, 'accion':'Crear'})


def editarCargo(request,id):
    error, cargo_form= None, None
    try:
        cargo = Cargo.objects.get(id=id)
        if request.method == "GET":
            cargo_form = CargoForm(instance=cargo)
        else:
            cargo_form = CargoForm(request.POST,instance=cargo) 
        if cargo_form.is_valid():
            cargo_form.save()
            return redirect('cargo') 
    except Exception as e:
            error = e
    cargos = Cargo.objects.all()
    return render(request, "pages/insertarCargo.html",{'CargoForm':cargo_form,'cargos':cargos, 'accion':'Actualizar'})


def eliminarCargo(request,id):
    cargo = Cargo.objects.get(id=id)
    if request.method == "POST":
        #ELIMINACION FISICA DEL REGISTRO
        print(cargo)
        cargo.delete()
        #ELIMINACION LOGICA DEL REGISTRO
        #cargo.estado=False
        #cargo.save()
        #Regresa al listado de cargos
        return redirect("cargo")
    return render(request, "pages/eliminarCargo.html",{'cargo':cargo})




# vistas de departamentos

def crearDepartamento(request):
    print(request)
    print(request.method)
    if request.method == "POST":
        print("Entró por POST")
        departamento_form = DepartamentoForm(request.POST) 
        if departamento_form.is_valid():
            departamento_form.save()
    else:
        print("Entró por GET")
    departamento_form = DepartamentoForm() #instanciando formulario
    departamentos = Departamento.objects.all()
    return render(request, "pages/departamento.html",{'DepartamentoForm':departamento_form,'departamentos':departamentos, 'accion':'Crear'})

def insertarDepartamento(request):
    print(request)
    print(request.method)
    if request.method == "POST":
        print("Entró por POST")
        departamento_form = DepartamentoForm(request.POST) 
        if departamento_form.is_valid():
            departamento_form.save()
            return redirect('departamento')
    else:
        print("Entró por GET")
    departamento_form = DepartamentoForm() #instanciando formulario
    departamentos = Departamento.objects.all()
    return render(request, "pages/insertarDepartamento.html",{'DepartamentoForm':departamento_form,'departamentos':departamentos, 'accion':'Crear'})

def editarDepartamento(request,id):
    error, departamento_form= None, None
    try:
        departamento = Departamento.objects.get(id=id)
        if request.method == "GET":
            departamento_form = DepartamentoForm(instance=departamento)
        else:
            departamento_form = DepartamentoForm(request.POST,instance=departamento) 
        if departamento_form.is_valid():
            departamento_form.save()
            return redirect('departamento') 
    except Exception as e:
            error = e
    departamentos = Departamento.objects.all()
    return render(request, "pages/insertarDepartamento.html",{'DepartamentoForm':departamento_form,'departamentos':departamentos, 'accion':'Actualizar'})


def eliminarDepartamento(request,id):
    departamento = Departamento.objects.get(id=id)
    if request.method == "POST":
        #ELIMINACION FISICA DEL REGISTRO
        print(departamento)
        departamento.delete()
        #ELIMINACION LOGICA DEL REGISTRO
        #cargo.estado=False
        #cargo.save()
        #Regresa al listado de cargos
        return redirect("departamento")
    return render(request, "pages/eliminarDepartamento.html",{'departamento':departamento})


# vistas de empleados

def crearEmpleado(request):
    print(request)
    print(request.method)
    if request.method == "POST":
        print("Entró por POST")
        empleado_form = EmpleadoForm(request.POST) 
        if empleado_form.is_valid():
            empleado_form.save()
    else:
        print("Entró por GET")
    empleado_form = EmpleadoForm() #instanciando formulario
    empleados = Empleado.objects.all()
    return render(request, "pages/empleado.html",{'EmpleadoForm':empleado_form,'empleados':empleados, 'accion':'Crear'})

def insertarEmpleado(request):
    print(request)
    print(request.method)
    if request.method == "POST":
        print("Entró por POST")
        empleado_form = EmpleadoForm(request.POST) 
        if empleado_form.is_valid():
            empleado_form.save()
            return redirect('empleado')
    else:
        print("Entró por GET")
    empleado_form = EmpleadoForm() #instanciando formulario
    empleados = Empleado.objects.all()
    return render(request, "pages/insertarEmpleado.html",{'EmpleadoForm':empleado_form,'empleados':empleados, 'accion':'Crear'})

def editarEmpleado(request,id):
    error, empleado_form= None, None
    try:
        empleado = Empleado.objects.get(id=id)
        if request.method == "GET":
            empleado_form = EmpleadoForm(instance=empleado)
        else:
            empleado_form = EmpleadoForm(request.POST,instance=empleado) 
        if empleado_form.is_valid():
            empleado_form.save()
            return redirect('empleado') 
    except Exception as e:
            error = e
    empleados = Empleado.objects.all()
    return render(request, "pages/insertarEmpleado.html",{'EmpleadoForm':empleado_form,'empleados':empleados, 'accion':'Actualizar'})


def eliminarEmpleado(request,id):
    empleado = Empleado.objects.get(id=id)
    if request.method == "POST":
        #ELIMINACION FISICA DEL REGISTRO
        print(empleado)
        empleado.delete()
        #ELIMINACION LOGICA DEL REGISTRO
        #cargo.estado=False
        #cargo.save()
        #Regresa al listado de cargos
        return redirect("empleado")
    return render(request, "pages/eliminarEmpleado.html",{'empleado':empleado})
    




# def cargo(request):
#     #return HttpResponse("<h1>Mantenimiento de Cargos</h1>")
#     return render(request, "pages/cargo.html")
# def departamento(request):
#     #return HttpResponse("<h1>Mantenimiento de Departamentos</h1>")
#     return render(request, "pages/departamento.html")
# def empleado(request):
#     #return HttpResponse("<h1>Mantenimiento de Empleados</h1>")   
#     return render(request, "pages/empleado.html")
    