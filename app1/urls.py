from django.urls import path
from app1 import views

urlpatterns = [
    path('', views.home, name="home"),
    path("addition", views.addition, name="addition")
]
