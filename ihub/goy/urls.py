from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add/', views.add_task, name='add_task'),
    path('eliminar/<int:id>/', views.eliminar, name='eliminar'),  # Añadir esta línea
    path('editar/<int:tarea_id>/', views.editar, name='editar'),  # Asegúrate de que esta línea esté correcta

    ]