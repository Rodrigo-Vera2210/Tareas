from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import *
from rest_framework.routers import DefaultRouter


urlpatterns = [
    path('',TareaListView.as_view()),
    path('crear/',CrearTareaApiView.as_view(), name='crearTarea'),
    path('update/<int:pk>',ActualizarTarea.as_view()),
    path('delete/<int:pk>',EliminarTarea.as_view()),
]
