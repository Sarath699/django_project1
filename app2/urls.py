from django.urls import path
from app2 import views

urlpatterns = [
    path('', views.travello, name="travello")
]
