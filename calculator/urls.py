from django.urls import path
from . import views

urlpatterns = [
    path('', views.calculator_request, name="calculator_request"),
]