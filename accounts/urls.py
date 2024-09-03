from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('profile/edit/', views.profile_edit, name='profile_edit'),
    path('register_success/', views.register_success, name='register_success'),
    path('profile/', views.profile, name='profile'),
]
