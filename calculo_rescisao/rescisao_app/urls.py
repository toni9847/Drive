from django.urls import path
from .views import calcular_rescisao

urlpatterns = [
    path('<int:funcionario_id>/', calcular_rescisao, name='calcular_rescisao'),
]
