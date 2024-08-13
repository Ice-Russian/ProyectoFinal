from django.urls import path
from admin_user.views import *

urlpatterns = [
    path('', inicio, name='index'),

    path('cursos/', curso, name='cursos'),


    path('estudiantes/', estudiantes, name='estudiantes'),


    path('profesores/', profesores, name='profesores'),


    path('entregables/', entrega, name='entregables'),

]