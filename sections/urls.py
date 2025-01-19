
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('sections/', views.section_list, name='section_list'),
    path('users/', views.user_list, name='user_list'),
    path('users/create/', views.create_user, name='create_user'),
    path('users/delete/<int:user_id>/', views.delete_user, name='delete_user'),
    path('sections/create/', views.create_section, name='create_section'),
    path('sections/delete/<int:section_id>/', views.delete_section, name='delete_section'),
    path('sections/<int:section_id>/remove_user/<int:user_id>/', views.remove_user_from_section, name='remove_user_from_section'),
]