from . import views
from django.urls import path


urlpatterns = [
    path('edit/<int:post_id>/', views.edit_post, name='edit_post'),
    path('create/', views.create_post, name='create_post'),
    path('delete/<int:post_id>/', views.delete_post, name='delete_post'),
]