from django import forms
from .models import Cargo, Departamento, Empleado

class CargoForm(forms.ModelForm):
    class Meta:
        model = Cargo        
        fields = ['descripcion','estado']  
        widgets = {
            'descripcion':forms.TextInput(attrs={
                'placeholder':'Nombre del Cargo',
                'class':'input',
                'required':True 
            })
        }        

class DepartamentoForm(forms.ModelForm):
    class Meta:
        model = Departamento        
        fields = ['descripcion','estado']  
        widgets = {
            'descripcion':forms.TextInput(attrs={
                'placeholder':'Nombre del Departamento',
                'class':'input',
                'required':True 
            })
        }            

class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = "__all__"
        widgets = {
            'nombre':forms.TextInput(attrs={
                'placeholder':'Ingrese su nombre',
                'class':'input',
                'required':True 
            }),
            'cedula':forms.TextInput(attrs={
                'placeholder':'Ingrese su n° de cédula',
                'class':'input',
                'required':True 
            }),
            'sueldo':forms.TextInput(attrs={
                'placeholder':'Ingrese su sueldo(USD)',
                'class':'input',
                'required':True 
            })
        }   



        
        
