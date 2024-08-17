from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    #path('create_post/', views.create_post, name='create_post'),
    path('profile/edit/', views.profile_edit, name='profile_edit'),
    path('register_success/', views.register_success, name='register_success'),
]

urlpatterns += [
    path('profile/', views.profile, name='profile'),
    path('profile/post/create/', views.create_post, name='create_post'),
    path('profile/post/<int:post_id>/edit/', views.edit_post, name='post_edit'),
    path('profile/post/<int:post_id>/delete/', views.delete_post, name='post_delete'),
]