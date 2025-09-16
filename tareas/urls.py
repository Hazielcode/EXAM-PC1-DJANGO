from django.contrib import admin
from django.urls import path
from gestor import views

urlpatterns = [
    path('', views.lista_tareas, name='lista_tareas'),
    path('tareas/nueva/', views.crear_tarea, name='crear_tarea'),
    path('tareas/<int:id>/editar/', views.editar_tarea, name='editar_tarea'),
    path('tareas/<int:id>/eliminar/', views.eliminar_tarea, name='eliminar_tarea'),
    path('categorias/', views.lista_categorias, name='lista_categorias'),
    path('categorias/nueva/', views.crear_categoria, name='crear_categoria'),
    path('categorias/<int:id>/editar/', views.editar_categoria, name='editar_categoria'),
    path('categorias/<int:id>/eliminar/', views.eliminar_categoria, name='eliminar_categoria'),

]
