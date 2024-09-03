from django.urls import path
from blog.views import (
            pages_list,  
            page_create, 
            page_edit,  
            page_success, 
            page_delete,
            page_detail,


)

urlpatterns = [
    path('pages/', pages_list, name='pages_list'),  # Lista de blogs
    path('create/', page_create, name='page_create'),  # Crear blog
    path('<int:pk>/delete/', page_delete, name='page_delete'),   # Borrar blog
    path('<int:pk>/', page_detail, name='page_detail'),  # Detalle del blog
    path('edit/<int:pk>/', page_edit, name='page_edit'), #Editar blog
    path('success/', page_success, name='success'),

]
