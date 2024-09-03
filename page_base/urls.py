from .views import inicio, about_view
from django.urls import path

urlpatterns = [
    path('about/', about_view, name='about'),
    path('', inicio, name='index'),  # Página de inicio
]


