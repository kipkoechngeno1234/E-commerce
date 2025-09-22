from django.urls import path
from .import views

urlpatterns = [
    path('Hello/', views.a_tech, name="Hello")
]