from django.shortcuts import render
from admin_user.models import Curso, Estudiante, Profesor, Entregable
from config.forms import EntregableFormulario
# Create your views here.


# Paginas de Inicio

def inicio(request):
    return render(request, "admin_user/index.html")
def curso(request):
    return render(request, "admin_user/cursos.html")
def estudiantes(request):
    return render(request, "admin_user/estudiantes.html")
def profesores(request):
    return render(request, "admin_user/profesores.html")
def entregables(request):
    return render(request, "admin_user/entregrable.html")

# Fin de paginas de inicio

# Entregable

def entrega(request):
    if request.method == 'POST':
        formEntregables = EntregableFormulario(request.POST)
        if formEntregables.is_valid():
            informacion = formEntregables.cleaned_data
            entregable = Entregable(nombre=informacion["nombre"], fecha_de_entrega=informacion["fecha_de_entrega"], entregado=informacion["entregado"])
            entregable.save()
            
            return render(request, "admin_user/AccionExitosa.html")
    else:
        formEntregables = EntregableFormulario()

    return render(request, "admin_user/entregables.html", {"formEntregables": formEntregables})

# Fin entregable