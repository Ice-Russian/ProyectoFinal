from django.urls import path
from blog.views import inicio, about_view, pages_list, page_detail, page_create, page_edit, page_delete






urlpatterns = [
    path('about/', about_view, name='about'),
    path('', inicio, name='index'),  # Página de inicio
    path('pages/', pages_list, name='pages_list'),  # Lista de blogs
    path('pages/<int:page_id>/', page_detail, name='page_detail'),  # Detalle del blog
    path('pages/create/', page_create, name='page_create'),  # Crear nuevo blog
    path('pages/<int:page_id>/edit/', page_edit, name='page_edit'),  # Editar blog
    path('pages/<int:page_id>/delete/', page_delete, name='page_delete'),  # Borrar blog
]
