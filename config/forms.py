from django import forms

class CursoFormulario(forms.Form):
    curso = forms.CharField(max_length=20)
    comision = forms.IntegerField()

class BuscaCursoForm(forms.Form):
    nombre = forms.CharField()

class EstudianteFormulario(forms.Form):
    nombre = forms.CharField(max_length=20)
    apellido = forms.CharField(max_length=20)
    email = forms.EmailField(required=False)

class BuscarEstudianteForm(forms.Form):
    nombre = forms.CharField(max_length=20)

class ProfesorFormulario(forms.Form):
    nombre = forms.CharField(max_length=20)
    apellido =forms.CharField(max_length=20)
    email =forms.EmailField(required=False)
    profesion =forms.CharField(max_length=20)

class BuscarProfesorForm(forms.Form):
    nombre = forms.CharField(max_length=20)

class EntregableFormulario(forms.Form):
    nombre = forms.CharField(max_length=20)
    fecha_de_entrega = forms.DateField()
    entregado = forms.BooleanField()