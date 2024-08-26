from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('profile/edit/', views.profile_edit, name='profile_edit'),
    path('register_success/', views.register_success, name='register_success'),
]

urlpatterns += [
    path('profile/', views.profile, name='profile'),
    path('post/edit/<int:post_id>/', views.edit_post, name='edit_post'),
    path('post/create/', views.create_post, name='create_post'),
    path('post/delete/<int:post_id>/', views.delete_post, name='delete_post'),
]