from django.urls import path
from blog.views import ( inicio, 
                        about_view, 
                        pages_list,  
                        page_create, 
                        page_edit,  
                        page_success, 
                        PageDeleteView,
                        PageDetailView,
                        PageUpdateView,

)




urlpatterns = [
    path('about/', about_view, name='about'),
    path('', inicio, name='index'),  # Página de inicio
    path('pages/', pages_list, name='pages_list'),  # Lista de blogs
    path('pages/create/', page_create, name='page_create'),  # Crear nuevo blog
    path('blogpages/<int:pk>/delete/', PageDeleteView.as_view(), name='page_delete'),   # Borrar blog
    path('blogpages/<int:page_id>/', PageDetailView.as_view(), name='page_detail'),  # Detalle del blog
    path('edit/<int:pk>/', PageUpdateView.as_view(), name='page_edit'),
    path('success/', page_success, name='success'),

]

