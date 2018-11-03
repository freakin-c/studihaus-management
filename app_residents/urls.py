from django.urls import path
from . import views

urlpatterns = [
        path('', views.residents, name='index'),
        path('<int:pk>/', views.resident, name='resident'),
]
