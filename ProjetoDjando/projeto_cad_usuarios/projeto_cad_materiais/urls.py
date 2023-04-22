from django.urls import path
from app_cad_materiais import views

urlpatterns = [
    path('', views.home,name='home'),
]
